import datetime, hashlib, json, os

from .Block import Block_

class Blockchain_:

    def __init__(self, chain_id:int) -> None:

        self.chain_id = chain_id
        self.chain = {}

        self.genesis_block = Block_(
            index=0,
            previous_hash = "0x" + str(self.chain_id).zfill(64),
            nonce = 0,
            txns = [],
            signature = 'im the genesis block :)',
            chain_data = {},
        )
        self.chain.update((self.genesis_block.return_data()))
        print("\n\n  Hello from class Blockchain_\n  CHAIN: ",self.chain, "\n\n")

    def get_tallest_block(self):
        block_list = tuple(self.chain.keys())
        block_data = self.chain.get(f'{block_list[-1]}')

        print("TALLEST BLOCK: ")
        print(block_list[-1], ": ", block_data)
        
        return (block_data)


    def append_block_(self, *blocks:Block_):
        for block in blocks:
            self.chain.update(block.return_data())
