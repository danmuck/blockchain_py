import datetime, hashlib, json, os
from itertools import chain

from .Block import Block_
class Blockchain_:

    def __init__(self, chain_id:int) -> None:

        self.chain_id = chain_id
        self.chain = {}
        self.chain_data = {}

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
        self.chain = self.load_chain_json()
        print("\n\nBlockchain_ initialized...\n  CHAIN: ", json.dumps(self.chain, indent=2), "\n\n")


    def load_chain_json(self):
        try:
            with open(f"{os.getcwd()}/chain_data/Chain_state_{self.chain_id}.json", "r") as file:
                chain_ = dict(json.load(file))
                self.chain = chain_
                return chain_
        except json.JSONDecodeError:
            print("SCREAM")
        except FileNotFoundError:
            try:
                os.mkdir(f"{os.getcwd()}/chain_data/")
            except FileExistsError:
                pass
            finally:
                with open(f"{os.getcwd()}/chain_data/Chain_state_{self.chain_id}.json", "x") as file:
                    chain_ = json.dumps(self.chain)
                    file.write(chain_)

    def write_chain_json(self):
        with open(f"{os.getcwd()}/chain_data/Chain_state_{self.chain_id}.json", "w") as file:
            file.write(json.dumps(self.chain, indent=2))
        with open(f"{os.getcwd()}/chain_data/Chain_data_{self.chain_id}.json", "w") as file:
            file.write(json.dumps(self.chain_data, indent=2))

    def get_tallest_block(self):
        block_list = tuple(self.chain.keys())
        block_data = dict(self.chain.get(f'{block_list[-1]}'))

        # print("TALLEST BLOCK: ")
        # print(block_list[-1], ":", json.dumps(block_data, indent=2))
        # print(block_data)
        return block_data, block_list[-1]

    def check_previous_block(self, block_hash:str):
        pass

    def validate_chain(self):
        for i in self.chain.keys():
            block_key = self.chain.get(i)['previous_hash']
            prev_block = self.chain.get(block_key)
            encoded_block = json.dumps(prev_block).encode()
            hashed_block = ''.join(('0x', hashlib.sha256(encoded_block).hexdigest()))
            if block_key == hashed_block:
                print(f'good_block: {i}')
                print(f'Prev_hash: {hashed_block}')
                pass
            elif i == list(self.chain.keys())[0]:
                print(f'Gen_block: {i}')
            else:
                print(f'!!Err Bad chain. [{i}] !!')
                print(f'    Real_hash: {hashed_block}')


    def append_block_(self, block:Block_):
        appendage = block.block
        # self.load_chain_json()
        if appendage.get('previous_hash') == self.get_tallest_block()[1] and appendage.get('index') == len(self.chain):
            self.chain.update(block.block_dict)
            self.write_chain_json()
            self.update_chain_data_()
            # print(self.chain_data[f'{block.block_hash}'])
        else:
            print(f"\n\nErr!! Bad Block on block sig: [{appendage.get('signature')}] !!")
            print("BLOCK_HEIGHT: ", appendage.get("index"), " | REAL_HEIGHT: ", len(self.chain))
            print("REAL_PREV_HASH: ", self.get_tallest_block()[1])
            print("PREV_ON_BLOCK:  ", appendage.get('previous_hash'))

    def update_chain_data_(self):
        self.load_chain_json()
        for block in self.chain.items():
            # print(block)
            self.chain_data.update({block[0]: (block[1]['index'], block[1]['chain_data'])})

