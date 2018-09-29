# import the Block object from block.py
from block import Block

#init a Blockchain
class Blockchain:
	def __init__(self):
		self.chain = []
		self.all_transactions = []
		# first block creation
		self.genesis_block()

	def genesis_block():
		# don't exist previous transactions
		transactions = []
		# don't exist a previous hash
		previous_hash = "0"
		self.chain.append(Block(transactions, previous_hash))