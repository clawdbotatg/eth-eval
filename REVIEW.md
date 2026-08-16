# eth-eval — all 176 tasks for review


## tasks/gen-calldata.jsonl

### calldata-sel-01  (computed)
**Q:** What is the 4-byte function selector for the Solidity function `setOperator(address)`?

Answer with only the 0x-prefixed hex selector.

**Grader:** `{"type": "exact", "expect": "0xb3ab15fb"}`
**Reference:** 0xb3ab15fb

### calldata-sel-02  (computed)
**Q:** What is the 4-byte function selector for the Solidity function `claimRewardsFor(bool,address,bytes32)`?

Answer with only the 0x-prefixed hex selector.

**Grader:** `{"type": "exact", "expect": "0xd58fd9a7"}`
**Reference:** 0xd58fd9a7

### calldata-sel-03  (computed)
**Q:** What is the 4-byte function selector for the Solidity function `stakeFor(uint256,address,bytes32)`?

Answer with only the 0x-prefixed hex selector.

**Grader:** `{"type": "exact", "expect": "0xa3b1e76e"}`
**Reference:** 0xa3b1e76e

### calldata-sel-04  (computed)
**Q:** What is the 4-byte function selector for the Solidity function `redeemV2(bytes32)`?

Answer with only the 0x-prefixed hex selector.

**Grader:** `{"type": "exact", "expect": "0x99119479"}`
**Reference:** 0x99119479

### calldata-sel-05  (computed)
**Q:** What is the 4-byte function selector for the Solidity function `liquidate(bytes32)`?

Answer with only the 0x-prefixed hex selector.

**Grader:** `{"type": "exact", "expect": "0x0a71096e"}`
**Reference:** 0x0a71096e

### calldata-enc-01  (computed)
**Q:** ABI-encode a call to the Solidity function `claimRewards(bool,address)` with arguments: bool = true, address = 0x32a78bf36789defc38cb0e58a0bbce41e052013e.

Answer with only the full 0x-prefixed calldata hex string.

**Grader:** `{"type": "exact", "expect": "0x8f1dae29000000000000000000000000000000000000000000000000000000000000000100000000000000000000000032a78bf36789defc38cb0e58a0bbce41e052013e"}`
**Reference:** 0x8f1dae29000000000000000000000000000000000000000000000000000000000000000100000000000000000000000032a78bf36789defc38cb0e58a0bbce41e052013e

### calldata-enc-02  (computed)
**Q:** ABI-encode a call to the Solidity function `updateOracle(address)` with arguments: address = 0x5562dffdbe5c76f87400c317ef8e85404a769f92.

Answer with only the full 0x-prefixed calldata hex string.

**Grader:** `{"type": "exact", "expect": "0x1cb44dfc0000000000000000000000005562dffdbe5c76f87400c317ef8e85404a769f92"}`
**Reference:** 0x1cb44dfc0000000000000000000000005562dffdbe5c76f87400c317ef8e85404a769f92

### calldata-enc-03  (computed)
**Q:** ABI-encode a call to the Solidity function `rebalance(address,uint256)` with arguments: address = 0xbb339dad6bffddc62b666ca0bff22e277ea2fd24, uint256 = 360623057.

Answer with only the full 0x-prefixed calldata hex string.

**Grader:** `{"type": "exact", "expect": "0x3da9b9d0000000000000000000000000bb339dad6bffddc62b666ca0bff22e277ea2fd2400000000000000000000000000000000000000000000000000000000157eabd1"}`
**Reference:** 0x3da9b9d0000000000000000000000000bb339dad6bffddc62b666ca0bff22e277ea2fd2400000000000000000000000000000000000000000000000000000000157eabd1

### calldata-enc-04  (computed)
**Q:** ABI-encode a call to the Solidity function `harvest(bool,uint256)` with arguments: bool = true, uint256 = 821316524.

Answer with only the full 0x-prefixed calldata hex string.

**Grader:** `{"type": "exact", "expect": "0xd02221a300000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000030f44bac"}`
**Reference:** 0xd02221a300000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000030f44bac

### calldata-dec-01  (computed)
**Q:** A contract has these functions:
- redeem(bool)
- bridgeOut(uint256,address,uint256)
- rebalanceFor(uint256,bool)

This calldata is sent to it:
0xeca349000000000000000000000000000000000000000000000000000000000016f581ca000000000000000000000000881b4ebc64a78eb2b9e5fb967bd68e88ffb22c8d00000000000000000000000000000000000000000000000000000000310d9c52

Which function is being called, and with what arguments?

Reply with JSON only: {"function": "<name>", "args": [...]} — addresses as 0x strings, uints as numbers, bools as true/false.

**Grader:** `{"type": "json", "expect": {"function": "bridgeOut", "args": [385188298, "0x881b4ebc64a78eb2b9e5fb967bd68e88ffb22c8d", 822975570]}}`
**Reference:** {"function": "bridgeOut", "args": [385188298, "0x881b4ebc64a78eb2b9e5fb967bd68e88ffb22c8d", 822975570]}

### calldata-dec-02  (computed)
**Q:** A contract has these functions:
- withdrawToV2(uint256,uint256)
- redeemV2(address,uint256,bool)
- claimRewardsFor(uint256,address,uint256)

This calldata is sent to it:
0xfdf7c73c000000000000000000000000191745cf0679cfe3188e56135ca504d22300711500000000000000000000000000000000000000000000000000000000147d4a0a0000000000000000000000000000000000000000000000000000000000000000

Which function is being called, and with what arguments?

Reply with JSON only: {"function": "<name>", "args": [...]} — addresses as 0x strings, uints as numbers, bools as true/false.

**Grader:** `{"type": "json", "expect": {"function": "redeemV2", "args": ["0x191745cf0679cfe3188e56135ca504d223007115", 343755274, false]}}`
**Reference:** {"function": "redeemV2", "args": ["0x191745cf0679cfe3188e56135ca504d223007115", 343755274, false]}

### calldata-dec-03  (computed)
**Q:** A contract has these functions:
- bridgeOutFor(bool,uint256,uint256)
- redeemFor(bool,address)
- delegateVotes(uint256)

This calldata is sent to it:
0xba10205a0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000c4d9cb82f0a80d126547355c5cfbb18fe30c7c9c

Which function is being called, and with what arguments?

Reply with JSON only: {"function": "<name>", "args": [...]} — addresses as 0x strings, uints as numbers, bools as true/false.

**Grader:** `{"type": "json", "expect": {"function": "redeemFor", "args": [true, "0xc4d9cb82f0a80d126547355c5cfbb18fe30c7c9c"]}}`
**Reference:** {"function": "redeemFor", "args": [true, "0xc4d9cb82f0a80d126547355c5cfbb18fe30c7c9c"]}

### calldata-dec-04  (computed)
**Q:** A contract has these functions:
- updateOracleV2(uint256,uint256)
- rebalance(address,bool,uint256)
- swapExact(uint256,uint256)

This calldata is sent to it:
0xfe90357c000000000000000000000000794f812efe8f79aaa4e640dcee6943c3af709a9100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007363d97

Which function is being called, and with what arguments?

Reply with JSON only: {"function": "<name>", "args": [...]} — addresses as 0x strings, uints as numbers, bools as true/false.

**Grader:** `{"type": "json", "expect": {"function": "rebalance", "args": ["0x794f812efe8f79aaa4e640dcee6943c3af709a91", false, 120995223]}}`
**Reference:** {"function": "rebalance", "args": ["0x794f812efe8f79aaa4e640dcee6943c3af709a91", false, 120995223]}

### calldata-dec-05  (computed)
**Q:** A contract has these functions:
- setOperatorFor(bool,address,uint256)
- setOperatorV2(bool,uint256)
- redeem(uint256,uint256,bool)

This calldata is sent to it:
0xb5d6656c00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000035edca99

Which function is being called, and with what arguments?

Reply with JSON only: {"function": "<name>", "args": [...]} — addresses as 0x strings, uints as numbers, bools as true/false.

**Grader:** `{"type": "json", "expect": {"function": "setOperatorV2", "args": [false, 904776345]}}`
**Reference:** {"function": "setOperatorV2", "args": [false, 904776345]}

### calldata-dec-06  (computed)
**Q:** A contract has these functions:
- claimRewards(address,uint256)
- delegateVotes(bool)
- claimRewardsV2(bool)

This calldata is sent to it:
0x9a99b4f000000000000000000000000078734594190e530da3d738d8083583f58e95dd80000000000000000000000000000000000000000000000000000000001a1939e7

Which function is being called, and with what arguments?

Reply with JSON only: {"function": "<name>", "args": [...]} — addresses as 0x strings, uints as numbers, bools as true/false.

**Grader:** `{"type": "json", "expect": {"function": "claimRewards", "args": ["0x78734594190e530da3d738d8083583f58e95dd80", 437860839]}}`
**Reference:** {"function": "claimRewards", "args": ["0x78734594190e530da3d738d8083583f58e95dd80", 437860839]}


## tasks/gen-derivations.jsonl

### derivations-create-01  (computed)
**Q:** An EOA at 0x9D2912E25AbA50dDA580b03ade947b7C79B56596 sends a contract-creation transaction (plain CREATE) with account nonce 482.

What address will the new contract be deployed at?

Answer with only the address (any casing).

**Grader:** `{"type": "exact", "expect": "0x8127b89F87710FD86b2FcdfFBD33373eBb007ffD"}`
**Reference:** 0x8127b89F87710FD86b2FcdfFBD33373eBb007ffD

### derivations-create-02  (computed)
**Q:** An EOA at 0x2f2445B9E88ED8634049bA1aa1A60597B468D824 sends a contract-creation transaction (plain CREATE) with account nonce 224.

What address will the new contract be deployed at?

Answer with only the address (any casing).

**Grader:** `{"type": "exact", "expect": "0xF14640c01CC374CFf3420162207e85e54D40bb11"}`
**Reference:** 0xF14640c01CC374CFf3420162207e85e54D40bb11

### derivations-create-03  (computed)
**Q:** An EOA at 0xaEa1CCe4D2BA42A6579a74Cee63Ec34d166d4E44 sends a contract-creation transaction (plain CREATE) with account nonce 394.

What address will the new contract be deployed at?

Answer with only the address (any casing).

**Grader:** `{"type": "exact", "expect": "0xdB6b8d23D7817b8306EFe1Ce343f24f5971A88ba"}`
**Reference:** 0xdB6b8d23D7817b8306EFe1Ce343f24f5971A88ba

### derivations-create2-01  (computed)
**Q:** Compute the CREATE2 address for:
- deployer: 0x51e58baae07e5e42a589e35115c342778f053454
- salt: 0xe91fa9a70fee436e2236b7ac281f33dfd126394d92b4efe1206c6e89dbfddc64
- keccak256(init_code): 0xfa0d476db4609708045a254354dd942fa0f715e781227f850a557d27b02dd280

Answer with only the resulting address (any casing).

**Grader:** `{"type": "exact", "expect": "0x549bfbe18fc93e9649235d1a48ff59c7e4a3a50e"}`
**Reference:** 0x549bfbe18fc93e9649235d1a48ff59c7e4a3a50e

