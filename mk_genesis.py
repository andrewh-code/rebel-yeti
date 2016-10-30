#!/usr/bin/python 

# import libraries
import json
import argparse
import random
import binascii
import os
import time

'''
{
    "nonce": "0xdeadbeefdeadbeef",
    "timestamp": "0x0",
    "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "extraData": "0x0",
    "gasLimit": "0x8000000",
    "difficulty": "0x400",
    "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "coinbase": "0x3333333333333333333333333333333333333333",
    "alloc": {
    }
}
'''

def main():
    
    init_hex = "0x0000000000000000000000000000000000000000000000000000000000000000"
    # create hash table to hold arguments  
    genesis_hash = {}
    genesis_hash['nonce'] = ''
    genesis_hash['timestamp'] = ''
    genesis_hash['parentHash'] = ''
    genesis_hash['extraData'] = ''
    genesis_hash['gasLimit'] = ''
    genesis_hash['difficulty'] = ''
    genesis_hash['mixhash'] = ''
    genesis_hash['coinbase'] = ''
    genesis_hash['alloc'] = ''
    
    
    
    # nonce
    str_out = "";  
    str_out = generate_nonce()
    str_out = left_pad_x(str_out)
    genesis_hash['nonce'] = str_out

    # timestamp
    str_timestamp = "";
    str_timestamp = generate_timestamp()
    str_timestamp = left_pad_x(str_timestamp)
    genesis_hash['timestamp'] = str_timestamp
    
    # parentHash
    # initiate to 0 for the genesis block?
    genesis_hash['parentHash'] = init_hex
    
    #gasLimit 
    str_gas_limit = set_gas_limit(100)
    str_gas_limit = left_pad_x(str_gas_limit)
    genesis_hash['gasLimit'] = str_gas_limit
    
    
    # output hash
    for key in genesis_hash:
        print key + '\t' + genesis_hash[key]

# generate nonce
def generate_nonce():
    
    # n <= 2^256/Hd  ^  m = Hm
    
    str_random = binascii.b2a_hex(os.urandom(8))
    #str_random = random.randint(0, 18446744073709551615)
    
    return str_random 

# add the 0x representation of the hex value (string)
def left_pad_x(str_input):
    pad = "0x"
    return pad + str_input



# generate timestamp
def generate_timestamp():
    '''
        timestamp: a sclar value equal to the reasonable
        output of Unix's time() at the block's inception; 
        formally Hs 
    '''
    
    timestamp = str(int(time.time()))   # use time.time() to represent Unix time 
    timestamp = binascii.b2a_hex(timestamp)

    return timestamp

# set gasLimit
def set_gas_limit(limit):    

    '''
        if ((limit == 0) or (not limit)):
            # set default gas limit value 
            gas_limit = str(100)
        else:
            gas_limit = str(limit)
    '''

    return gas_limit

if __name__ == "__main__":
    main()