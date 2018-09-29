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

	# validate de hash with the atual block and the previous one
	def validate_chain(self):
		for i in range(1, len(self.chain)):
			current = self.chain[i]
			previous = self.chain[i - 1]
			# check te current block's hash
			if(current.hash() != current.generate_hash()):
				print("The current block is not valid, the atual hash it is not the same!")
				return False
				# check the previous block's hash in then atual block
			if(current.previous_hash != previous.generate_hash()):
				print("The previous block's hash is invalid!")
				return False
			# returned true after passed in the two conditions 
			return True