### derivations-create2-02  (computed)
**Q:** Compute the CREATE2 address for:
- deployer: 0xccdb65fd5314ac104b74580d4b0a454654f48959
- salt: 0xa204749b9dee703e1f34fc0d3457329dedc55c03ba4058285e141d8bcc38a578
- keccak256(init_code): 0xee2efcebb888f2a2b1f6a64c8342bafefe6c0540fb2e4bd2a6fb4fe93d7b48cc

Answer with only the resulting address (any casing).

**Grader:** `{"type": "exact", "expect": "0x08db4c1f1014fbc875a36302403a21facbf7f862"}`
**Reference:** 0x08db4c1f1014fbc875a36302403a21facbf7f862

### derivations-create2-03  (computed)
**Q:** Compute the CREATE2 address for:
- deployer: 0x5c305883bba2a4551b25947565a83d5bf8e5c0bd
- salt: 0xc1b9843a4478dd57c479a1ee47dbfbd9d551f407c7bdc783190212275429984d
- keccak256(init_code): 0x7f0b9f4a970e20ed191b06972af7958e1a2e7a57ecc5a8be0f083fee3f758ce7

Answer with only the resulting address (any casing).

**Grader:** `{"type": "exact", "expect": "0x033343e32b1e9c7c377267324c0dfbf58523c16b"}`
**Reference:** 0x033343e32b1e9c7c377267324c0dfbf58523c16b

### derivations-slot-01  (computed)
**Q:** A Solidity contract declares `mapping(address => uint256) balances;` at storage slot 8.

What storage slot holds `balances[0x325233368573facf351e9deb22d802736340b358]`?

Answer with only the 0x-prefixed 32-byte slot as hex.

**Grader:** `{"type": "exact", "expect": "0x327fbfa5f389fb5378a83cbc95040727947b6771a4fd5caddb00ef403b0a3807"}`
**Reference:** 0x327fbfa5f389fb5378a83cbc95040727947b6771a4fd5caddb00ef403b0a3807

### derivations-slot-02  (computed)
**Q:** A Solidity contract declares `mapping(address => uint256) balances;` at storage slot 10.

What storage slot holds `balances[0x2704007563c3ecd1e756ce7de5748254e0ce506c]`?

Answer with only the 0x-prefixed 32-byte slot as hex.

**Grader:** `{"type": "exact", "expect": "0xc9c483381f9a3720fb8ec955d5ea135c47dda5adb3c10eb5a22da6454385878d"}`
**Reference:** 0xc9c483381f9a3720fb8ec955d5ea135c47dda5adb3c10eb5a22da6454385878d

### derivations-slot-03  (computed)
**Q:** A Solidity contract declares `mapping(address => uint256) balances;` at storage slot 8.

What storage slot holds `balances[0x32d0c26f1e914ae9bca27afa0226655597431328]`?

Answer with only the 0x-prefixed 32-byte slot as hex.

**Grader:** `{"type": "exact", "expect": "0xcb2150a0ab28533d4bfa750c4ac33b8207cfbd73029d5a386b01e8607246d3ee"}`
**Reference:** 0xcb2150a0ab28533d4bfa750c4ac33b8207cfbd73029d5a386b01e8607246d3ee

### derivations-slot-04  (computed)
**Q:** A Solidity contract declares `mapping(address => uint256) balances;` at storage slot 0.

What storage slot holds `balances[0x64424d01ead88586a769d1ccd0edc5046df4bb9d]`?

Answer with only the 0x-prefixed 32-byte slot as hex.

**Grader:** `{"type": "exact", "expect": "0x3587e8658ebed48e758aad9788988c61499dec07456052d160ee349350f93c92"}`
**Reference:** 0x3587e8658ebed48e758aad9788988c61499dec07456052d160ee349350f93c92


## tasks/gen-gas.jsonl

### gas-intrinsic-01  (computed)
**Q:** A simple value-transfer transaction to an EOA carries this calldata:
0x0046be6100d30000677700c4000000960022ac00009f76123a0000e8001b00ec00b54500e699

Using EIP-2028 calldata pricing (ignore the EIP-7623 floor and access lists), what is the transaction's intrinsic gas?

End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 21404}`
**Reference:** Answer: 21404

### gas-intrinsic-02  (computed)
**Q:** A simple value-transfer transaction to an EOA carries this calldata:
0x00a600760060fd8545da0000004000d2c80000c000930000d4b50011

Using EIP-2028 calldata pricing (ignore the EIP-7623 floor and access lists), what is the transaction's intrinsic gas?

End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 21292}`
**Reference:** Answer: 21292

### gas-intrinsic-03  (computed)
**Q:** A simple value-transfer transaction to an EOA carries this calldata:
0x000000000000d7201e010000c600b900006216d200000003e3004a00d9000000

Using EIP-2028 calldata pricing (ignore the EIP-7623 floor and access lists), what is the transaction's intrinsic gas?

End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 21284}`
**Reference:** Answer: 21284

### gas-intrinsic-04  (computed)
**Q:** A simple value-transfer transaction to an EOA carries this calldata:
0xf4acc8006b1a0000000000fe00290000c500df9a5b0000c6c20000ff1e00b30000b05400d68d1f

Using EIP-2028 calldata pricing (ignore the EIP-7623 floor and access lists), what is the transaction's intrinsic gas?

End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 21408}`
**Reference:** Answer: 21408

### gas-basefee-01  (computed)
**Q:** An EIP-1559 chain has a gas target of 15,000,000 per block. The base fee entering block 1 is 1400000000 wei.
Blocks execute as follows:
- block 1: 30,000,000 gas used
- block 2: 15,000,000 gas used

Using the exact EIP-1559 integer update rule, what is the base fee (in wei) entering the block AFTER the last one listed?

End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 1575000000}`
**Reference:** Answer: 1575000000

### gas-basefee-02  (computed)
**Q:** An EIP-1559 chain has a gas target of 15,000,000 per block. The base fee entering block 1 is 5900000000 wei.
Blocks execute as follows:
- block 1: 0 gas used
- block 2: 0 gas used
- block 3: 0 gas used

Using the exact EIP-1559 integer update rule, what is the base fee (in wei) entering the block AFTER the last one listed?

End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 3952539063}`
**Reference:** Answer: 3952539063

### gas-basefee-03  (computed)
**Q:** An EIP-1559 chain has a gas target of 15,000,000 per block. The base fee entering block 1 is 4800000000 wei.
Blocks execute as follows:
- block 1: 3,000,000 gas used
- block 2: 22,500,000 gas used

Using the exact EIP-1559 integer update rule, what is the base fee (in wei) entering the block AFTER the last one listed?

End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 4590000000}`
**Reference:** Answer: 4590000000

### gas-basefee-04  (computed)
**Q:** An EIP-1559 chain has a gas target of 15,000,000 per block. The base fee entering block 1 is 2400000000 wei.
Blocks execute as follows:
- block 1: 15,000,000 gas used
- block 2: 15,000,000 gas used
- block 3: 30,000,000 gas used

Using the exact EIP-1559 integer update rule, what is the base fee (in wei) entering the block AFTER the last one listed?

End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 2700000000}`
**Reference:** Answer: 2700000000


## tasks/gen-indexing.jsonl

### indexing-topic-01  (computed)
**Q:** A Solidity contract declares `event Harvested(bytes32, address, bytes32);`.

What is topic0 (the event signature hash) of the logs this event emits?

Answer with only the 0x-prefixed 32-byte hex value.

**Grader:** `{"type": "exact", "expect": "0xff6a5362202886553320d2a0d4b8c27404142647ec12d55162561be3e95febcb"}`
**Reference:** 0xff6a5362202886553320d2a0d4b8c27404142647ec12d55162561be3e95febcb

### indexing-topic-02  (computed)
**Q:** A Solidity contract declares `event Swapped(address);`.

What is topic0 (the event signature hash) of the logs this event emits?

Answer with only the 0x-prefixed 32-byte hex value.

**Grader:** `{"type": "exact", "expect": "0x9f9d8176388b18cf78a5d05972aa3601b5e5a8a6c6f5e62caa7f537a9663ef9a"}`
**Reference:** 0x9f9d8176388b18cf78a5d05972aa3601b5e5a8a6c6f5e62caa7f537a9663ef9a

### indexing-topic-03  (computed)
**Q:** A Solidity contract declares `event Liquidated(address, address, bytes32);`.

What is topic0 (the event signature hash) of the logs this event emits?

Answer with only the 0x-prefixed 32-byte hex value.

**Grader:** `{"type": "exact", "expect": "0xb642fd2c82e9fbe6ce65106e174fa319d852f58efffead26bb75c5cd061c9964"}`
**Reference:** 0xb642fd2c82e9fbe6ce65106e174fa319d852f58efffead26bb75c5cd061c9964

### indexing-topic-04  (computed)
**Q:** A Solidity contract declares `event RewardPaid(uint256);`.

What is topic0 (the event signature hash) of the logs this event emits?

Answer with only the 0x-prefixed 32-byte hex value.

**Grader:** `{"type": "exact", "expect": "0x67bb155fcabb99400c32b640dc7704c8f18aae4c817704c7267c5a8cd26dfc19"}`
**Reference:** 0x67bb155fcabb99400c32b640dc7704c8f18aae4c817704c7267c5a8cd26dfc19


## tasks/gen-units.jsonl

### units-01  (computed)
**Q:** Convert 412.5 gwei to wei.

End your reply with a line of the form "Answer: <integer>" (plain decimal, no separators).

**Grader:** `{"type": "bigint", "expect": 412500000000}`
**Reference:** Answer: 412500000000

### units-02  (computed)
**Q:** Convert 2.356 ether to wei.

End your reply with a line of the form "Answer: <integer>" (plain decimal, no separators).

**Grader:** `{"type": "bigint", "expect": 2356000000000000000}`
**Reference:** Answer: 2356000000000000000

### units-03  (computed)
**Q:** An ERC-20 token has 8 decimals. What raw integer amount represents 414 whole tokens?

End your reply with a line of the form "Answer: <integer>" (plain decimal, no separators).

**Grader:** `{"type": "bigint", "expect": 41400000000}`
**Reference:** Answer: 41400000000

### units-04  (computed)
**Q:** Convert 418.25 gwei to wei.

End your reply with a line of the form "Answer: <integer>" (plain decimal, no separators).

**Grader:** `{"type": "bigint", "expect": 418250000000}`
**Reference:** Answer: 418250000000

### units-05  (computed)
**Q:** Convert 6.522 ether to wei.

End your reply with a line of the form "Answer: <integer>" (plain decimal, no separators).

**Grader:** `{"type": "bigint", "expect": 6522000000000000000}`
**Reference:** Answer: 6522000000000000000


## tasks/gen-wallets.jsonl

### wallets-eip55-01  (computed)
**Q:** Convert this Ethereum address to its EIP-55 checksummed form:
0xe653c60ab4b1d30a1efbeb73903ed9423319832e

Answer with only the checksummed address.

**Grader:** `{"type": "exact", "expect": "0xe653C60Ab4b1d30A1EfBeb73903eD9423319832E", "case_sensitive": true}`
**Reference:** 0xe653C60Ab4b1d30A1EfBeb73903eD9423319832E

### wallets-eip55-02  (computed)
**Q:** Convert this Ethereum address to its EIP-55 checksummed form:
0xf90e335b1b9f5bd07293abbc75f66200469a3529

