# A very simple blockchain using our Block class
import Transaction
import Block
import User


def validate_proof(_proof, _difficulty):
for x in range(_difficulty):
    if _proof[x] != '0':
        return True
    else:
        continue
return False


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        self.chain.append(Block('', 0))

    # prints contents of blockchain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()    

    def last_hash(self):
        return self.chain[len(self.chain)-1].hash

    # add block to blockchain `chain`
    def add_block(self, transactions):
        prev_hash = self.last_hash()
        new_block = Block(transactions, prev_hash)
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block

    def validate_chain(self):
        for i in range(1, len(self.chain)): 
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.generate_hash():
                return False
            if previous.hash != previous.generate_hash():
                return False
        return True

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        searching = validate_proof(proof, difficulty)
        while searching:
            block.nonce += 1
            proof = block.generate_hash()
            searching = validate_proof(proof, difficulty)
        block.nonce = 0
        return proof
