import hashlib
import json
import os
from random import randint
from typing import Any

from modules.chain_ctl.utilities.Debug import DEBUG_MODE
from modules.chain_ctl.wallet.Recovery_Options import REC_OPTS
from modules.chain_ctl.utilities.Shifter import shifter_


class Wallet_:
    address_: str
    root_b: str
    balance: float
    txn_hist: list
    inv_data: dict

    recover_hash: str
    signer_hash: str
    wallet_: dict

    f_curr: dict

    def __init__(
        self,
        root_b: str,
        balance: float = 0,
        inv_data: dict = None,
        address: str = None,
        rec_hash: str = None,
        sign_hash: str = None,
        txn_hist: list = None,
        chains: list = None,
        init_txn: dict = None,
    ) -> None:
        self.root_b = root_b
        self.balance = balance
        self.address_ = address
        self.recover_hash = rec_hash
        self.signer_hash = sign_hash
        self.txn_hist = txn_hist
        self.inv_data = inv_data
        self.chains = chains
        # self.txn_hist.append(init_txn)

        self.wallet_: dict = {}

    def gen_wallet(self) -> dict:
        wallet_ = {
            self.address_: {
                "sign_hash": self.signer_hash,
                "$DIRT": self.balance,
                "inv_data": self.inv_data,
                "txn_hist": self.txn_hist,
                "rec_hash": self.recover_hash,
                "root_b": self.root_b,
                "chains": [self.root_b],
            }
        }
        self.wallet_ = wallet_
        return wallet_

    def init_wallet(
        self, password: str = None
    ) -> tuple[str, str, tuple[str, ...]]:
        hash_r, pass_phrase_ = self.gen_recovery()

        if password is None:
            hash_p, password_ = self.set_signer()
        else:
            hash_p, password_ = self.set_signer(password)

        encoded_addr = json.dumps("_".join([hash_r, hash_p, self.root_b])).encode()
        hash_ = shifter_("".join(("0x", hashlib.sha256(encoded_addr).hexdigest())))

        self.address_ = hash_
        self.txn_hist = []
        self.inv_data = {}
        self.chains = []
        self.gen_wallet()

        return hash_, password_, pass_phrase_

    def gen_recovery(self):
        your_opts = []
        i = 1
        while len(your_opts) < 12:
            new_opt = REC_OPTS[randint(0, len(REC_OPTS) - 1)]
            if new_opt not in your_opts:
                your_opts.append(new_opt)
                print(i, new_opt)
                i += 1
        encoded_opts = json.dumps(your_opts).encode()
        hash_ = shifter_("".join(("0x", hashlib.sha256(encoded_opts).hexdigest())))
        if self.recover_hash is None:
            self.recover_hash = hash_
        # print(self.recover_hash, your_opts)
        return hash_, tuple(your_opts)

    def set_signer(self, sign_pass: str = "password"):
        password = sign_pass
        encoded_pass = json.dumps(password).encode()
        hash_ = shifter_("".join(("0x", hashlib.sha256(encoded_pass).hexdigest())))
        if self.signer_hash is None:
            self.signer_hash = hash_
        # print(password, hash_)
        return hash_, password

    def print_wallets(self) -> list[str]:
        with open(f"{os.getcwd()}/user_data/wallet.json", "r") as file:
            wallet = dict(json.load(file))
            w_keys = [*wallet]
        if DEBUG_MODE > 2:
            print(w_keys)
        return w_keys

    def recover_wallet(self, o_chain_g: str):
        if DEBUG_MODE > 2:
            pass  # ################################################################
        print(
            """"
            At each prompt, enter your recovery phrase in order, 1 word at a time..
                (next you will be prompted to enter your sign_pass)
            """
        )
        # wallet_addr = input("Enter the complete 66-character wallet_address: ")

        (
            one_,
            two_,
            three_,
            four_,
            five_,
            six_,
            sev_,
            eight_,
            nine_,
            ten_,
            elev_,
            twel_,
        ) = (
            input(": "),
            input(": "),
            input(": "),
            input(": "),
            input(": "),
            input(": "),
            input(": "),
            input(": "),
            input(": "),
            input(": "),
            input(": "),
            input(": "),
        )
        pass_ = input("sign_pass: ")

        hash_list = []
        for i in [
            one_,
            two_,
            three_,
            four_,
            five_,
            six_,
            sev_,
            eight_,
            nine_,
            ten_,
            elev_,
            twel_,
        ]:
            hash_list.append(i)

        encoded_r = json.dumps(hash_list).encode()
        hash_r = shifter_("".join(("0x", hashlib.sha256(encoded_r).hexdigest())))
        encoded_p = json.dumps(pass_).encode()
        hash_p = shifter_("".join(("0x", hashlib.sha256(encoded_p).hexdigest())))
        encoded_addr = json.dumps("_".join([hash_r, hash_p, o_chain_g])).encode()
        w_addr_ = shifter_("".join(("0x", hashlib.sha256(encoded_addr).hexdigest())))
        self.address_ = w_addr_
        self.balance = 0
        self.txn_hist = [{}]
        self.inv_data = {}
        self.recover_hash = hash_r
        self.signer_hash = hash_p
        wallet_ = self.gen_wallet()
        self.store_wallet()
        return wallet_, hash_r, hash_p, w_addr_

    def store_wallet(self):
        all_wall = {}
        try:
            os.mkdir(f"{os.getcwd()}/user_data/")
        # [bug]: this is almost certainly resulting in incorrect behaviour
        #       if a file called user_data exists, the directory is not created
        except FileExistsError:
            pass 
        try:
            with open(f"{os.getcwd()}/user_data/wallet.json", "x") as file:
                wallet_data = json.dumps(self.gen_wallet(), indent=2)
                file.write(wallet_data)
        except FileExistsError:
            try:
                with open(f"{os.getcwd()}/user_data/wallet.json", "r") as file:
                    wallets_ = dict(json.load(file))
                    items_ = [wallets_.items()]
                    for item in items_:
                        all_wall.update(item)
                with open(f"{os.getcwd()}/user_data/wallet.json", "w") as file:
                    new_wallet_ = self.gen_wallet()
                    all_wall.update(new_wallet_)
                    wallet_data = json.dumps(all_wall, indent=2)
                    file.write(wallet_data)
            except FileNotFoundError:
                pass

    def new_txn(self):
        pass