Answer with only the checksummed address.

**Grader:** `{"type": "exact", "expect": "0xF90E335b1B9F5Bd07293aBBc75F66200469A3529", "case_sensitive": true}`
**Reference:** 0xF90E335b1B9F5Bd07293aBBc75F66200469A3529

### wallets-eip55-03  (computed)
**Q:** Convert this Ethereum address to its EIP-55 checksummed form:
0x80d48a6ee577a0ce3c3c4a913b30921fb264cd87

Answer with only the checksummed address.

**Grader:** `{"type": "exact", "expect": "0x80D48a6Ee577A0ce3c3c4A913b30921fb264Cd87", "case_sensitive": true}`
**Reference:** 0x80D48a6Ee577A0ce3c3c4A913b30921fb264Cd87

### wallets-eip55-04  (computed)
**Q:** Convert this Ethereum address to its EIP-55 checksummed form:
0xc180d945aeabdd802d048bb752cd208eacb518ad

Answer with only the checksummed address.

**Grader:** `{"type": "exact", "expect": "0xC180D945aeabDD802D048BB752CD208EacB518Ad", "case_sensitive": true}`
**Reference:** 0xC180D945aeabDD802D048BB752CD208EacB518Ad


## tasks/skill-addresses.jsonl

### addresses-k-01  (fact)
**Q:** What is the canonical Ethereum mainnet contract address of native USDC (Circle's USD Coin)? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"}`
**Reference:** Answer: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
**ethskills quote:** | Mainnet | `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48` | ✅ Verified |

### addresses-k-02  (fact)
**Q:** What is the canonical Ethereum mainnet contract address of WETH (Wrapped Ether)? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"}`
**Reference:** Answer: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
**ethskills quote:** | Mainnet | `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` | ✅ Verified |

### addresses-k-03  (fact)
**Q:** What is the canonical Ethereum mainnet contract address of USDT (Tether)? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0xdAC17F958D2ee523a2206206994597C13D831ec7"}`
**Reference:** Answer: 0xdAC17F958D2ee523a2206206994597C13D831ec7
**ethskills quote:** | Mainnet | `0xdAC17F958D2ee523a2206206994597C13D831ec7` | ✅ Verified |

### addresses-k-04  (fact)
**Q:** What is the canonical Ethereum mainnet address of the Uniswap V2 Router (Router02)? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"}`
**Reference:** Answer: 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D
**ethskills quote:** | Router | `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D` | ✅ Verified |

### addresses-k-05  (fact)
**Q:** Permit2, the universal token-approval contract used by the Uniswap Universal Router, is deployed via CREATE2 at the same address on all EVM chains. What is that address? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0x000000000022D473030F116dDEE9F6B43aC78BA3"}`
**Reference:** Answer: 0x000000000022D473030F116dDEE9F6B43aC78BA3
**ethskills quote:** | All chains | `0x000000000022D473030F116dDEE9F6B43aC78BA3` | ✅ Verified |

### addresses-k-06  (fact)
**Q:** What is the Ethereum mainnet address of the current ENS Registry (the registry contract in use since the 2020 migration)? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e"}`
**Reference:** Answer: 0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e
**ethskills quote:** | Registry | `0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e` | ✅ Verified |

### addresses-k-07  (fact)
**Q:** What is the canonical address of the ERC-4337 EntryPoint v0.6 contract (same CREATE2 address on all EVM chains)? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789"}`
**Reference:** Answer: 0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789
**ethskills quote:** | EntryPoint v0.6 | `0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789` | ✅ Verified |

### addresses-k-08  (fact)
**Q:** Arachnid's deterministic CREATE2 deployer (the proxy used by Foundry and many protocols for deterministic deployments) lives at the same address on every EVM chain. What is that address? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0x4e59b44847b379578588920cA78FbF26c0B4956C"}`
**Reference:** Answer: 0x4e59b44847b379578588920cA78FbF26c0B4956C
**ethskills quote:** | Arachnid's Deployer | `0x4e59b44847b379578588920cA78FbF26c0B4956C` | ✅ Verified |

### addresses-k-09  (fact)
**Q:** What is the Ethereum mainnet address of the Safe (Gnosis Safe) ProxyFactory used with the v1.3.0 singleton to deploy new Safe multisig wallets? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2"}`
**Reference:** Answer: 0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2
**ethskills quote:** | ProxyFactory | `0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2` | ✅ Verified |

### addresses-k-10  (fact)
**Q:** What is the contract address of native USDC (issued by Circle, not the bridged USDbC) on Base? End your reply with a line of the form "Answer: <address>".

**Grader:** `{"type": "exact", "expect": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"}`
**Reference:** Answer: 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
**ethskills quote:** | Base | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` | ✅ Verified |


## tasks/skill-concepts.jsonl

### concepts-k-01  (fact)
**Q:** When referring to activity that happens on the blockchain, the Ethereum community has settled on one preferred spelling of the term. Which is it: "on-chain", "on chain", or "onchain"?
End your reply with a line of the form "Answer: <spelling>".

**Grader:** `{"type": "exact", "expect": "onchain"}`
**Reference:** Answer: onchain
**ethskills quote:** **Terminology:** You say "on-chain." The Ethereum community says **"onchain"** — one word, no hyphen.

### concepts-k-02  (fact)
**Q:** A developer designs an Ethereum contract expecting it to "wake up" every hour and run a function by itself. Why will this never happen?
A) The EVM's built-in scheduler only supports daily intervals
B) Contracts can self-execute, but only during block finalization
C) Contracts cannot execute themselves — every function call needs an external caller who pays gas
D) Only the deployer's node can trigger scheduled execution
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "any_of", "options": [{"type": "exact", "expect": "C"}, {"type": "regex", "pattern": "^\\(?C\\b"}]}`
**Reference:** Answer: C
**ethskills quote:** Smart contracts cannot execute themselves. There is no cron job, no scheduler, no background process. Every function needs a caller who pays gas.

### concepts-k-03  (fact)
**Q:** Inside a Solidity contract, a developer writes `blockhash(block.number)` hoping to get the hash of the current block. What value does this expression always return?
End your reply with a line of the form "Answer: <value>".

**Grader:** `{"type": "any_of", "options": [{"type": "exact", "expect": "zero"}, {"type": "exact", "expect": "0"}, {"type": "bigint", "expect": 0}]}`
**Reference:** Answer: 0
**ethskills quote:** // ❌ blockhash(block.number) is ALWAYS zero for the current block

### concepts-k-04  (fact)
**Q:** A contract derives "randomness" as `uint(keccak256(abi.encodePacked(block.timestamp)))`. Which network participant is in a position to manipulate this value (within a window of roughly 15 seconds) to bias the outcome?
End your reply with a line of the form "Answer: <who>".

**Grader:** `{"type": "regex", "pattern": "validator|miner|proposer|block\\s+producer"}`
**Reference:** Answer: the validator (block proposer) can manipulate block.timestamp
**ethskills quote:** // ❌ Validators can manipulate block.timestamp (within ~15 seconds)

### concepts-k-05  (fact)
**Q:** In a commit-reveal randomness scheme where the random seed mixes the revealed secret with `blockhash(commitBlock)`, the reveal must happen within a limited number of blocks after the commit — wait longer and `blockhash` for the commit block returns zero. Within how many blocks must the reveal happen?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 256}`
**Reference:** Answer: 256
**ethskills quote:** - Must reveal within 256 blocks (blockhash returns zero after that)

### concepts-k-06  (recommendation)
**Q:** You are building an onchain lottery that needs provably unbiased randomness, delivered with a cryptographic proof that anyone can verify onchain. Commit-reveal is deemed too weak for this use case. Which widely-recommended oracle product is the standard choice?
End your reply with a line of the form "Answer: <product>".

**Grader:** `{"type": "regex", "pattern": "chainlink|\\bvrf\\b"}`
**Reference:** Answer: Chainlink VRF
**ethskills quote:** Use commit-reveal for simple cases. Use Chainlink VRF when you need provable randomness (lotteries, NFT reveals, gaming).

### concepts-k-07  (fact)
**Q:** Your smart contract needs a token price, and a teammate suggests reading the spot price directly from a DEX pool's reserves. This is unsafe because a specific kind of attack can fake that price for the duration of a single transaction. Name the attack primitive.
End your reply with a line of the form "Answer: <attack>".

**Grader:** `{"type": "regex", "pattern": "flash[\\s-]*loan"}`
**Reference:** Answer: a flash loan (flash-loan price manipulation)
**ethskills quote:** Use Chainlink — never read prices from a DEX pool, because a flash loan can fake the price for one transaction.

### concepts-k-08  (fact)
**Q:** In Aave/Compound-style overcollateralized lending, anyone may call `liquidate()` on a loan once its health factor drops below a specific numeric threshold. What is that threshold value?
End your reply with a line of the form "Answer: <number>".

**Grader:** `{"type": "numeric", "expect": 1, "tol": 0.001}`
**Reference:** Answer: 1
**ethskills quote:** Loan health factor drops below 1
→ ANYONE can call liquidate()

### concepts-k-09  (fact)
**Q:** The Ethereum community has a specific term for an unstoppable protocol that runs forever with no operator, no company, no server, and no admin key — sustained purely by its own incentives (Uniswap is the canonical example). What is the term?
End your reply with a line of the form "Answer: <term>".

**Grader:** `{"type": "regex", "pattern": "hyper[\\s-]*structure"}`
**Reference:** Answer: a hyperstructure
**ethskills quote:** This is a **hyperstructure** — an unstoppable protocol that runs forever, with no operator, no company, no server, no admin key.

### concepts-k-10  (fact)
**Q:** The Ethereum Foundation uses the shorthand acronym "CROPS" for the set of core properties that make Ethereum Ethereum. Expand the acronym: name the properties it stands for.
End your reply with a line of the form "Answer: <comma-separated properties>".

**Grader:** `{"type": "regex_all", "patterns": ["censorship", "open[\\s-]*source", "privacy", "security"], "on": "full"}`
**Reference:** Answer: Censorship Resistance, Open Source and Free (as in Freedom), Privacy, Security
**ethskills quote:** **CROPS** — Censorship Resistance, Open Source and Free (as in Freedom), Privacy, Security — is the Ethereum Foundation's shorthand for what makes Ethereum Ethereum.


## tasks/skill-frontend.jsonl

### frontend-k-01  (fact)
**Q:** In a dApp frontend using viem, you have an account balance as a bigint in wei and want to display it as a human-readable ETH string (e.g. 1500000000000000000n should display as "1.5"). Which viem utility function do you call?
End your reply with a line of the form "Answer: <function name>".

**Grader:** `{"type": "regex", "pattern": "formatEther"}`
**Reference:** Answer: formatEther
**ethskills quote:** import { formatEther, formatUnits, parseEther, parseUnits } from "viem";

formatEther(weiAmount);

### frontend-k-02  (fact)
**Q:** Using viem's parseUnits to convert the human-readable amount "100" of USDC into token base units (using USDC's standard number of decimals), what integer value do you get?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 100000000}`
**Reference:** Answer: 100000000
**ethskills quote:** parseUnits("100", 6); // USDC-style 6 decimals

