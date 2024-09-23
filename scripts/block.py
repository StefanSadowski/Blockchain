"""Author: Stefan Sadowski"""
# IMPORTS
import hashlib
import json
from time import time

# CONSTANTS

# CLASSES
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # create a genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Creating a new Block for a blockchain.

        :param: <int> proof: The proof given by a Work algorithm
        :param: <str> previous_hash (optional): Hash of the previous block

        :return: <dict> New Block
        """
        # create a new block 
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # add a new transaction
        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })

        return self.last_block["index"] + 1

    @staticmethod
    def hash(block):
        """
        Creating a SHA-256 hash of a block
        :param: block
        """
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # returns last block
        return self.chain[-1]
    
    def proof_of_work(self, last_proof):
            """
            Simple Proof of Work Algorithm:
            - Find a number p' such that hash(p*p') contains leading 4 zeroes, where p is the previous p'
            - p is the previous proof, and p' is the new proof
            :param: <int> last_proof
            :return: <int>
            """

            proof = 0
            while self.valid_proof(last_proof, proof) is False:
                proof += 1

            return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param: <int> last_proof_ Previous Proof
        :param: <int> proof: Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
# FUNCTIONS

# CODE
if __name__ == "__main__":
    pass