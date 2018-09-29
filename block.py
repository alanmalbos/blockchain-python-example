from datetime import datetime
from hashlib import sha256

class Block:
	def __init__(self, transactions, previous_hash):
		self.timestamp = datetime.now()
		self.transactions = transactions
		self.previous_hash = previous_hash
		self.hash = sel.genarate_hash()

	def print_block(self):
		# print the block content
		print("Timestamp: ", self.timestamp)
		print("Transactions: ", self.transactions)
		print("Current hash: ", self.genarate_hash())

	def generate_hash(self):
		block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
		block_hash = sha256(block_contents.encode())
		return block_hash.hexdigest()