### frontend-k-03  (recommendation)
**Q:** A dApp's primary action area shows exactly one button at a time, choosing among: Connect Wallet, Switch Network, Approve, and Stake. The user's wallet is connected but on the wrong chain, and their token allowance is insufficient. Which button should be shown?
A) Approve
B) Switch Network
C) Stake
D) Connect Wallet
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "B"}`
**Reference:** Answer: B
**ethskills quote:** Wrong-network check must happen before approval/action checks

### frontend-k-04  (fact)
**Q:** A developer using wagmi's useWriteContract disables an Approve button only while the hook's isPending is true. Why can a user still double-submit the approval?
A) isPending stays true forever if the transaction reverts
B) isPending becomes false as soon as the wallet returns the transaction hash, before onchain confirmation
C) isPending only tracks read calls, not writes
D) isPending resets only after the allowance query refetches
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "B"}`
**Reference:** Answer: B
**ethskills quote:** `isPending` drops to `false` when the wallet returns the tx hash — before on-chain confirmation. There is a window where `isPending = false` AND the allowance hasn't updated → button re-enables mid-flight and a user can double-submit.

### frontend-k-05  (fact)
**Q:** In a dApp's approval button handler, a submitting flag is set on click and cleared only after the awaited transaction call succeeds — there is no finally block. The user rejects the transaction in their wallet. What happens to the button?
A) It re-enables after a 4 second cooldown
B) It stays disabled permanently
C) It shows a success state
D) It automatically resubmits the approval
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "B"}`
**Reference:** Answer: B
**ethskills quote:** `finally {}` is required — without it a rejected tx locks the button permanently.

### frontend-k-06  (fact)
**Q:** You run a Scaffold-ETH 2 project in fork mode with `yarn fork --network base`. The fork runs locally on Anvil. What chain ID must the frontend's targetNetworks entry in scaffold.config.ts correspond to during development?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 31337}`
**Reference:** Answer: 31337
**ethskills quote:** When using fork mode, the frontend target network MUST be `chains.foundry` (chain ID 31337), NOT the chain you're forking.

### frontend-k-07  (fact)
**Q:** A Next.js app is statically exported (output: "export") and deployed to IPFS. The root route / loads fine, but /debug returns 404 because the build emitted debug.html instead of a directory with an index.html, and IPFS gateways only resolve directories to index.html. Which next.config.ts option (name and value) fixes this?
End your reply with a line of the form "Answer: <option>: <value>".

**Grader:** `{"type": "regex_all", "patterns": ["trailingSlash", "\\btrue\\b"]}`
**Reference:** Answer: trailingSlash: true
**ethskills quote:** `trailingSlash: true` (CRITICAL)** — This is the #1 reason routes break:
- `trailingSlash: false` (default) → generates `debug.html`
- `trailingSlash: true` → generates `debug/index.html`

### frontend-k-08  (fact)
**Q:** On a local Anvil fork, block.timestamp stays frozen between transactions, silently breaking any contract logic that uses timestamps (deadlines, expiry, vesting). Which JSON-RPC method do you call (e.g. via `cast rpc <method> 1`) to make the node mine a block every second?
End your reply with a line of the form "Answer: <rpc method name>".

**Grader:** `{"type": "regex", "pattern": "(anvil|evm)_setIntervalMining"}`
**Reference:** Answer: anvil_setIntervalMining
**ethskills quote:** cast rpc anvil_setIntervalMining 1
```

Without this, `block.timestamp` stays FROZEN. Any contract logic using timestamps (deadlines, expiry, vesting) will break silently.

### frontend-k-09  (fact)
**Q:** Node.js 25+ ships a built-in localStorage object that is missing standard WebStorage methods like getItem/setItem, which crashes next-themes and RainbowKit during Next.js static prerendering. The fix is a localStorage polyfill, but it must be injected via NODE_OPTIONS="--require ./polyfill.cjs" rather than Next.js's instrumentation.ts. Why?
A) instrumentation.ts only runs in production mode, not during builds
B) Next.js prerenders pages in a separate build worker process where instrumentation.ts never runs, while --require injects into every Node process including workers
C) --require is needed to transpile the TypeScript polyfill
D) instrumentation.ts runs after pages have already been rendered
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "B"}`
**Reference:** Answer: B
**ethskills quote:** Next.js spawns a separate build worker process for prerendering. `--require` injects into EVERY Node process (including workers). `next.config.ts` polyfill only runs in the main process. `instrumentation.ts` doesn't run in the build worker. Only `--require` works.

### frontend-k-10  (recommendation)
**Q:** Following Scaffold-ETH 2 conventions, what single command do you run to scaffold a brand-new dApp project (Foundry, Next.js, RainbowKit, and the scaffold hooks all pre-wired), instead of running forge init or creating a Next.js project from scratch?
End your reply with a line of the form "Answer: <command>".

**Grader:** `{"type": "regex", "pattern": "create-eth"}`
**Reference:** Answer: npx create-eth@latest
**ethskills quote:** `npx create-eth@latest` handles everything — Foundry, Next.js, RainbowKit, scaffold hooks. Never run `forge init` or create Next.js projects from scratch.


## tasks/skill-fundamentals.jsonl

### fundamentals-k-01  (recommendation)
**Q:** When writing about activity that happens on an Ethereum blockchain (as opposed to off it), which spelling does the Ethereum community prefer: "on-chain", "onchain", or "on chain"?
End your reply with a line of the form "Answer: <spelling>".

**Grader:** `{"type": "regex", "pattern": "\\bonchain\\b"}`
**Reference:** Answer: onchain
**ethskills quote:** You say "on-chain." The Ethereum community says **"onchain"** — one word, no hyphen. Use "onchain" in all writing.

### fundamentals-k-02  (fact)
**Q:** What is Ethereum mainnet's target block time, in seconds?
End your reply with a line of the form "Answer: <number>".

**Grader:** `{"type": "bigint", "expect": 12}`
**Reference:** Answer: 12
**ethskills quote:** **Block time:** 12 seconds

### fundamentals-k-03  (fact)
**Q:** An autonomous AI agent runs a paid service as a smart contract on Ethereum. The startup that originally deployed the contract later shuts down. According to the standard argument for building agent services on a permissionless blockchain like Ethereum, what happens to the service?
A) It halts until governance appoints a new operator
B) It keeps running indefinitely, because it never depended on any company's cooperation
C) Validators automatically pause it after a period of inactivity
D) It switches to read-only mode
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "any_of", "options": [{"type": "exact", "expect": "B"}, {"type": "regex", "pattern": "^b\\b"}]}`
**Reference:** Answer: B
**ethskills quote:** No API keys to revoke, no accounts to ban, no services to shut down. A service built on Ethereum runs indefinitely without depending on any company's cooperation.

### fundamentals-k-04  (fact)
**Q:** As of early 2026, what is the typical base fee on Ethereum mainnet?
A) Above 30 gwei
B) 10-30 gwei
C) 1-10 gwei
D) Under 1 gwei
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "any_of", "options": [{"type": "exact", "expect": "D"}, {"type": "regex", "pattern": "^d\\b|under\\s*1\\s*gwei"}]}`
**Reference:** Answer: D
**ethskills quote:** **Mainnet base fee:** Under 1 gwei (typically 0.1-0.5, varies daily)

### fundamentals-k-05  (fact)
**Q:** Ethereum's Pectra upgrade (May 2025) let externally owned accounts temporarily act as smart accounts ("smart EOAs"). Which EIP introduced this capability?
End your reply with a line of the form "Answer: EIP-<number>".

**Grader:** `{"type": "regex", "pattern": "\\b7702\\b"}`
**Reference:** Answer: EIP-7702
**ethskills quote:** **Pectra (May 7, 2025):** EIP-7702 smart EOAs, 2x blob capacity, BLS precompiles

### fundamentals-k-06  (fact)
**Q:** Which ERC standard defines an onchain identity and reputation registry for AI agents, and was deployed to Ethereum mainnet in January 2026?
End your reply with a line of the form "Answer: ERC-<number>".

**Grader:** `{"type": "regex", "pattern": "\\b8004\\b"}`
**Reference:** Answer: ERC-8004
**ethskills quote:** **ERC-8004** — onchain agent identity registry (deployed Jan 29, 2026)

### fundamentals-k-07  (fact)
**Q:** In the x402 machine-to-machine payment flow, an agent calling an API receives an HTTP 402 "Payment Required" response, signs a payment authorization, and retries the request with a payment header. Which EIP standard is that payment signature based on?
End your reply with a line of the form "Answer: EIP-<number>".

**Grader:** `{"type": "regex", "pattern": "\\b3009\\b"}`
**Reference:** Answer: EIP-3009
**ethskills quote:** Agent calls API → gets 402 → signs EIP-3009 payment → retries with payment header → gets response.

### fundamentals-k-08  (fact)
**Q:** Ethereum's Fusaka upgrade (December 2025) shipped PeerDAS. Under PeerDAS, what fraction of the blob data does each node sample/download instead of downloading all of it?
End your reply with a line of the form "Answer: <fraction>".

**Grader:** `{"type": "regex", "pattern": "\\b1\\s*/\\s*8\\b|one[\\s-]?eighth|\\b12\\.5\\s*%"}`
**Reference:** Answer: 1/8
**ethskills quote:** **Fusaka (Dec 3, 2025):** PeerDAS (nodes sample 1/8 of data), 2x gas limit (30M→60M)

### fundamentals-k-09  (fact)
**Q:** Ethereum's Glamsterdam upgrade (planned for mid-2026) includes a feature abbreviated "ePBS". What does ePBS stand for, and which EIP specifies it?
End your reply with a line of the form "Answer: <expansion>, EIP-<number>".

**Grader:** `{"type": "regex_all", "patterns": ["proposer[\\s-]?builder\\s+separation", "\\b7732\\b"]}`
**Reference:** Answer: Enshrined Proposer-Builder Separation, EIP-7732
**ethskills quote:** ePBS — Enshrined Proposer-Builder Separation (EIP-7732)

### fundamentals-k-10  (fact)
**Q:** Verkle trees were long expected to replace Ethereum's state trie, but roadmap plans shifted toward a binary state tree (EIP-7864) instead. What cryptographic concern about Verkle trees, identified in mid-2024, was the primary driver of this shift?
End your reply with a line of the form "Answer: <concern>".

**Grader:** `{"type": "regex", "pattern": "quantum"}`
**Reference:** Answer: Verkle tree cryptography is potentially quantum-vulnerable (the replacement is driven by quantum resistance)
**ethskills quote:** the primary driver is quantum resistance, and it also improves ZK-proof efficiency 3-100x. Verkle tree cryptography was identified as potentially quantum-vulnerable in mid-2024.


## tasks/skill-gas.jsonl

