import datetime, hashlib, json, os

from .Block import Block_

class Blockchain_:

    def __init__(self, chain_id:int) -> None:

        self.chain_id = chain_id
        self.chain = {}

        self.genesis_block = Block_(
            index=len(self.chain.keys()),
            previous_hash = "0x" + str(self.chain_id).zfill(64),
            nonce = 0,
            txns = [],
            signature = 'im the genesis block :)',
            chain_data = {},
        )
        self.chain.update((self.genesis_block.return_data()))
        print("\n\n  Hello from class Blockchain_\n  CHAIN: ",self.chain, "\n\n")

    def get_tallest_block(self) -> dict:
        block_list = tuple(self.chain.keys())
        block_data = self.chain.get(f'{block_list[-1]}')

        print("TALLEST BLOCK: ")
        print(block_list[-1], ":", json.dumps(block_data, indent=2))
        
        return (block_data)

    def check_previous_block(self, block_hash:str):

        pass

    def append_block_(self, block:Block_):
        appendage = block.return_data().get(block.block_hash)
        if appendage['index'] == len(self.chain):
            self.chain.update(block.return_data())
        else:
            print("Err!! Wrong Height !!")
