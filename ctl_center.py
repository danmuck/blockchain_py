#!/usr/bin/env python3



import json, time, os
from random import randint
from modules.chain_ctl.Minter import Minter_, ez_random, No_fun
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Block import Block_
from modules.chain_ctl.Proof_of_Work import Proof_of_Work
from modules.chain_ctl.Transactions import Wallet_
from modules.chain_ctl.Miner import Auto_Miner_
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


global CHAIN, CHAIN_ID, PROOF_OF_WORK, MINER, MINTER, WALLET
CHAIN:Blockchain_
CHAIN_ID:int
PROOF_OF_WORK:Proof_of_Work
MINER:Auto_Miner_ 
MINTER:Minter_
WALLET:Wallet_

def wallet_quick_login(new_=False, w_index:int=0):
    global WALLET
    try:
        with open(f"{os.getcwd()}/user_data/wallet.json", "r") as file:
            wallet = dict(json.load(file))
            w_keys = [*wallet]
            WALLET = Wallet_(
                wallet[w_keys[w_index]]['root_b'], 
                wallet[w_keys[w_index]]['$DIRT'], 
                {},
                wallet[w_keys[w_index]]['inv_data'],
                w_keys[w_index],
                wallet[w_keys[w_index]]['rec_hash'],
                wallet[w_keys[w_index]]['sign_hash'],
                wallet[w_keys[w_index]]['txn_hist'],
                False
                )
    except FileNotFoundError:
        print("New Wallet")
        WALLET = Wallet_(CHAIN.genesis_b)
        WALLET.store_wallet()

    if new_ is True:
        print("New Wallet")
        WALLET = Wallet_(CHAIN.genesis_b)
        WALLET.store_wallet()
        wallet_quick_login(w_index=len(WALLET.print_wallets(False))-1)        

def wallet_login():
    global WALLET
    wallet_quick_login()
    print('Which wallet would you like to login with?')
    i = 0
    for wallet in WALLET.print_wallets(False):
        print(f'{i}. {wallet}')
        i+=1
    u_input = int(input(': '))
    try:
        u_input = int(u_input)
    except Exception:
        print('Integer value required, using default. (0)')
        wallet_quick_login()
    wallet_quick_login(False, u_input)

