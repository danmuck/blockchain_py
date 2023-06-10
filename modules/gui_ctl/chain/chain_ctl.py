import json
import os

# from ctl_center import new_wallet
from modules.chain_ctl import Proof_of_Work
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.miner.Miner import Auto_Miner_
from modules.chain_ctl.minter.Minter import Minter_
from modules.chain_ctl.wallet.Wallet import Wallet_

global CHAIN, CHAIN_ID, PROOF_OF_WORK, MINER, MINTER, WALLET
CHAIN: Blockchain_
CHAIN_ID: int
PROOF_OF_WORK: Proof_of_Work
MINER: Auto_Miner_
MINTER: Minter_
WALLET: Wallet_

"""

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!            TEMPORARY                   !!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""


def new_wallet() -> (str, str):
    global WALLET
    WALLET = Wallet_(CHAIN.genesis_b)
    password = input("Enter a sign_pass: ")
    hash_, password_, pass_phrase_ = WALLET.init_wallet(password)

    print(
        f"""
       [ Ready to show password and passphrase for new wallet address:  ]

    !!   {hash_}

       [ This is the last time that you will see these so write them    ] 
       [     down in an appropriate place for safe keeping!!            ]

    """
    )
    u_input = input("Ready? (Y/n) \n: ").casefold()
    if u_input in ["y", "yes", ""]:
        print("Signer Password:", password_)
        i = 1
        for word in pass_phrase_:
            print("  ", i, word)
            i += 1

    input("\nPress Enter to continue\n: ")

    return hash_, password


"""

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!            TEMPORARY                   !!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""


def chain_init(chain_id: int):
    global CHAIN, CHAIN_ID
    CHAIN_ID = chain_id
    CHAIN = Blockchain_(CHAIN_ID)

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


def update_wallet_info():
    chain_datas, all_txns, txn_splits, invent_splits = CHAIN.join_data(
        WALLET.gen_wallet()
    )
    # CHAIN.update_user(txn_splits, invent_splits)
    CHAIN.user_journal_update()
    wallet_quick_login(address=WALLET.address_)


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


def wallet_quick_login(new_=False, address: str = "") -> Wallet_:
    global WALLET
    key_holder: list[str] = []
    try:
        with open(f"{os.getcwd()}/user_data/wallet.json", "r") as file:
            wallet = dict(json.load(file))
            key_holder = [*wallet]
            WALLET = Wallet_(
                wallet[address]["root_b"],
                wallet[address]["$DIRT"],
                wallet[address]["inv_data"],
                address,
                wallet[address]["rec_hash"],
                wallet[address]["sign_hash"],
                wallet[address]["txn_hist"],
                wallet[address]["chains"],
                {},
            )
    except FileNotFoundError:
        print("New Wallet")
        address, *_ = new_wallet()
        WALLET.store_wallet()
    except KeyError:
        wallet_quick_login(address=key_holder[0])

    if new_ is True:
        print("New Wallet")
        address, *_ = new_wallet()
        WALLET.store_wallet()
        wallet_quick_login(address=address)

    return WALLET


def wallet_login():
    """
        Update [WALLET.print_wallets] to return dict instead of list
    """
    global WALLET
    wallet_quick_login()
    print("Which wallet would you like to use?")
    i = 0
    login_dict = {}
    for wallet in WALLET.print_wallets():
        login_dict.update({f"{i}": wallet})
        print(f"{i}. {wallet}")
        i += 1
    u_input = input(": ")
    try:
        wallet_quick_login(False, login_dict.get(u_input))
    except ValueError:
        print("Integer value required, using default. (0)")
        wallet_quick_login()


def auto_miner(miner_name: str = "Miner", iters: int = 16):
    global CHAIN, CHAIN_ID, MINER, WALLET
    MINER = Auto_Miner_(CHAIN, WALLET.address_, miner_name, iters)
    MINER.generator()


def auto_minter(minter_name: str = "Minter", iters: int = 16000):
    global CHAIN, CHAIN_ID, MINTER, WALLET
    MINTER = Minter_(CHAIN, WALLET.address_, minter_name, iters)
    MINTER.generator()
    MINTER.update_history_json()
    MINTER.history_counts()