### gas-k-01  (fact)
**Q:** How much gas does a simple ETH value transfer (plain send to an EOA, empty calldata) consume on Ethereum?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 21000}`
**Reference:** Answer: 21000
**ethskills quote:** | ETH transfer | 21,000 | **$0.004** | $0.04 | $0.42 |

### gas-k-02  (fact)
**Q:** Which EIP introduced blob-carrying transactions to Ethereum, letting rollups post their data as blobs?
End your reply with a line of the form "Answer: EIP-<number>".

**Grader:** `{"type": "regex", "pattern": "\\b4844\\b"}`
**Reference:** Answer: EIP-4844
**ethskills quote:** **EIP-4844 (Dencun, March 2024):** Blob transactions — L2s post data as blobs instead of calldata, 100x cheaper.

### gas-k-03  (fact)
**Q:** The Ethereum network upgrade of March 2024 that activated blob transactions (EIP-4844) is commonly known by what name?
End your reply with a line of the form "Answer: <upgrade name>".

**Grader:** `{"type": "regex", "pattern": "dencun|cancun"}`
**Reference:** Answer: Dencun
**ethskills quote:** **EIP-4844 (Dencun, March 2024):** Blob transactions — L2s post data as blobs instead of calldata, 100x cheaper.

### gas-k-04  (fact)
**Q:** After EIP-4844, rollups post their batch data to Ethereum as blobs. Before that, which part of a regular transaction did rollups use to post that data (roughly 100x more expensive)?
End your reply with a line of the form "Answer: <term>".

**Grader:** `{"type": "regex", "pattern": "call\\s?-?data"}`
**Reference:** Answer: calldata
**ethskills quote:** **EIP-4844 (Dencun, March 2024):** Blob transactions — L2s post data as blobs instead of calldata, 100x cheaper.

### gas-k-05  (fact)
**Q:** The Pectra upgrade (May 2025) changed Ethereum's target blob count per block from 3 to what number?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 6}`
**Reference:** Answer: 6
**ethskills quote:** **Pectra (May 2025):** Doubled blob capacity (3→6 target blobs).

### gas-k-06  (fact)
**Q:** The Fusaka upgrade (December 2025) raised Ethereum mainnet's block gas limit from 30 million to what value? Answer in millions of gas.
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 60}`
**Reference:** Answer: 60
**ethskills quote:** **Fusaka (Dec 2025):** PeerDAS (nodes sample 1/8 of data) + 2x gas limit (30M→60M).

### gas-k-07  (fact)
**Q:** Under PeerDAS (shipped in Ethereum's Fusaka upgrade), each node samples what fraction of blob data instead of downloading all of it?
End your reply with a line of the form "Answer: <fraction>".

**Grader:** `{"type": "regex", "pattern": "1\\s*/\\s*8|one[\\s-]?eighth|12\\.5\\s*%"}`
**Reference:** Answer: 1/8
**ethskills quote:** **Fusaka (Dec 2025):** PeerDAS (nodes sample 1/8 of data) + 2x gas limit (30M→60M).

### gas-k-08  (fact)
**Q:** The total fee a user pays for a transaction on an optimistic or ZK rollup is made up of which two cost components?
A) L2 execution gas plus L1 data gas (data availability)
B) Priority tip plus MEV auction fee
C) Sequencer subscription plus validator staking fee
D) Storage rent plus compute credits
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "A"}`
**Reference:** Answer: A
**ethskills quote:** L2 transactions have two cost components:
1. **L2 execution gas** — paying the sequencer
2. **L1 data gas** — paying Ethereum for data availability (blobs post-4844)

### gas-k-09  (fact)
**Q:** Roughly how much gas does a standard ERC-20 token transfer use on Ethereum?
A) ~21,000
B) ~65,000
C) ~250,000
D) ~650,000
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "B"}`
**Reference:** Answer: B
**ethskills quote:** | ERC-20 transfer | ~65,000 | **$0.013** | $0.13 | $1.30 |

### gas-k-10  (recommendation)
**Q:** You're starting a new Ethereum project (a DeFi protocol composing with existing liquidity) and have no concrete reason to pick any particular chain. Given 2026 gas economics, does current ecosystem guidance say to default to Ethereum mainnet or to an L2?
End your reply with a line of the form "Answer: <mainnet or L2>".

**Grader:** `{"type": "regex", "pattern": "mainnet|\\bL1\\b|layer\\s?-?\\s?(1|one)"}`
**Reference:** Answer: mainnet
**ethskills quote:** **Use mainnet when:** DeFi, governance, identity, high-value transfers, composing with mainnet liquidity, or when you don't have a concrete reason for an L2. Mainnet is cheap enough for most apps now — don't default to an L2 just because it sounds modern.


## tasks/skill-indexing.jsonl

### indexing-k-01  (fact)
**Q:** How many `indexed` parameters (topics, excluding the event signature topic0) can a standard non-anonymous Solidity event declare at most?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 3}`
**Reference:** Answer: 3
**ethskills quote:** You get 3 indexed topics per event.

### indexing-k-02  (fact)
**Q:** Where does Ethereum store the event logs a contract emits?
A) In the contract's storage slots
B) In transaction receipts
C) In the transaction's calldata
D) In the block header only
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "any_of", "options": [{"type": "regex", "pattern": "\\bB\\b"}, {"type": "regex", "pattern": "receipt"}]}`
**Reference:** Answer: B
**ethskills quote:** They're stored in transaction receipts, not in contract storage, so they don't cost storage gas.

### indexing-k-03  (fact)
**Q:** You need to read a contract's state as it was at a block from three years ago via JSON-RPC (an `eth_call` against an old block tag). What special kind of Ethereum node does this require?
End your reply with a line of the form "Answer: <node type>".

**Grader:** `{"type": "regex", "pattern": "archive"}`
**Reference:** Answer: an archive node
**ethskills quote:** Reading state at a historical block requires an archive node (expensive, slow).

### indexing-k-04  (fact)
**Q:** The Multicall3 contract is deployed at the same address on Ethereum, Arbitrum, Optimism, Base, Polygon, and 50+ other chains. What is that address?
End your reply with a line of the form "Answer: <0x-prefixed address>".

**Grader:** `{"type": "exact", "expect": "0xcA11bde05977b3631167028862bE2a173976CA11"}`
**Reference:** Answer: 0xcA11bde05977b3631167028862bE2a173976CA11
**ethskills quote:** // Multicall3: 0xcA11bde05977b3631167028862bE2a173976CA11
// Same address on Ethereum, Arbitrum, Optimism, Base, Polygon, and 50+ chains

### indexing-k-05  (fact)
**Q:** When you deploy a subgraph to The Graph, your contract's events become queryable through an API. What query language does that API use?
End your reply with a line of the form "Answer: <query language>".

**Grader:** `{"type": "regex", "pattern": "graph\\s?-?\\s?ql"}`
**Reference:** Answer: GraphQL
**ethskills quote:** The Graph turns your contract's events into a queryable GraphQL API.

### indexing-k-06  (fact)
**Q:** Using The Graph's `graph` CLI while building a subgraph, which command generates the typed classes for your entities and events from the schema and contract ABIs?
End your reply with a line of the form "Answer: <command>".

**Grader:** `{"type": "regex", "pattern": "codegen"}`
**Reference:** Answer: graph codegen
**ethskills quote:** # Generate types from schema
graph codegen

### indexing-k-07  (fact)
**Q:** In a subgraph's schema.graphql, which directive do you attach to an entity field to declare it as a reverse lookup — populated from a field on another entity rather than stored directly?
End your reply with a line of the form "Answer: <directive>".

**Grader:** `{"type": "regex", "pattern": "derived.?from"}`
**Reference:** Answer: @derivedFrom
**ethskills quote:** transfers: [Transfer!]! @derivedFrom(field: "token")

### indexing-k-08  (fact)
**Q:** Under EVM LOG opcode pricing, how many gas does each byte of an event's non-indexed data payload cost to emit?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 8}`
**Reference:** Answer: 8
**ethskills quote:** Solidity events are cheap to emit (~375 gas base + 375 per indexed topic + 8 gas per byte of data) and free to read offchain.

### indexing-k-09  (recommendation)
**Q:** You're deciding whether to fetch a contract's full event history directly with `eth_getLogs` or to stand up an indexer (e.g. a subgraph). Per common ecosystem guidance, beyond roughly what block-range size does direct log scanning break down, meaning you should reach for an indexer instead?
A) ~100 blocks
B) ~10,000 blocks
C) ~10,000,000 blocks
D) There is no practical limit
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "any_of", "options": [{"type": "regex", "pattern": "\\bB\\b"}, {"type": "regex", "pattern": "\\b10\\s?k\\b"}]}`
**Reference:** Answer: B
**ethskills quote:** Any query that would require scanning more than ~10K blocks

### indexing-k-10  (recommendation)
**Q:** Several event-indexing tools exist in the Ethereum ecosystem. Which open-source indexing framework is characterized as TypeScript-first and local-first — a simpler alternative to The Graph when the index only needs to serve a single app?
End your reply with a line of the form "Answer: <tool name>".

**Grader:** `{"type": "regex", "pattern": "\\bponder\\b"}`
**Reference:** Answer: Ponder
**ethskills quote:** | **Ponder** | TypeScript-first indexing | Local-first, simpler than The Graph for single-app use |


## tasks/skill-l2s.jsonl

### l2s-k-01  (fact)
**Q:** What is the chain ID of Base, Coinbase's Ethereum L2 mainnet? 
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "bigint", "expect": 8453}`
**Reference:** Answer: 8453
**ethskills quote:** | **Base** | Optimistic (OP Stack) | $0.0008-0.002 | 2s | 7 days | 8453 |

### l2s-k-02  (recommendation)
**Q:** Your users must be able to withdraw funds to Ethereum L1 through the rollup's canonical (official) bridge within about an hour or two, not after a multi-day wait. Which family of rollups should you choose: optimistic rollups or ZK rollups? 
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "\\bzk\\b|zero.?knowledge|validity"}`
**Reference:** Answer: ZK rollups
**ethskills quote:** | No 7-day withdrawal wait | **ZK rollup** (zkSync, Scroll, Linea) | 15-120 min finality |

### l2s-k-03  (fact)
**Q:** You want to deploy the same contract to the same address on several EVM chains. Which opcode/deployment mechanism makes the address deterministic, so that the same salt + same bytecode + same deployer yields the same address on every chain? 
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "create\\s*-?2"}`
**Reference:** Answer: CREATE2
**ethskills quote:** Use CREATE2 for deterministic addresses across chains: ... # Same salt + same bytecode + same deployer = same address on every chain

### l2s-k-04  (fact)
**Q:** To compile and deploy Solidity contracts on zkSync Era, you cannot use the standard solc toolchain output directly. What is the name of the compiler you must use instead? 
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "zksolc"}`
**Reference:** Answer: zksolc
**ethskills quote:** **zkSync Era:** Must use `zksolc` compiler. No `EXTCODECOPY` (compile-time error).

### l2s-k-05  (fact)
**Q:** In a Solidity contract running on Arbitrum One, you read `block.number`. Whose block number does it return? 
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "\\bl1\\b|layer\\s*-?1|ethereum|mainnet"}`
**Reference:** Answer: The L1 (Ethereum mainnet) block number, not Arbitrum's own
**ethskills quote:** Arbitrum's `block.number` returns L1 block number, not L2.

### l2s-k-06  (fact)
**Q:** Which best describes Celo's architecture after its March 2025 migration? (A) An independent proof-of-stake L1, (B) An OP Stack L2 on Ethereum, (C) A Cosmos SDK appchain, (D) A Polygon CDK validium. 
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "B"}`
**Reference:** Answer: B
**ethskills quote:** **Now:** OP Stack L2 on Ethereum — **migrated March 26, 2025** (block 31056500)

### l2s-k-07  (fact)
**Q:** Unichain, Uniswap's L2, uses TEE-based block building with a private encrypted mempool. Within a block, by what criterion does it order transactions instead of gas price? 
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "time|arrival|first.?come|fcfs"}`
**Reference:** Answer: By time received (first-come-first-served), not by gas price
**ethskills quote:** Transactions ordered by **time received, NOT gas price**

