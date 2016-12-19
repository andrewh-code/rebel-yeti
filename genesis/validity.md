# Ethereum Yellow Paper
TO DO: update formatting 
TO DO: add example based off genesis block 

## Purpose
The purpose of this document is to provide a layman's explanation of the block header validity functions found in the Ethereum Yellow Paper written by Gavin Wood.
## Section 4.4 - The Block

**Block header attributes**

**parentHash** (Hp): The Keccak 256-bit hash of the parent block's header, in its entirety. <br>
**ommersHash** (Ho): The Keccak 256-bit hash of the ommers list portion of this block. <br>


| Attribute         |Symbol               |Description                     |
| ------------------|---------------------|--------------------------------|
| parentHash        |       Hp            | The Keccak 256-bit hash of the parent block's header, in its entirety. |
| ommersHash        |       Ho            | The Keccak 256-bit hash of the ommers list portion of this block.
| beneficiary       |       Hc            | The 160-bit address to which all fees collected from the successful mining of this block be transferred.
| stateRoot         |       Ho            | The keccak 256-bit hash of the root node of the state trie, after all transactions are executed and finalisations applied.
| transactionsRoot  |       Ht            | The keccak 256-bit hash of the root node of the trie structure populated with each transaction in the transactions list portion of the block.
| receiptsRoot      |       He            | The Keccak 256-bit hash of the root node of the trie structure populated with the receipts of each transaction in the transactions list portion of the block.
| logsBloom         |       Hb            | The Bloom filter composed from indexable information (logger address and log topics) contained in each log entry from the receipt of each transaction  in the transactions list.
| difficulty        |       Hd            | 
| number            |       Hi            |
| gasLimit          |       Hl            |
| gasused           |       Hg            |
| timestamp         |       Hs            |
| extraData         |       Hx            |
| mixHash           |       Hm            |
| nonce             |       Hn            |


other
Block number = Hi    
### Section 4.4.4 - Block Header Validity

(37)    

Block number: 
(38)    
The current block's (Hi) block number is the parent block plus one
    
Canoncial difficulty:
(39)   
In order to understand (39), you have to understand equations (40) to (44).


    (40)
    Pretty much the initial difficulty (D0) is 2^17
    TO DO: watch vitaly's presentation, he explained why it's 2^17

    (41) 
    Take the floor of the parent block's difficulty divided by 2048 (2^11). Basically round down to the nearest whole number after dividing.

    (42)
    If the timestamp of the current block (H2) is less than the sum of the timestamp of the parent block plus 13, then set it to 1
    Else, set it to -1

    (43)
    Take your current block's time stamp and subtract the parent block's timestamp fom it. Divide the result by 10 and then take that result and floor it (round down).
    Take whichever value is bigger, this one or -99

    (44) 
    take the block number and divide it by 100 000. Subtract the result by 2. Floor (round down) the answer and then subtract 2. Then use this answer as the exponent in the 2 to the power of calculation.
    Floor the final result

The difficulty of the current block can be of three possibilities:
    1. The initial difficulty (D0) set in the very first block, the genesis block (This is only done if you're looking at the genesis block) 
    2. the maximum of the following 2 options:
        1.1 The initial difficulty (D0) of the genesis block
        1.2 the initial difficulty OR the parent block's difficulty + (41) + (43) + (44). Whichever one is bigger. This only applies if the block number (Hi) of the block you're looking at is less than NH (TO DO: NH)


The gas limit has to fulfill the following three relations:
    (45)
    gas limit must be less than the gas limit of the parent block's gas limi plus the floor of the parent block's gas limit divided by 1024  
    AND

    (46)
    gas limit must be greater than the gas limit of the parent block's gas limit subtract the floor of the parent block's gas limit divided by 1024
    AND

    (47)
    gas limit must be equal to or greater than 125 000


Timestamp:

(48)
The timestamp of the block must be greater than the parent block's time stamp

Nonce:

(49)
The nonce is less than or equal to 2^256 divided by the current block's difficulty AND m = mixedHash of the block 