def wallet_recover():
    global WALLET
    WALLET = Wallet_(CHAIN.genesis_b, new_=False)
    WALLET.recover_wallet(CHAIN.genesis_b)
    wallet_quick_login(w_index=len(WALLET.print_wallets(False))-1)

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

                                                    -- dirt_Ranch^_mgmt
    
    """)
    global CHAIN, CHAIN_ID, MINTER, WALLET
    u_input_q = input("Single Iteration Lotto..? \n (single iter_, no minter_logs) \n(y/N): ").casefold()
    if u_input_q in ['Y', 'y', 'yes']:
        MINTER = Minter_(CHAIN, WALLET.address_, quick=True)
        MINTER.generator()
    else:
        u_input_n = str(input("Enter a minter_name.. \n  default: Minter \n: "))
        u_input_i = input("Enter desired iterations.. \n  default: 16000 \n: ")
        if u_input_n == '':
            u_input_n = 'Minter'

        if u_input_i == '':
            u_input_i = 16000
        else:
            try:
                u_input_i = u_input_i.lower().replace('k', '000', 1).replace('m', '000000', 1).replace('b', '000000000', 1)
                u_input_i = str(u_input_i).lower().strip('abcdefghijklmnopqrstuvwxyz')
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


def auto_miner_init():
    print("""-- Welcome to the Auto_Miner

    Auto-Mine a set number of blocks!
        
        All Minter_data can be found in the [minter_data] directory once a 
        minter has been initialized along with your respective Chain_data
        files in the [chain_data] directory.

                                                    -- dirt_Ranch^_mgmt
    
    """)
    global CHAIN, CHAIN_ID, MINER, WALLET
    u_input_q = input("Single Block..? \n(y/N): ").casefold()
    if u_input_q in ['Y', 'y', 'yes']:
        MINER = Auto_Miner_(CHAIN, WALLET.address_, quick=True)
        MINER.generator()
    else:
        u_input_n = str(input("Enter an Auto_Miner_name.. \n  default: Miner \n: "))
        u_input_i = input("Enter desired iterations.. \n  default: 16 \n: ")
        if u_input_n == '':
            u_input_n = 'Auto_Miner'
        if u_input_i == '':
            u_input_i = 16
        else:
            try:
                u_input_i = u_input_i.lower().replace('k', '000', 1).replace('m', '000000', 1).replace('b', '000000000', 1)
                u_input_i = str(u_input_i).lower().strip('abcdefghijklmnopqrstuvwxyz')
                u_input_i = int(u_input_i)
                if u_input_i == 0:
                    u_input_i = 1
            except ValueError:
                u_input_i = 16

        MINER = Auto_Miner_(CHAIN, WALLET.address_, u_input_n, u_input_i)
        MINER.generator()

        print("\n\n-- [end] --\n\nCHAIN: " ,json.dumps(CHAIN.chain, indent=2))
        print("HEIGHT: ", len(CHAIN.chain))

def wallet_opts():
    print('''
        1. Load current wallet.json
        2. New wallet

        0. Recover wallet on current chain.
    ''')
    u_input = input(": ")
    try:
        u_input = int(u_input)
    except Exception:
        pass
    if u_input == 1 or u_input == '':
        wallet_login()
    if u_input == 2:
        wallet_quick_login(True)        
    elif u_input == 0:
        wallet_recover()


def chain_init(chain_id:int):
    global CHAIN, CHAIN_ID
    CHAIN_ID = chain_id 
    CHAIN = Blockchain_(CHAIN_ID)
    wallet_login()

    print("""Where to next?
        1. Chain Info
        2. Wallet Options
        3. Auto_Miner
        4. No_fun Minter (default)

        0. Exit
    """)
    u_input = input(": ")
    try:
        u_input = int(u_input)
    except Exception:
        pass
    if u_input == 1:
        # print(json.dumps(CHAIN.join_data(WALLET.gen_wallet()), indent=2))
        chain_datas, all_txns, txn_splits, invent_splits = CHAIN.join_data(WALLET.gen_wallet())
        print("======================================================")
        print(json.dumps(chain_datas, indent=2))
        print("======================================================")
        print(json.dumps(all_txns, indent=2))
        print("======================================================")
        print(json.dumps(txn_splits, indent=2))
        print("======================================================")
        print(json.dumps(invent_splits, indent=2))
        print("======================================================")
        chain_init(CHAIN_ID)

    elif u_input == 2:
        wallet_opts()
        chain_init(CHAIN_ID)
    elif u_input == 3:
        auto_miner_init()
        chain_init(CHAIN_ID)
    elif u_input == 4 or u_input == '':
        minter_init()
        chain_init(CHAIN_ID)
    elif u_input == 0:
        exit()
    else:
        chain_init(CHAIN_ID)


def dirt_ranch_welcome():
    print("-- Welcome to dirt_Ranch^_, which wagon you ridin' today?")
    print('''
        1. Enter Chain_id
        2. Default on Master::chain_id=0 (default)
        3. Advanced_Mode_Autorun
        
        0. Exit

        99. TEST
    ''')
    u_input = input(": ")
    try:
        u_input = int(u_input)
    except Exception:
        pass
    if u_input == 1:
        u_input = input("chain_id: #")
        chain_init(u_input)
    elif u_input == 2 or u_input == '':
        chain_init(0)

    elif u_input == 3:
        wallet_quick_login()
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

    elif u_input == 0:
        exit()
    
    elif u_input == 99:
        wallet_quick_login()
        WALLET.print_wallets()
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
