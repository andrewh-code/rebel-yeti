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

{
  "nonce": "0x0000000000000042",
  "difficulty": "0x400000000",
  "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "coinbase": "0x0000000000000000000000000000000000000000",
  "timestamp": "0x00",
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "extraData": "0x11bbe8db4e347b4e8c937c1c8370e4b5ed33adb3db69cbdb7a38e1e50b1b82fa",
  "gasLimit": "0x1388",
  "alloc": {
    "3282791d6fd713f1e94f4bfd565eaa78b3a0599d": {
      "balance": "1337000000000000000000"
    },
    "17961d633bcf20a7b029a7d94b7df4da2ec5427f": {
      "balance": "229427000000000000000"
    }
  }
}
'''



def main():
    
    file_name = "genesis_block.json"
    gb = {}
    
    # gb
    gb["nonce"]         = "0x0000000000000000"  # 16 digit hex
    gb["timestamp"]     = "0x00"
    gb["parentHash"]    = "0x0000000000000000000000000000000000000000000000000000000000000000"
    gb["extraData"]     = "0x00"
    gb["gasLimit"]      = "0x3E8" #1000 
    gb["difficulty"]    = "0x64" #100
    gb["mixhash"]       =  "0x0000000000000000000000000000000000000000000000000000000000000000"
    gb["coinbase"]      = "0x0000000000000000000000000000000000000000000000000000000000000000" #160 bit address, set by miner, can be anything in the geensis
    gb["alloc"]         = " "
    
    
    with open(file_name, 'w') as outfile:
        json.dump(gb, outfile)
        #json.dump(gb, outfile, ensure_ascii=False) # for unicode purposes
    
if __name__ == "__main__":
    main()