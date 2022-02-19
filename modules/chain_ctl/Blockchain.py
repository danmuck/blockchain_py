import datetime, hashlib, json, os

from .Block import Block_

class Blockchain_:
    chain_id:int
    chain:dict
    chain_data:dict
    genesis_b:str
    sync_mc = bool
    txns_:dict
    def __init__(self, chain_id:int) -> None:

        self.chain_id:int = chain_id
        self.chain:dict = {}
        self.chain_data:dict = {}
        self.sync_mc = True

        self.genesis_block = Block_(
            index=len(self.chain.keys()),
            previous_hash = "0x" + str(self.chain_id).zfill(64),
            nonce = 42069,
            signature = 'im the genesis block... new chain incoming!! :)',
            txns = {},
            chain_data = {},
            print_it=False
        )
        # global MASTER_CHAIN
        # MASTER_CHAIN = load_master_chain(self)
        
        self.chain.update((self.genesis_block.block_data))
        # try:
        #     self.validate_chain()
        # except Exception:
        #     self.chain = self.load_chain_json()
        self.validate_chain(True)
        self.genesis_b = str(list(self.chain.keys())[0])
        print("\n\nBlockchain_ initialized...\n  TAIL: ", json.dumps(list(self.chain.values())[-4:], indent=2), "\n\n")
    
    def validate_chain(self, print_it=False) -> bool:
        '''
            Validate the current chain against its canonical master; 
                currently validating against chain_data/Chain_state.json
        '''
        chain_ = self.load_chain_json()
        for i in self.chain.keys():
            block_key = self.chain.get(i)['previous_hash']
            prev_block = self.chain.get(block_key)
            encoded_block = json.dumps(prev_block).encode()
            hashed_block = ''.join(('0x', hashlib.sha256(encoded_block).hexdigest()))
            if block_key == hashed_block:
                # print(f'Previous block hashed:\t {prev_block["index"]}::{hashed_block}')
                # print(f'Good Block:\t\t {chain_.get(i)["index"]}::{i}')
                pass
            elif i == list(self.chain.keys())[0]:
                pass
            else:
                print(f'\n!!Err Bad block. [{i}] !! \n')
                raise Exception
        for j in chain_.keys():
            block_key = chain_.get(j)['previous_hash']
            prev_block = chain_.get(block_key)
            encoded_block = json.dumps(prev_block).encode()
            hashed_block = ''.join(('0x', hashlib.sha256(encoded_block).hexdigest()))
            if block_key == hashed_block:
                pass
            elif j == list(chain_.keys())[0]:
                pass
            else:
                print(f'\n!!Err Bad block. [{i}] !! \n')
                raise Exception

        if list(self.chain.keys()) in list(chain_.keys()) and len(chain_) >= len(self.chain) or len(chain_) == 1:
            if self.chain == chain_:
                pass
            self.load_chain_json()
        elif len(self.chain) > len(chain_) and list(chain_.keys()) in list(self.chain.keys()):
            # prepare to diverge
            self.chain_id+=1
            print(f"!Err Chain height surpassed master::Diverging to chain_id: {self.chain_id}...  !!")
            self.validate_chain()
        else:
            self.chain = self.load_chain_json()

        self.validate_master_chain(chain_, print_it)

        self.update_chain_data_()
        if print_it is True:
            print("!!Hey [chain valid]  !!")
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

    def sync_to_master(self):
        self.chain = self.load_master_chain()
        self.update_chain_data_()
        self.write_chain_json()
        self.validate_chain()

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
        appendage = block.block
        self.validate_chain()
        if appendage.get('previous_hash') == self.get_tallest_block()[1] and appendage.get('index') == len(self.chain):
            self.chain.update(block.block_data)
            print("!!Hey [new block success]  !!")
            self.write_chain_json()
            self.validate_chain()
        else:
            print(f"\n\nErr!! Bad Block on block sig: [{appendage.get('signature')}] !!")

    def update_chain_data_(self):
        '''
            Update chain_data on chain as separate dictionary for logging and interfacing
        '''
        # self.load_chain_json()
        for block in self.chain.items():
            # print(block)
            self.chain_data.update({block[0]: (block[1]['index'], block[1]['chain_data'])})

    def join_data(self, wallet_:dict=None):
        joined_chain_data = {} #chain_data
        joined_txns_all = {} #txns
        joined_txn_splits = {}
        joined_invent_splits = {"":{}}
        for block in self.chain.items():
            # print(block) 
            # block[0] is hash, block[1] is dict
            self.chain_data.update({block[0]: (block[1]['index'], block[1]['chain_data'])})
            if block[1]['chain_data'] != []:    
                joined_chain_data.update(block[1]['chain_data'])
        print("======================================================")
        for block in self.chain.items():
            # print(block[1]['transactions'])
            # block[0] is hash
            # block[1] is data
            if block[1]['transactions'] != {}:
                joined_txns_all.update(block[1]['transactions'])
        
        for key, value in joined_txns_all.items():
            '''
                Get Wallet balances
            '''
            txn_data = dict(value)

            if txn_data['to'] not in joined_txn_splits.keys():
                joined_txn_splits.update({txn_data['to']: 0})
            
            if txn_data['from'] not in joined_txn_splits.keys():
                joined_txn_splits.update({txn_data['from']: 0})

            to_bal = float(joined_txn_splits.get(txn_data["to"]))
            from_bal = float(joined_txn_splits.get(txn_data["from"]))
            joined_txn_splits.update({txn_data['to']: sum([to_bal, float(txn_data['amt'])])})
            joined_txn_splits.update({txn_data['from']: sum([from_bal, float(- txn_data['amt'])])})
        
        if wallet_ is not None:
            wallet_keys = [*wallet_]
            wallet_d = dict
            for key in wallet_keys:
                if key in joined_txn_splits.keys():
                    try:
                        with open(f"{os.getcwd()}/user_data/wallet.json", "r") as file:
                            wallet = dict(json.load(file))
                            wallet[key]['balance'] = joined_txn_splits[key]
                            # wallet[key]['data'] = 
                            wallet_d = wallet
                        with open(f"{os.getcwd()}/user_data/wallet.json", "w") as file:
                            file.write(json.dumps(wallet_d, indent=2))
                    except FileNotFoundError:
                        pass

        for key, value in joined_txns_all.items():
            '''
                Get Wallet inventory
            '''
            # to, from, data
            list_ =[(str, str, {})]

            if txn_data['to'] not in joined_invent_splits.keys():
                joined_invent_splits.update({txn_data['to']: {}})
                pass
            
            if txn_data['from'] not in joined_invent_splits.keys():
                joined_invent_splits.update({txn_data['from']: {}})
                pass

            if value['data'] != {}:
                print(value['data'])
                # joined_invent_splits.update({txn_data['to']: value['data']})
                joined_invent_splits[txn_data['to']].update(value['data'])

        if wallet_ is not None:
            wallet_keys = [*wallet_]
            wallet_d = dict
            for key in wallet_keys:
                if key in joined_txn_splits.keys():
                    try:
                        with open(f"{os.getcwd()}/user_data/wallet.json", "r") as file:
                            wallet = dict(json.load(file))
                            wallet[key]['inv_data'] = joined_invent_splits[key]
                            wallet_d = wallet
                        with open(f"{os.getcwd()}/user_data/wallet.json", "w") as file:
                            file.write(json.dumps(wallet_d, indent=2))
                    except FileNotFoundError:
                        pass

        return joined_chain_data, joined_txns_all, joined_txn_splits, joined_invent_splits
        

        
    def load_master_chain(self, chk_chain:dict=None) -> dict:
        '''
            File handling for the Master Blockchain_ state via JSON
        '''
        try:
            with open(f"{os.getcwd()}/Master_chain.json", "r") as file:
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
                with open(f"{os.getcwd()}/Master_chain.json", "x") as file:
                    if chk_chain != None:
                        chain_ = json.dumps(chk_chain)
                        file.write(chain_)
                        return chk_chain
                    file.write(json.dumps({"oops": "goof", "probably": "delete_me"}))
                    print("!!Err No chain given to load_master_chain()  !!")
                    return {}

    def update_master_chain(self, new_master:dict, print_it=False):
        '''
            Update Master Blockchain_ state along with its chain_data to JSON files
        '''
        with open(f"{os.getcwd()}/Master_chain.json", "w") as file:
            file.write(json.dumps(new_master, indent=2))
            if print_it is True:
                print("!!Hey [on master]  !!")
        pass

    def validate_master_chain(self, new_master:dict=None, print_it=False):
        '''
            Validate the canonical Master chain; 
        '''
        chain_ = self.load_master_chain(new_master)
        for i in chain_.keys():
            block_key = chain_.get(i)['previous_hash']
            prev_block = chain_.get(block_key)
            encoded_block = json.dumps(prev_block).encode()
            hashed_block = ''.join(('0x', hashlib.sha256(encoded_block).hexdigest()))
            if block_key == hashed_block:
                pass
            elif i == list(chain_.keys())[0]:
                pass
            else:
                print(f'\n!!Err Bad block on Master. [{i}] !! \n')
                raise Exception
        if new_master != None:
            if new_master.items() == chain_.items() or len(new_master) == len(chain_) + 1:
                if print_it is True:
                    self.update_master_chain(new_master, print_it=True)
                else:
                    self.update_master_chain(new_master)
            else:
                # if print_it is True:
                print("!!Hey [not on master]  !!")
                if self.sync_mc is True:
                    u_input = input("Sync chain to master? (Y/n) \n: ").casefold()
                    if u_input in ['y', 'yes', '']:
                        self.sync_to_master()
                    else:
                        u_input = input("Are you sure you would like to skip master_sync? (Y/n) \n: ").casefold()
                        if u_input in ['y', 'yes', '']:
                            self.sync_mc = False
                        else:
                            self.sync_to_master()

        if print_it is True:
            print("!!Hey [master valid]  !!")

