import json
import os

from modules.chain_ctl import Proof_of_Work
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Miner import Auto_Miner_
from modules.chain_ctl.Minter import Minter_
from modules.chain_ctl.Transactions import Wallet_

global CHAIN, CHAIN_ID, PROOF_OF_WORK, MINER, MINTER, WALLET
CHAIN: Blockchain_
CHAIN_ID: int
PROOF_OF_WORK: Proof_of_Work
MINER: Auto_Miner_
MINTER: Minter_
WALLET: Wallet_


def chain_init(chain_id: int, print_it: bool = True):
    global CHAIN, CHAIN_ID
    CHAIN_ID = chain_id
    CHAIN = Blockchain_(CHAIN_ID, print_it)

    return CHAIN


def get_chain_string() -> str:
    try:
        return json.dumps(CHAIN.chain, indent=2)
    except NameError:
        return "No chain initialized."


def get_wallet_string() -> str:
    try:
        WALLET.gen_wallet()
        return json.dumps(WALLET.wallet_, indent=2)
    except NameError:
        return "No wallet initialized."


def get_joined_data():
    chain_datas, all_txns, txn_splits, invent_splits = CHAIN.join_data(
        WALLET.gen_wallet()
    )
    CHAIN.user_journal_update()
    output = f"""
        ============================= =============================
        
        
{json.dumps(all_txns, indent=2)}
        ==================   All Transactions    ==================
        
        
{json.dumps(chain_datas, indent=2)}
        ==================    All Chain Data     ==================
        
        
{json.dumps(invent_splits, indent=2)}
        ================== Wallet Inventory List ==================
        
        
{json.dumps(txn_splits, indent=2)}
        ==================   Balances::Ledger    ==================

        -- The file cabinet fell over... sections are labeled from the bottom...
            I tried my best to put the most important stuff last... 
            ... let's hope it stayed that way...
    
        ============================= =============================
    """
    chain_init(CHAIN_ID)

    return output


def wallet_quick_login(new_=False, w_index: int = 0) -> Wallet_:
    global WALLET
    try:
        with open(f"{os.getcwd()}/user_data/wallet.json", "r") as file:
            wallet = dict(json.load(file))
            w_keys = [*wallet]
            WALLET = Wallet_(
                wallet[w_keys[w_index]]["root_b"],
                wallet[w_keys[w_index]]["$DIRT"],
                {},
                wallet[w_keys[w_index]]["inv_data"],
                w_keys[w_index],
                wallet[w_keys[w_index]]["rec_hash"],
                wallet[w_keys[w_index]]["sign_hash"],
                wallet[w_keys[w_index]]["txn_hist"],
                wallet[w_keys[w_index]]["chains"],
                False,
            )
    except FileNotFoundError:
        print("New Wallet")
        WALLET = Wallet_(CHAIN.genesis_b)
        WALLET.store_wallet()

    if new_ is True:
        print("New Wallet")
        WALLET = Wallet_(CHAIN.genesis_b)
        WALLET.store_wallet()
        wallet_quick_login(w_index=len(WALLET.print_wallets(False)) - 1)

    return WALLET


def wallet_login():
    global WALLET
    wallet_quick_login()
    print("Which wallet would you like to use?")
    i = 0
    for wallet in WALLET.print_wallets(False):
        print(f"{i}. {wallet}")
        i += 1
    u_input = input(": ")
    try:
        wallet_quick_login(False, int(u_input))
    except ValueError:
        print("Integer value required, using default. (0)")
        wallet_quick_login()


def auto_miner():
    global CHAIN, CHAIN_ID, MINER, WALLET