### l2s-k-08  (fact)
**Q:** One major Ethereum L2 lets you write smart contracts in Rust, C, or C++, compiled to WASM and running alongside the EVM with shared state, giving large gas savings for compute-heavy work. Name the L2 and the feature. 
End your reply with a line of the form "Answer: <chain>, <feature name>".

**Grader:** `{"type": "regex_all", "patterns": ["arbitrum", "stylus"]}`
**Reference:** Answer: Arbitrum, Stylus
**ethskills quote:** **Stylus:** Write smart contracts in Rust, C, C++ (compiles to WASM, runs alongside EVM, shares state). Use for compute-heavy operations (10-100x gas savings).

### l2s-k-09  (fact)
**Q:** Superchain (OP Stack) member chains contribute a share of their sequencer revenue to the Optimism Collective. What percentage? 
End your reply with a line of the form "Answer: <number>%".

**Grader:** `{"type": "any_of", "options": [{"type": "bigint", "expect": 15}, {"type": "regex", "pattern": "\\b15\\s*(%|percent)"}]}`
**Reference:** Answer: 15%
**ethskills quote:** Members contribute **15% of sequencer revenue** to the Optimism Collective.

### l2s-k-10  (fact)
**Q:** On zkSync Era, the deepest liquidity for most pairs is not on Uniswap but on the chain's largest native DEX, a classic AMM. What is it called? 
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "syncswap"}`
**Reference:** Answer: SyncSwap
**ethskills quote:** | zkSync | SyncSwap | Classic AMM | Largest native DEX on zkSync |


## tasks/skill-protocol.jsonl

### protocol-k-01  (fact)
**Q:** Which EIP introduced blob-carrying transactions (proto-danksharding) to Ethereum, shipping in the Dencun hard fork? 
End your reply with a line of the form "Answer: <EIP number>".

**Grader:** `{"type": "bigint", "expect": 4844}`
**Reference:** Answer: 4844
**ethskills quote:** | Dencun | Mar 13, 2024 | EIP-4844 blobs (proto-danksharding) |

### protocol-k-02  (fact)
**Q:** Which Ethereum hard fork (April 2023) enabled staking withdrawals via EIP-4895? 
End your reply with a line of the form "Answer: <fork name>".

**Grader:** `{"type": "regex", "pattern": "shapella|shanghai|capella"}`
**Reference:** Answer: Shapella
**ethskills quote:** | Shapella | Apr 12, 2023 | Staking withdrawals (EIP-4895) |

### protocol-k-03  (fact)
**Q:** EIP-7702, which lets EOAs temporarily act as smart-contract accounts, went live on Ethereum mainnet in which hard fork? 
End your reply with a line of the form "Answer: <fork name>".

**Grader:** `{"type": "regex", "pattern": "pectra|prague"}`
**Reference:** Answer: Pectra
**ethskills quote:** | Pectra | May 7, 2025 | EIP-7702 (smart EOAs), validator consolidation (EIP-7251) |

### protocol-k-04  (fact)
**Q:** In the ethereum/EIPs repository, what status label marks an EIP that has had no activity for 6+ months and is probably dead or deprioritized? 
End your reply with a line of the form "Answer: <status>".

**Grader:** `{"type": "regex", "pattern": "stagnant"}`
**Reference:** Answer: Stagnant
**ethskills quote:** `Stagnant` = no activity for 6+ months, probably dead or deprioritized

### protocol-k-05  (fact)
**Q:** The hard-fork inclusion stages used by Ethereum core devs — CFI (Considered for Inclusion), SFI (Scheduled for Inclusion), and DFI (Declined for Inclusion) — are formally defined in which EIP? 
End your reply with a line of the form "Answer: <EIP number>".

**Grader:** `{"type": "bigint", "expect": 7723}`
**Reference:** Answer: 7723
**ethskills quote:** **CFI (Considered for Inclusion)**: Core devs are seriously evaluating it for a specific fork. Implementation work begins. Defined in EIP-7723

### protocol-k-06  (fact)
**Q:** Each Ethereum hard fork has a meta-EIP listing its scope. Which meta-EIP defines the scope of the Pectra hard fork? 
End your reply with a line of the form "Answer: <EIP number>".

**Grader:** `{"type": "bigint", "expect": 7600}`
**Reference:** Answer: 7600
**ethskills quote:** 2. Or check the fork's meta-EIP (e.g., EIP-7600 for Pectra)

### protocol-k-07  (fact)
**Q:** For years Verkle trees were Ethereum's leading candidate for enabling statelessness, but in 2024-2025 concerns about ZK-compatibility and quantum resistance shifted core-dev focus to a different state tree structure. Which one? 
End your reply with a line of the form "Answer: <tree structure>".

**Grader:** `{"type": "regex", "pattern": "binary"}`
**Reference:** Answer: binary trees
**ethskills quote:** Verkle was the leading statelessness candidate for years — then in 2024-2025, concerns about ZK-compatibility and quantum resistance shifted focus to binary trees instead.

### protocol-k-08  (fact)
**Q:** PeerDAS (peer data availability sampling), the headline change of Ethereum's Fusaka hard fork, is specified in which EIP? 
End your reply with a line of the form "Answer: <EIP number>".

**Grader:** `{"type": "bigint", "expect": 7594}`
**Reference:** Answer: 7594
**ethskills quote:** | Fusaka | Dec 3, 2025 | PeerDAS (EIP-7594), more blobs (EIP-7892) |

### protocol-k-09  (fact)
**Q:** Enshrined proposer-builder separation (ePBS), slated for consideration in the Glamsterdam hard fork, is specified in which EIP? 
End your reply with a line of the form "Answer: <EIP number>".

**Grader:** `{"type": "bigint", "expect": 7732}`
**Reference:** Answer: 7732
**ethskills quote:** | Glamsterdam | ~Q3-Q4 2026 (in progress) | ePBS (EIP-7732), block access lists (EIP-7928) |

### protocol-k-10  (recommendation)
**Q:** You need to check whether an Ethereum feature is actually scheduled for an upcoming hard fork. One website is the recommended first stop: it tracks EIP inclusion status (CFI/SFI/DFI) per fork, devnet implementation matrices, and summaries of every All Core Devs call. Which site is it? 
End your reply with a line of the form "Answer: <domain>".

**Grader:** `{"type": "regex", "pattern": "forkcast"}`
**Reference:** Answer: forkcast.org
**ethskills quote:** 1. **[forkcast.org](https://forkcast.org)** — The best single resource for protocol status.


## tasks/skill-security.jsonl

### security-k-01  (fact)
**Q:** A Solidity withdraw function reads the caller's balance, sends that amount of ETH to the caller via a low-level call, and only after the call returns does it set the caller's balance to zero. An attacker's contract uses its receive function to call withdraw again before the first invocation finishes, draining the contract. What is the name of this vulnerability class?
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "re-?(entranc|entry)"}`
**Reference:** Answer: reentrancy
**ethskills quote:** An external call can call back into your contract before the first call finishes. If you update state AFTER the external call, the attacker re-enters with stale state.

### security-k-02  (fact)
**Q:** How many decimals does the USDC token contract use?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 6}`
**Reference:** Answer: 6
**ethskills quote:** **USDC has 6 decimals, not 18.** This is the #1 source of "where did my money go?" bugs.

### security-k-03  (fact)
**Q:** You submit a swap of 10 ETH for USDC on Uniswap through the public mempool with a 1% slippage tolerance. A bot sees your pending transaction, buys USDC immediately before yours executes (pushing the price up), lets your swap fill at the worse price, then sells immediately after your transaction, pocketing the difference. What is this specific MEV attack called?
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "sandwich"}`
**Reference:** Answer: a sandwich attack
**ethskills quote:** 3. Attacker frontruns: buys USDC before you → price rises
4. Your swap executes at a worse price (but within your 1% slippage)
5. Attacker backruns: sells USDC after you → profits from the price difference

### security-k-04  (fact)
**Q:** A Solidity function body is ordered so that it first validates inputs and conditions, then updates all contract state, and only performs external calls last. What is the standard name of this defensive coding pattern?
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "checks?[\\s_-]*effects?[\\s_-]*interactions?|\\bCEI\\b"}`
**Reference:** Answer: Checks-Effects-Interactions (CEI)
**ethskills quote:** **The pattern: Checks → Effects → Interactions (CEI)**
1. **Checks** — validate inputs and conditions
2. **Effects** — update all state
3. **Interactions** — external calls last

### security-k-05  (fact)
**Q:** A brand-new ERC-4626-style vault has no deposits yet. An attacker deposits 1 wei of the underlying token and receives 1 share, then transfers 1000 tokens directly to the vault's address without calling deposit. A victim then deposits 1999 tokens and, because share math rounds down, receives 0 shares; the attacker redeems their single share for all 3000 tokens. What is this attack commonly called?
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "inflation|donation|first[\\s_-]?deposit"}`
**Reference:** Answer: the vault inflation attack (first-depositor share price manipulation)
**ethskills quote:** The first depositor in an ERC-4626 vault can manipulate the share price to steal from subsequent depositors.

### security-k-06  (recommendation)
**Q:** A lending protocol needs an onchain ETH/USD price to value collateral. Computing it from a Uniswap pair's current reserves is dangerous because a flash loan can skew the spot price within a single transaction. For a high-value decision like this, which oracle provider is the standard recommendation?
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "chainlink|\\btwap\\b|time[\\s_-]?weighted"}`
**Reference:** Answer: Chainlink
**ethskills quote:** A flash loan can manipulate any pool's spot price within a single transaction. This has caused hundreds of millions in losses.

// ✅ SAFE — Chainlink with staleness + sanity checks

### security-k-07  (fact)
**Q:** A deployed contract that holds user funds exposes a function `emergencyWithdraw()` marked `external` with no modifiers; its body transfers the contract's entire token balance to `msg.sender`. Anyone who calls it receives all the funds. What vulnerability class is this?
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "access[\\s_-]?control|unprotected|unrestricted|unauthoriz"}`
**Reference:** Answer: missing access control (unprotected privileged function)
**ethskills quote:** Every state-changing function needs explicit access control. "Who should be able to call this?" is the first question.

// ❌ WRONG — anyone can drain the contract

