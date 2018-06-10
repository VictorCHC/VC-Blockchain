# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:39:56 2018

@author: VictorCHC

Reference:
    https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
"""
import hashlib as hasher
import datetime as date

#Basic block structure
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
    
    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode())
        return sha.hexdigest()


# Genesis Block
"""A genesis block is a special block which is the first block in the chain.
The block index is 0 and it has an arbitrary data value and an arbitrary value 
in the “previous hash” parameter"""

def create_genesis_block():
    """Manually construct a block with index zero and abritrary previous hash"""
    return Block(0, date.datetime.now(), "Genesis Block", "0")
    

# Succeeding blocks in the chain
"""After creating a genesis block a function is needed to generate succeeding
blocks in the blockchain. This function will take the previous block in the
chain as a parameter, create the data for the block to be generated, and return
the new block with its appropriate data. When new blocks has information from
previous blocks, the integrity of the blockchain increases with each new block.
This cryptographic chain makes it difficult for outside parties to alter 
previous records in the chain."""

def next_block(last_block):
    """Takes previous block in the chain as a parameter, create the data for 
    the block to be generated, and return the new block with its appropriate 
    data"""
    
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Block number " + str(this_index)
    this_hash = last_block.hash
    
    return Block(this_index, this_timestamp, this_data, this_hash)


# Creating the blockchain
"""The blockchain will be a simple Python list. Element zero in the list will
be the genesis block. We will make the chain only 50 blocks long with a
for loop."""

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Number of blocks to add AFTER the genesis block
num_of_blocks_to_add = 49

# Add blocks to the chain
for i in range(num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    
    print ("Block #{} has been added to the blockchain!").format(block_to_add.index)
    print ("Hash: {}\n").format(block_to_add.hash)