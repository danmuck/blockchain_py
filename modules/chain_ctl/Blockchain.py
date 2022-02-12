import datetime, hashlib, json, os

from .Block import Block_
class Blockchain_:

    def __init__(self, chain_id:int) -> None:

        self.chain_id = chain_id
        self.chain = {}

        self.genesis_block = Block_(
            index=len(self.chain.keys()),
            previous_hash = "0x" + str(self.chain_id).zfill(64),
            nonce = 42069,
            signature = 'im the genesis block... new chain incoming!! :)',
            txns = [],
            chain_data = {},
            print_it=True
        )
        self.chain.update((self.genesis_block.block_dict))
        print("\n\nNew Blockchain_ initialized...\n  CHAIN: ", json.dumps(self.chain, indent=2), "\n\n")

    def get_tallest_block(self):
        block_list = tuple(self.chain.keys())
        block_data = dict(self.chain.get(f'{block_list[-1]}'))

        # print("TALLEST BLOCK: ")
        # print(block_list[-1], ":", json.dumps(block_data, indent=2))
        # print(block_data)
        return block_data, block_list[-1]

    def check_previous_block(self, block_hash:str):

        pass

    def append_block_(self, block:Block_):
        appendage = block.block
        if appendage.get('previous_hash') == self.get_tallest_block()[1] and appendage.get('index') == len(self.chain):
            self.chain.update(block.block_dict)
        else:
            print(f"\n\nErr!! Bad Block on block sig: [{appendage.get('signature')}] !!")
            print("BLOCK_HEIGHT: ", appendage.get("index"), " | REAL_HEIGHT: ", len(self.chain))
            print("REAL_PREV_HASH: ", self.get_tallest_block()[1])
            print("PREV_ON_BLOCK:  ", appendage.get('previous_hash'))
