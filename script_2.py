from hashlib import sha256
# the transactions for the new block
new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# set a difficulty with the amoung of zeros that must be found
difficulty = 2
nonce = 0

# creating the proof of work
proof = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()

# printing the proof
print(proof)

#finding a proof that has 2 leading zeros
while (proof[:2] != "0" * difficulty):
	nonce += 1
	proof = sha256((str(nonce) + str()new_transactions).encode()).hexdigest()

# print the final proof that was found
final_proof = proof
print(final_proof)	