#!/usr/bin/env python3



import json, time, os
from random import randint
from modules.chain_ctl.Minter import Minter_, ez_random, No_fun
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Block import Block_
from modules.chain_ctl.Proof_of_Work import Proof_of_Work
from modules.chain_ctl.Transactions import Wallet_
# from modules.chain_ctl.No_funs import No_fun



chain_menu = (
    "[Mine a Block]",
    "[Print Chain]",
    "[Print Chain]",
    "[Print Chain]",
    "[Print Chain]",
    "[Print Chain]",
    "[Print Chain]",
    "[Print Chain]",

)        

'''
    Minter
    Mine One Custom
    Mine empty blocks
    Print data
    Nuke chain

'''
class Timer:
    def __init__(self) -> None:
        self.start_time = float
    def start_timer(self):
        self.start_time = time.time()
        return self.start_time
    def end_timer(self):
        return round(time.time() - self.start_time, 2)
timer = Timer()


global CHAIN, CHAIN_ID, PROOF_OF_WORK, MINTER, WALLET
CHAIN:Blockchain_
CHAIN_ID:int
PROOF_OF_WORK:Proof_of_Work 
MINTER:Minter_
WALLET:Wallet_

def wallet_login():
    global WALLET
    try:
        with open(f"{os.getcwd()}/user_data/wallet.json", "r") as file:
            wallet = dict(json.load(file))
            w_keys = [*wallet]
            WALLET = Wallet_(
                wallet[w_keys[0]]['root_b'], 
                wallet[w_keys[0]]['balance'], 
                {},
                wallet[w_keys[0]]['inv_data'],
                w_keys[0],
                wallet[w_keys[0]]['rec_hash'],
                wallet[w_keys[0]]['sign_hash'],
                wallet[w_keys[0]]['txn_hist'],
                False
                )
    except FileNotFoundError:
        print("New Wallet")
        WALLET = Wallet_(CHAIN.get_tallest_block()[1], 0, {}, {}, True)
        WALLET.store_wallet()


def chain_info():
    pass

def minter_init():


    print("""-- Welcome to the No_fun::Minter

    No_funs are a very basic implementation of NFTs or Non-Fungible Tokens...
        with every iteration you have the chance to land a No_fun...
        ... and in turn, mine a block into the current chain!
        ... No_funs carry traits with a chance to land a rare void state.
        
        Currently all No_funs are written into blocks::chain_data with that 
        expected to change upon the implementation of txns and $DIRT.
        
        All Minter_data can be found in the [minter_data] directory once a 
        minter has been initialized along with your respective Chain_data
        files in the [chain_data] directory.

                                                    -- Dirt_Ranch_mgmt
    
    """)
    global CHAIN, CHAIN_ID, MINTER, WALLET
    u_input_q = input("Single Iteration Lotto..? \n (single iter_, no minter_logs) \n(y/N): ").casefold()
    if u_input_q in ['Y', 'y', 'yes']:
        MINTER = Minter_(CHAIN, WALLET.address_, quick=True)
        MINTER.generator()
        chain_init(CHAIN.chain_id)
    else:
        u_input_n = str(input("Enter a minter_name.. \n  default: Minter \n: "))
        u_input_i = input("Enter desired iterations.. \n  default: 16000 \n: ")
        if u_input_n == '':
            u_input_n = 'Minter'

        if u_input_i == '':
            u_input_i = 16000
        else:
            try:
                u_input_i = int(u_input_i)
                if u_input_i == 0:
                    u_input_i = 1
            except ValueError:
                u_input_i = 16000

        MINTER = Minter_(CHAIN, WALLET.address_, u_input_n, u_input_i)
        MINTER.generator()
        MINTER.update_history_json()
        MINTER.history_counts()

        print("\n\n-- [end] --\n\nCHAIN: " ,json.dumps(CHAIN.chain, indent=2))
        print("HEIGHT: ", len(CHAIN.chain))

        chain_init(CHAIN.chain_id)
    pass

def pow_init():
    pass

def chain_init(chain_id:int):
    global CHAIN, CHAIN_ID
    CHAIN_ID = chain_id 
    CHAIN = Blockchain_(CHAIN_ID)
    wallet_login()

    print("""Where to next?
        1. Chain Info
        2. Block Miner
        3. No_fun Minter
    """)
    u_input = int(input(": "))
    if u_input == 1:
        # print(json.dumps(CHAIN.join_data(WALLET.gen_wallet()), indent=2))
        chain_datas, all_txns, txn_splits, invent_splits = CHAIN.join_data(WALLET.gen_wallet())
        print(json.dumps(chain_datas, indent=2))
        print(json.dumps(all_txns, indent=2))
        print(json.dumps(txn_splits, indent=2))
        print(json.dumps(invent_splits, indent=2))

    elif u_input == 2:
        pow_init(CHAIN)
    elif u_input == 3:
        minter_init()

    else:
        chain_init(CHAIN_ID)

def dirt_ranch_welcome():
    print("-- Welcome to Dirt_Ranch, which wagon you ridin' today?")
    print('''
        1. Enter Chain_id
        2. Default on Master (chain_id=0)

        0. Advanced_Mode_Autorun
    ''')
    u_input = int(input(": "))
    if u_input == 1:
        u_input = input("chain_id: #")
        chain_init(u_input)
    elif u_input == 2:
        chain_init(0)

    elif u_input == 0:
        wallet_login()
        # running defaults to genesis
        global CHAIN, CHAIN_ID, MINTER, PROOF_OF_WORK
        CHAIN_ID = 0
        CHAIN = Blockchain_(CHAIN_ID)
        MINTER = Minter_(CHAIN)
        PROOF_OF_WORK = Proof_of_Work(CHAIN, '_')

        MINTER.generator()
        MINTER.update_history_json()
        MINTER.history_counts()

        print("\n\n-- [end] --\n\nCHAIN: " ,json.dumps(CHAIN.chain, indent=2))
        print("HEIGHT: ", len(CHAIN.chain))

    pass




def main():
    dirt_ranch_welcome()
    # bc = Blockchain_(99)
    # work = Proof_of_Work(bc)
    # minter = Minter_(bc, iters_=120000)
    # minter.generator()
    # # minter.check_for_uniques()
    # minter.update_history_json()
    # minter.history_counts()
    # print("\n\n-- [end] --\n\nCHAIN: " ,json.dumps(bc.chain, indent=2))
    # print("HEIGHT: ", len(bc.chain))
    # print(bc.hash_chain_())
    # # work.mine_block(txns=["FAKER hehe :)", "8==D"], chain_data={"Im_data": "Liar, he's a my key, IM data... maybe we're both data..."})
    # # print(bc.hash_chain_())
    # test = ez_random().get_()
    # print(test)
    # bl = Block_(0,"0xsomestringshehe", 13, [], "stresfd", {})
    # bc.append_block_(bl)
    # timer.start_timer()
    # work.mine_block(bc)
    # work.mine_block(bc)
    # work.mine_block(bc)
    # i = 0
    # while i < 10:
    #     work.mine_block(bc)
    #     i+=1
    # print("TIME: " ,timer.end_timer(), "sec")

    # menu.main_menu_()
    # ri = randint(0, 9999)
    # nf = No_fun(ri)
    # checks_ = nf.get_attrs()

    # work.mine_block(txns=["some", "testing :)"], chain_data=checks_)
    

main()
