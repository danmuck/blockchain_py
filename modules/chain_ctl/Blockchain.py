import datetime, hashlib, json, os

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
            print_it=False
        )
        self.chain.update((self.genesis_block.block_dict))
        self.validate_chain()
        print("\n\nBlockchain_ initialized...\n  TAIL: ", json.dumps(list(self.chain.values())[-4:], indent=2), "\n\n")
    
    def validate_chain(self):
        '''
            Validate the current chain against its canonical master; 
                currently validating against chain_data/Chain_state.json
        '''
        self.chain = self.load_chain_json()
        j = 0
        for i in self.chain.keys():
            block_key = self.chain.get(i)['previous_hash']
            prev_block = self.chain.get(block_key)
            encoded_block = json.dumps(prev_block).encode()
            hashed_block = ''.join(('0x', hashlib.sha256(encoded_block).hexdigest()))
            if block_key == hashed_block:
                print(f'Previous block hashed:\t {prev_block["index"]}::{hashed_block}')
                print(f'Good Block:\t\t {self.chain.get(i)["index"]}::{i}')
            elif i == list(self.chain.keys())[0]:
                print()
                print(f'Genesis_block:\t\t {j}::{i}')
            else:
                print(f'\n!!Err Bad block. [{i}] !! \n')
                raise Exception
        self.update_chain_data_()
        print("!!Hey [CHAIN IS VALID]  !!")
        if len(self.chain.keys()) % 100 == 0:
            print(self.hash_chain_())

    def load_chain_json(self) -> dict:
        '''
            File handling for the Blockchain_ state via JSON
        '''
        try:
            with open(f"{os.getcwd()}/chain_data/Chain_state_{self.chain_id}.json", "r") as file:
                chain_ = dict(json.load(file))
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
                    return self.chain

    def write_chain_json(self):
        '''
            Update Blockchain_ state along with its chain_data to JSON files
        '''
        with open(f"{os.getcwd()}/chain_data/Chain_state_{self.chain_id}.json", "w") as file:
            file.write(json.dumps(self.chain, indent=2))
        with open(f"{os.getcwd()}/chain_data/Chain_data_{self.chain_id}.json", "w") as file:
            file.write(json.dumps(self.chain_data, indent=2))

    def get_tallest_block(self):
        '''
            Grab the tallest Block_ on the chain
        '''
        block_list = tuple(self.chain.keys())
        block_data = dict(self.chain.get(f'{block_list[-1]}'))

        # print("TALLEST BLOCK: ")
        # print(block_list[-1], ":", json.dumps(block_data, indent=2))
        # print(block_data)
        return block_data, block_list[-1]

    def check_previous_block(self, block_hash:str):
        '''
            Not even a thing yet, dont worry about comments
        '''
        pass

    # def hash_json_(self) -> str:
    #     chain_ = self.load_chain_json()
    #     encoded_chain = json.dumps(chain_).encode()
    #     return ''.join(('0x', hashlib.sha512(encoded_chain).hexdigest()))

    def hash_chain_(self) -> str:
        '''
            Hash the chain...
        '''
        chain_ = self.chain
        encoded_chain = json.dumps(chain_).encode()
        return ''.join(('0x', hashlib.sha512(encoded_chain).hexdigest()))
        
    def append_block_(self, block:Block_):
        '''
            Append block to chain...
        '''
        self.validate_chain()
        appendage = block.block
        if appendage.get('previous_hash') == self.get_tallest_block()[1] and appendage.get('index') == len(self.chain):
            self.chain.update(block.block_dict)
            self.write_chain_json()
            self.validate_chain()
        else:
            print(f"\n\nErr!! Bad Block on block sig: [{appendage.get('signature')}] !!")
            print("BLOCK_HEIGHT: ", appendage.get("index"), " | REAL_HEIGHT: ", len(self.chain))
            print("REAL_PREV_HASH: ", self.get_tallest_block()[1])
            print("PREV_ON_BLOCK:  ", appendage.get('previous_hash'))

    def update_chain_data_(self):
        '''
            Update chain_data on chain as separate dictionary for logging and interfacing
        '''
        # self.load_chain_json()
        for block in self.chain.items():
            # print(block)
            self.chain_data.update({block[0]: (block[1]['index'], block[1]['chain_data'])})

