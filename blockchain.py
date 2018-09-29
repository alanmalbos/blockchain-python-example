# import the Block object from block.py
from block import Block

#init a Blockchain
class Blockchain:
	def __init__(self):
		self.chain = []
		self.all_transactions = []
		# first block creation
		self.genesis_block()

	#create a genesis block
	def genesis_block():
		# don't exist previous transactions
		transactions = []
		# don't exist a previous hash
		previous_hash = "0"
		self.chain.append(Block(transactions, previous_hash))

	# print all blocks in chain
	def print_blocks(self):
		for i in range(len(self.chain)):
			current_block = self.chain[i]
			print("Block {} {}".format(i, current_block))
			current_block.print_contents()

	# add a new block to end of blockchain 'chain'
	def add_block(self, transactions):
		previous_block_hash = self.chain[len(self.chain) - 1].hash
		new_block = Block(transactions, previous_block_hash)
		self.chain.append(new_block)