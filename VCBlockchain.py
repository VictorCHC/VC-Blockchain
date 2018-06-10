# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:39:56 2018

@author: VictorCHC

Reference:
    https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
"""
import hashlib as hasher

"""This blockchain stores a timestamp and an index. Each block will have
a self-identifying hash. Each block's hash will be a cryptographic hash of the
block's index, timestamp data, and the hash of the previous block's hash.
The data can be anything you want"""

#Basic block structure
class Block:
        
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp,
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdigest()


"""A genesis block is a special block which is the first block in the chain.
The block index is 0 and it has an arbitrary data value and an arbitrary value 
in the “previous hash” parameter"""

