"""RPC and chain safety policy — enforced, not documented.

The repository rule: never a public RPC, always Alchemy with a key. For local
scenarios nothing upstream is needed at all; for future fork scenarios the
upstream URL is constructed HERE from ALCHEMY_API_KEY and never shown to the
agent, the logs, or the results.
"""
import os
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent.parent

# hostnames that must never be used as an upstream for a scored task
PUBLIC_RPC_HOSTS = {
    "mainnet.base.org", "base.llamarpc.com", "eth.llamarpc.com",
    "cloudflare-eth.com", "rpc.ankr.com", "eth.public-rpc.com",
    "ethereum.publicnode.com", "ethereum-rpc.publicnode.com",
    "rpc.flashbots.net", "1rpc.io", "eth.drpc.org",
}

ALCHEMY_HOSTS = {
    "mainnet": "eth-mainnet.g.alchemy.com",
    "sepolia": "eth-sepolia.g.alchemy.com",
    "base": "base-mainnet.g.alchemy.com",
    "arbitrum": "arb-mainnet.g.alchemy.com",
    "optimism": "opt-mainnet.g.alchemy.com",
}


def load_alchemy_key():
    """ALCHEMY_API_KEY from the environment or the gitignored .env."""
    key = os.environ.get("ALCHEMY_API_KEY", "")
    if not key:
        env = HERE / ".env"
        if env.exists():
            for line in env.read_text().splitlines():
                m = re.match(r"\s*ALCHEMY_API_KEY\s*=\s*['\"]?([\w-]+)", line)
                if m:
                    key = m.group(1)
    return key


def alchemy_url(chain="mainnet"):
    key = load_alchemy_key()
    if not key:
        raise SystemExit(
            "ALCHEMY_API_KEY not found in env or .env — fork scenarios refuse "
            "to run without it (no public-RPC fallback, ever). Grab a free key "
            "at https://dashboard.alchemy.com and add it to .env.")
    return f"https://{ALCHEMY_HOSTS[chain]}/v2/{key}"


def assert_upstream_allowed(url):
    """A scored fork task may only use a local node or an Alchemy endpoint."""
    host = (urlparse(url).hostname or "").lower()
    if host in ("127.0.0.1", "localhost", "::1"):
        return
    if host in PUBLIC_RPC_HOSTS:
        raise ValueError(f"public RPC {host} is forbidden for scored tasks")
    if host not in set(ALCHEMY_HOSTS.values()):
        raise ValueError(f"unrecognized upstream {host} — only local or Alchemy allowed")


def redact(text, extra_secrets=()):
    """Mask the Alchemy key (and any extra secrets) anywhere in text."""
    for secret in [load_alchemy_key(), *extra_secrets]:
        if secret:
            text = text.replace(secret, "«REDACTED»")
    return text
