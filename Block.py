# A very basic block class in Python3
from hashlib import sha256
from datetime import datetime


class Block:
    def __init__(self, transactions, previous_hash, nonce=0):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def print_block(self):
        # prints block contents
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())

    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.transactions) +\
                    str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()

    def add_transaction(self, _transaction):
        pass

    def remove_transaction(self, txID):
        pass