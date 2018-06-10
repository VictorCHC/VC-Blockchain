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

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp,
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        