### security-k-08  (fact)
**Q:** A contract behind an upgradeable proxy declared, in V1, exactly two storage variables in this order: `uint256 a; uint256 b;`. You are writing V2 and need to add a new variable `uint256 c`. Which V2 storage layout is safe?
A) uint256 c; uint256 a; uint256 b;
B) uint256 a; uint256 c; uint256 b;
C) uint256 a; uint256 b; uint256 c;
D) Any order is safe because variable names are preserved across upgrades
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "C"}`
**Reference:** Answer: C
**ethskills quote:** **Never change storage layout** — only append new variables at the end, never delete or reorder

### security-k-09  (fact)
**Q:** You are writing an upgradeable implementation contract that inherits OpenZeppelin's UUPSUpgradeable. There is one internal function you must override (typically restricted with an owner check) to control who may perform upgrades — getting it wrong can leave the contract locked. Name that function.
End your reply with a line of the form "Answer: <function name>".

**Grader:** `{"type": "regex", "pattern": "authorize[\\s_]?upgrade"}`
**Reference:** Answer: _authorizeUpgrade
**ethskills quote:** | Risk | Forgetting `_authorizeUpgrade` locks the contract | More gas overhead |

### security-k-10  (fact)
**Q:** A protocol verifies user signatures over typed structured data per EIP-712. Which component of the signed digest is specifically responsible for preventing a valid signature from being replayed against a different contract or on a different chain?
End your reply with a line of the form "Answer: <short answer>".

**Grader:** `{"type": "regex", "pattern": "domain[\\s_-]?separator"}`
**Reference:** Answer: the domain separator
**ethskills quote:** **Domain separator** prevents replaying signatures on different contracts or chains


## tasks/skill-standards.jsonl

### standards-k-01  (fact)
**Q:** A DeFi protocol wants its yield-bearing vault to expose a standardized share-accounting interface (deposit/mint/withdraw/redeem, convertToShares/convertToAssets) so aggregators can integrate any vault the same way. Which ERC number is the standard for tokenized vaults?
End your reply with a line of the form "Answer: <ERC number>".

**Grader:** `{"type": "regex", "pattern": "\\b4626\\b"}`
**Reference:** Answer: ERC-4626
**ethskills quote:** | ERC-4626 | Tokenized vaults | ✅ Standard for yield |

### standards-k-02  (fact)
**Q:** Which ERC number standardizes the `permit` function, letting an ERC-20 holder grant a spender an allowance with an off-chain signature instead of an on-chain `approve` transaction (gasless approvals)?
End your reply with a line of the form "Answer: <ERC number>".

**Grader:** `{"type": "regex", "pattern": "\\b2612\\b"}`
**Reference:** Answer: ERC-2612
**ethskills quote:** | ERC-2612 | Gasless approvals (Permit) | ✅ Widely adopted |

### standards-k-03  (fact)
**Q:** Which ERC number defines token-bound accounts — giving every NFT its own smart contract wallet that can hold assets and act onchain?
End your reply with a line of the form "Answer: <ERC number>".

**Grader:** `{"type": "regex", "pattern": "\\b6551\\b"}`
**Reference:** Answer: ERC-6551
**ethskills quote:** | ERC-6551 | Token-bound accounts (NFT wallets) | ✅ Niche adoption |

### standards-k-04  (fact)
**Q:** EIP-3009 lets a token holder sign an off-chain authorization that a third party can submit onchain to move the holder's tokens (USDC implements it, and the x402 payment protocol relies on it for settlement). What is the exact name of the token function the settling party calls?
End your reply with a line of the form "Answer: <functionName>".

**Grader:** `{"type": "regex", "pattern": "transfer\\s*with\\s*authorization"}`
**Reference:** Answer: transferWithAuthorization
**ethskills quote:** The x402 server calls `transferWithAuthorization` to settle payments on behalf of the client.

### standards-k-05  (fact)
**Q:** The x402 payment protocol is named after the HTTP status code a server returns when a resource requires payment. What is the standard reason phrase (the text name) of that HTTP status code?
End your reply with a line of the form "Answer: <reason phrase>".

**Grader:** `{"type": "regex", "pattern": "payment\\s*required"}`
**Reference:** Answer: Payment Required
**ethskills quote:** Uses the HTTP 402 "Payment Required" status code for internet-native payments.

### standards-k-06  (fact)
**Q:** EIP-7702, which lets an EOA authorize delegation to smart-contract code without migrating to a new account, went live on Ethereum mainnet in May 2025 as part of which network upgrade (hard fork)?
End your reply with a line of the form "Answer: <upgrade name>".

**Grader:** `{"type": "regex", "pattern": "pectra"}`
**Reference:** Answer: Pectra
**ethskills quote:** **EIP-7702 is live.** Shipped with Pectra (May 7, 2025).

### standards-k-07  (fact)
**Q:** Under EIP-7702, an EOA signs an authorization that sets a delegation designator pointing its code at a contract. Per the spec, how long does that delegation remain in effect?
A) It applies to a single transaction only, then clears automatically
B) It expires at the end of the block
C) It remains until replaced or cleared by a later authorization
D) It expires after a protocol-defined timeout
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "any_of", "options": [{"type": "exact", "expect": "C"}, {"type": "regex", "pattern": "answer:\\s*C\\b", "on": "full"}]}`
**Reference:** Answer: C
**ethskills quote:** **Important nuance:** Delegation is not automatically "single transaction only" by spec. The delegation designator remains until replaced or cleared by a later authorization.

### standards-k-08  (fact)
**Q:** ERC-8004 (the onchain agent identity registry deployed in January 2026) builds its Identity Registry on top of a pre-existing token standard, so each registered agent is a token with a unique tokenId. Which ERC token standard is it based on?
End your reply with a line of the form "Answer: <ERC number>".

**Grader:** `{"type": "regex", "pattern": "\\b721\\b"}`
**Reference:** Answer: ERC-721
**ethskills quote:** **1. Identity Registry (ERC-721 based)**
- Globally unique onchain identities for AI agents
- Each agent is an NFT with unique identifier

### standards-k-09  (fact)
**Q:** The x402 HTTP payment protocol defines payment schemes. `exact` covers fixed known-upfront prices. What is the name of the scheme for metered services (e.g. per-token LLM inference), where the client authorizes a maximum amount and the server settles only what was actually consumed?
End your reply with a line of the form "Answer: <scheme name>".

**Grader:** `{"type": "any_of", "options": [{"type": "exact", "expect": "upto"}, {"type": "regex", "pattern": "\\bup[- ]?to\\b"}]}`
**Reference:** Answer: upto
**ethskills quote:** **`upto`** (emerging) — Pay up to a maximum, final amount determined after work completes. Critical for metered services

### standards-k-10  (fact)
**Q:** ERC-8004 specifies a three-registry system for autonomous agents to trust and transact with each other. Name all three registries.
End your reply with a line of the form "Answer: <registry1>, <registry2>, <registry3>".

**Grader:** `{"type": "regex_all", "patterns": ["identit", "reputation", "validation"]}`
**Reference:** Answer: Identity Registry, Reputation Registry, Validation Registry
**ethskills quote:** ### Three Registry System

**1. Identity Registry (ERC-721 based)** … **2. Reputation Registry** … **3. Validation Registry**


## tasks/skill-testing.jsonl

### testing-k-01  (fact)
**Q:** In a Foundry (forge-std) Solidity test, which cheatcode sets msg.sender to a given address for only the next external call?
End your reply with a line of the form "Answer: <cheatcode name>".

**Grader:** `{"type": "regex", "pattern": "\\bprank\\b"}`
**Reference:** Answer: vm.prank
**ethskills quote:** vm.prank(alice);
        token.transfer(bob, 1_000e18);

### testing-k-02  (fact)
**Q:** In a Foundry test you need a fresh test address to hold 1 ether of native ETH before it sends a transaction. Which cheatcode sets an address's ETH balance?
End your reply with a line of the form "Answer: <cheatcode name>".

**Grader:** `{"type": "regex", "pattern": "\\bdeal\\b"}`
**Reference:** Answer: vm.deal
**ethskills quote:** address user = makeAddr("user");
        vm.deal(user, 1 ether);

### testing-k-03  (fact)
**Q:** In a Foundry test, which cheatcode do you call immediately before an external call to assert that the call reverts (optionally matching a specific revert reason)?
End your reply with a line of the form "Answer: <cheatcode name>".

**Grader:** `{"type": "regex", "pattern": "expect\\s?_?revert"}`
**Reference:** Answer: vm.expectRevert
**ethskills quote:** vm.expectRevert();                           // Any revert
vm.expectRevert("Insufficient balance");     // Specific message

