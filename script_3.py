from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

# create a new blockchain
local_blockchain = Blockchain()

# print a genesis block
local_blockchain.print_blocks()

# add a new blocks to a chain
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

# print all blocks in the chain
local_blockchain.print_blocks()

# try tamper a chain modifing a block
local_blockchain.chain[2].transactions = fake_transactions

# call a validate function to verify a chain
local_blockchain.validate_chain()