### testing-k-04  (fact)
**Q:** When you run `forge test` with no fuzz configuration in foundry.toml and no CLI flags, how many runs does Foundry execute per fuzz test by default?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 256}`
**Reference:** Answer: 256
**ethskills quote:** # Default: 256 runs
forge test

### testing-k-05  (fact)
**Q:** forge-std's vm.expectEmit takes four boolean flags, e.g. vm.expectEmit(true, true, false, true). The first three flags choose whether to check the event's three indexed topics. What part of the emitted event does the fourth flag choose to check? Answer with one word.
End your reply with a line of the form "Answer: <word>".

**Grader:** `{"type": "regex", "pattern": "\\bdata\\b"}`
**Reference:** Answer: data
**ethskills quote:** vm.expectEmit(true, true, false, true);      // (topic1, topic2, topic3, data)

### testing-k-06  (recommendation)
**Q:** In a Foundry fuzz test you must constrain a uint256 fuzz input to a range. One idiom, vm.assume(condition), discards inputs that fail the condition. The generally preferred idiom instead reshapes every input into the valid range. What is the name of that preferred forge-std helper function?
End your reply with a line of the form "Answer: <function name>".

**Grader:** `{"type": "regex", "pattern": "\\bbound\\b"}`
**Reference:** Answer: bound
**ethskills quote:** // bound() is preferred over vm.assume() — bound reshapes, assume discards

### testing-k-07  (fact)
**Q:** In a Foundry fork test's setUp function, which single cheatcode both creates a fork of a network (from an RPC alias or URL, optionally pinned to a block number) and makes it the currently active fork?
End your reply with a line of the form "Answer: <cheatcode name>".

**Grader:** `{"type": "regex", "pattern": "create\\s?_?select\\s?_?fork"}`
**Reference:** Answer: vm.createSelectFork
**ethskills quote:** // Fork mainnet at a specific block for reproducibility
        vm.createSelectFork("mainnet", 19_000_000);

### testing-k-08  (fact)
**Q:** In a Foundry invariant test, random calls are usually routed through a handler contract. Which forge-std function do you call in setUp to register the handler as the contract whose functions the invariant fuzzer will call in random sequences?
End your reply with a line of the form "Answer: <function name>".

**Grader:** `{"type": "regex", "pattern": "target\\s?_?contract"}`
**Reference:** Answer: targetContract
**ethskills quote:** // Tell Foundry which contract to call randomly
        targetContract(address(handler));

### testing-k-09  (fact)
**Q:** forge-std's assertApproxEqRel(actual, expected, maxPercentDelta) takes a relative tolerance. In the fixed-point scale used for maxPercentDelta, what numeric value represents 100%?
End your reply with a line of the form "Answer: <value>".

**Grader:** `{"type": "regex", "pattern": "(1e18|10\\s*\\^\\s*18|10\\s*\\*\\*\\s*18|\\bwad\\b|1[,_]?000[,_]?000[,_]?000[,_]?000[,_]?000[,_]?000)"}`
**Reference:** Answer: 1e18 (WAD)
**ethskills quote:** assertApproxEqRel(actual, expected, maxPercentDelta); // in WAD (1e18 = 100%)

### testing-k-10  (fact)
**Q:** In a Foundry test, a contract reverts with the parameterless custom error `Unauthorized()`. To make vm.expectRevert match that specific custom error, you pass a member of the error type as the argument. What is the name of that member?
End your reply with a line of the form "Answer: <member name>".

**Grader:** `{"type": "regex", "pattern": "\\bselector\\b"}`
**Reference:** Answer: selector (e.g. MyContract.Unauthorized.selector)
**ethskills quote:** vm.expectRevert(MyContract.CustomError.selector); // Custom error


## tasks/skill-tooling.jsonl

### tooling-k-01  (fact)
**Q:** In the Foundry toolchain, which tool do you run to spin up a local Ethereum node that forks mainnet state (e.g. with a --fork-url flag) so you can test against real deployed contracts with fake ETH?
End your reply with a line of the form "Answer: <tool name>".

**Grader:** `{"type": "regex", "pattern": "\\banvil\\b"}`
**Reference:** Answer: anvil
**ethskills quote:** **Fork mainnet locally:**
```bash
anvil --fork-url https://eth.llamarpc.com
# Now test against real contracts with fake ETH at http://localhost:8545
```

### tooling-k-02  (fact)
**Q:** Goerli and Rinkeby are deprecated. Name the primary Ethereum testnet developers should use instead, and give its chain ID.
End your reply with a line of the form "Answer: <testnet name>, chain ID <number>".

**Grader:** `{"type": "regex_all", "patterns": ["sepolia", "\\b11155111\\b"]}`
**Reference:** Answer: Sepolia, chain ID 11155111
**ethskills quote:** **Primary testnet:** Sepolia (Chain ID: 11155111). Goerli and Rinkeby are deprecated.

### tooling-k-03  (fact)
**Q:** One long-standing Ethereum smart-contract development framework (a JavaScript-based suite dating back to the early days of Solidity tooling) is now deprecated, with developers told to use Foundry or Hardhat instead. Which framework is it?
End your reply with a line of the form "Answer: <framework>".

**Grader:** `{"type": "regex", "pattern": "\\btruffle\\b"}`
**Reference:** Answer: Truffle
**ethskills quote:** **Deprecated:** Truffle (use Foundry/Hardhat), Goerli/Rinkeby (use Sepolia)

### tooling-k-04  (fact)
**Q:** You have raw transaction calldata (like 0xa9059cbb...) but no ABI. Which Foundry `cast` subcommand decodes it by looking up the function selector in the public 4-byte signature directory?
End your reply with a line of the form "Answer: cast <subcommand>".

**Grader:** `{"type": "regex", "pattern": "4[- ]?byte[- ]?(decode|calldata)"}`
**Reference:** Answer: cast 4byte-decode
**ethskills quote:** # Decode calldata
cast 4byte-decode 0xa9059cbb...

### tooling-k-05  (fact)
**Q:** Using Foundry's `cast` CLI, which subcommand resolves an ENS name like vitalik.eth to its address?
End your reply with a line of the form "Answer: cast <subcommand>".

**Grader:** `{"type": "regex", "pattern": "resolve[- _]?name"}`
**Reference:** Answer: cast resolve-name
**ethskills quote:** # ENS resolution
cast resolve-name vitalik.eth --rpc-url $RPC

### tooling-k-06  (fact)
**Q:** After deploying with Foundry, which `forge` subcommand submits your contract's source code for verification on a block explorer such as Etherscan?
End your reply with a line of the form "Answer: forge <subcommand>".

**Grader:** `{"type": "regex", "pattern": "verify[- _]?contract"}`
**Reference:** Answer: forge verify-contract
**ethskills quote:** 6. **Verification:** `forge verify-contract` or Etherscan API

### tooling-k-07  (recommendation)
**Q:** For building a React frontend for an Ethereum dApp in 2026, name the two-library combo that has become the ecosystem-consensus choice: a React hooks library paired with the lightweight TypeScript Ethereum client it is built on.
End your reply with a line of the form "Answer: <library> + <library>".

**Grader:** `{"type": "regex_all", "patterns": ["\\bwagmi\\b", "\\bviem\\b"]}`
**Reference:** Answer: wagmi + viem
**ethskills quote:** | React frontends | **wagmi + viem** (or SE2 which wraps these) |

### tooling-k-08  (recommendation)
**Q:** A JavaScript library for talking to Ethereum has been gaining ground on ethers.js because it is smaller and has better TypeScript support, and it also underpins the most popular React hooks library. Which library is it?
End your reply with a line of the form "Answer: <library>".

**Grader:** `{"type": "regex", "pattern": "\\bviem\\b"}`
**Reference:** Answer: viem
**ethskills quote:** **Viem gaining on ethers.js** (smaller, better TypeScript)

### tooling-k-09  (fact)
**Q:** What single npx command scaffolds a new Scaffold-ETH 2 project (the full-stack Solidity + Next.js + Foundry toolkit)?
End your reply with a line of the form "Answer: npx <package>".

**Grader:** `{"type": "regex", "pattern": "create[- _]?eth"}`
**Reference:** Answer: npx create-eth@latest
**ethskills quote:** - **Setup:** `npx create-eth@latest`

### tooling-k-10  (fact)
**Q:** From the command line, which Foundry `cast` subcommand generates a Solidity interface for a deployed verified contract (the CLI counterpart to exploring a contract in a browser tool)?
End your reply with a line of the form "Answer: cast <subcommand>".

**Grader:** `{"type": "regex", "pattern": "cast\\s+interface|^\\s*interface\\b"}`
**Reference:** Answer: cast interface
**ethskills quote:** 3. **Contract exploration:** abi.ninja (browser) or `cast interface` (CLI)


## tasks/skill-wallets.jsonl

### wallets-k-01  (fact)
**Q:** Which EIP, activated in Ethereum's Pectra upgrade, lets a regular EOA delegate execution to smart-contract code (enabling batching, gas sponsorship, and session-key-style UX) without migrating to a new wallet?
End your reply with a line of the form "Answer: <EIP number>".

**Grader:** `{"type": "regex", "pattern": "\\b7702\\b"}`
**Reference:** Answer: EIP-7702
**ethskills quote:** **EIP-7702 is live.** Since Pectra (May 7, 2025), regular EOAs can delegate execution to smart-contract code without migrating wallets. This enables batching, gas sponsorship, and session-key-style UX.

### wallets-k-02  (fact)
**Q:** A raw Ethereum private key, written in hexadecimal without the 0x prefix, is how many hex characters long?
End your reply with a line of the form "Answer: <integer>".

**Grader:** `{"type": "bigint", "expect": 64}`
**Reference:** Answer: 64
**ethskills quote:** **Rule of thumb:** If `grep -r "0x[a-fA-F0-9]{64}" .` matches anything in your source code, you have a problem.

### wallets-k-03  (fact)
**Q:** In which month and year did Ethereum's Pectra upgrade activate on mainnet?
End your reply with a line of the form "Answer: <month year>".

**Grader:** `{"type": "regex_all", "patterns": ["\\bmay\\b", "\\b2025\\b"]}`
**Reference:** Answer: May 2025
**ethskills quote:** **EIP-7702 is live.** Since Pectra (May 7, 2025), regular EOAs can delegate execution to smart-contract code without migrating wallets.

### wallets-k-04  (fact)
**Q:** After an EOA installs an EIP-7702 delegation, how long does that delegation remain active?
A) It applies to exactly one transaction, then clears automatically
B) It stays active until it is replaced or explicitly cleared
C) It expires at the end of the current epoch
D) It expires after 24 hours
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "B"}`
**Reference:** Answer: B
**ethskills quote:** This is not automatically "one and done" - the delegation can stay active until it is replaced or explicitly cleared.

### wallets-k-05  (fact)
**Q:** In EIP-7702, what does the EOA holder's signed authorization message specify?
A) A spending limit in wei for the account
B) Which contract code the EOA is allowed to run as its account logic
C) A list of token contracts the account may approve
D) A replacement private key for the account
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "B"}`
**Reference:** Answer: B
**ethskills quote:** 1. The wallet signs a message that says which contract code the EOA can use.
2. A special EIP-7702 transaction submits that signed message.

### wallets-k-06  (fact)
**Q:** What is the canonical deployed address of the ERC-4337 EntryPoint contract, version 0.7?
End your reply with a line of the form "Answer: <0x-prefixed address>".

**Grader:** `{"type": "exact", "expect": "0x0000000071727De22E5E9d8BAf0edAc6f37da032"}`
**Reference:** Answer: 0x0000000071727De22E5E9d8BAf0edAc6f37da032
**ethskills quote:** EntryPoint v0.7: `0x0000000071727De22E5E9d8BAf0edAc6f37da032`.

### wallets-k-07  (fact)
**Q:** Safe (formerly Gnosis Safe) v1.4.1 contracts are deployed at deterministic addresses that are identical across Mainnet, Arbitrum, Base, and other major chains. What is the address of the Safe Singleton (the master-copy implementation) for v1.4.1?
End your reply with a line of the form "Answer: <0x-prefixed address>".

**Grader:** `{"type": "exact", "expect": "0x41675C099F32341bf84BFc5382aF534df5C7461a"}`
**Reference:** Answer: 0x41675C099F32341bf84BFc5382aF534df5C7461a
**ethskills quote:** | Safe Singleton | `0x41675C099F32341bf84BFc5382aF534df5C7461a` |

### wallets-k-08  (fact)
**Q:** Safe (formerly Gnosis Safe) v1.4.1 contracts are deployed at deterministic addresses that are identical across major chains. What is the address of the Safe MultiSend contract for v1.4.1?
End your reply with a line of the form "Answer: <0x-prefixed address>".

**Grader:** `{"type": "exact", "expect": "0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526"}`
**Reference:** Answer: 0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526
**ethskills quote:** | MultiSend | `0x38869bf66a61cF6bDB996A6aE40D5853Fd43B526` |

### wallets-k-09  (recommendation)
**Q:** An AI agent manages funds jointly with its human operator via a Safe multisig. The owners are: the agent's hot wallet (automated), the human's hot wallet (manual), and the human's cold wallet (recovery) - with the threshold set so the agent alone cannot move funds, but agent + human together can. Express this configuration in standard M-of-N form.
End your reply with a line of the form "Answer: <M-of-N>".

**Grader:** `{"type": "regex", "pattern": "2(-of-|\\s*of\\s*|\\s*/\\s*)3"}`
**Reference:** Answer: 2-of-3
**ethskills quote:** **Pattern:** 2-of-3 Safe
- Owner 1: Agent's wallet (hot, automated)
- Owner 2: Human's hot wallet (hot, manual)
- Owner 3: Human's cold wallet (cold, recovery)
- Threshold: 2 (agent can queue transactions and human can execute or vice versa)

### wallets-k-10  (recommendation)
**Q:** You discover that the private key of a funded wallet was committed to a Git repository. What is the FIRST priority?
A) Rewrite the Git history with git filter-repo to remove the key
B) Assume the key is compromised and immediately transfer all funds to a new wallet
C) Make the repository private and delete the offending commit
D) Nothing urgent, as long as the repository is private
End your reply with a line of the form "Answer: <letter>".

**Grader:** `{"type": "exact", "expect": "B"}`
**Reference:** Answer: B
**ethskills quote:** 1. **Assume it's compromised.** Don't hope nobody saw it.
2. **Transfer all funds immediately** to a new wallet.
3. **Rotate the key.** Generate a new one. The old one is burned forever.
4. **Clean Git history** with `git filter-repo` or BFG Repo Cleaner — but this is damage control, not prevention.
