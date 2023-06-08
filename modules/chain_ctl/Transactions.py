import json, hashlib, datetime, os
from random import randint
from .Shifter import shifter_

REC_OPTS = [
    "dog",
    "cat",
    "bird",
    "mouse",
    "leopard",
    "jaguar",
    "panther",
    "cheetah",
    "bobcat",
    "tomcat",
    "lion",
    "tiger",
    "liger",
    "bengal",
    "tabby",
    "fox",
    "fenix",
    "bear",
    "polarbear",
    "grizzly",
    "panda",
    "koala",
    "klondike",
    "scarecrow",
    "tinman",
    "dorothy",
    "munchkin",
    "todo",
    "emerald",
    "ruby",
    "diamond",
    "sapphire",
    "topaz",
    "amethyst",
    "malachite",
    "parrot",
    "songbird",
    "cardinal",
    "bluejay",
    "jay",
    "hawk",
    "eagle",
    "robyn",
    "snake",
    "boa",
    "constrictor",
    "python",
    "rattlesnake",
    "kingsnake",
    "viper",
    "canine",
    "retriever",
    "sloth",
    "opossum",
    "raccoon",
    "squirrel",
    "groundhog",
    "beaver",
    "dirtpig",
    "pig",
    "cow",
    "horse",
    "hen",
    "chicken",
    "chick",
    "rooster",
    "llama",
    "camel",
    "alpaca",
    "farm",
    "city",
    "state",
    "country",
    "usa",
    "canada",
    "england",
    "spain",
    "germany",
    "france",
    "sweden",
    "norway",
    "iceland",
    "greenland",
    "mexico",
    "argentina",
    "panama",
    "japan",
    "korea",
    "china",
    "ukraine",
    "russia",
    "australia",
    "newzealand",
    "malasia",
    "egypt",
    "madagascar",
    "africa",
    "israel",
    "turkey",
    "mono",
    "di",
    "tri",
    "tetra",
    "penta",
    "hexa",
    "hepta",
    "octo",
    "ennea",
    "deca",
    "monkey",
    "gorilla",
    "baboon",
    "book",
    "page",
    "leather",
]


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
        init_txn: dict = {},
        inv_data={},
        address=None,
        rec_hash=None,
        sign_hash=None,
        txn_hist=[],
        new_=True,
    ) -> None:
        if new_ is not True:
            self.address_ = address
            self.recover_hash = rec_hash
            self.signer_hash = sign_hash
            self.txn_hist = txn_hist
            self.root_b = root_b
            self.balance = balance
            self.inv_data = inv_data
        else:
            self.recover_hash = None
            self.signer_hash = None
            self.txn_hist = []
            self.root_b = root_b
            self.balance = balance
            self.inv_data = inv_data
            self.address_ = self.init_wallet()
        self.txn_hist.append(init_txn)

        self.wallet_: dict = {}

    def init_wallet(self) -> str:
        hash_r, list_ = self.gen_recovery()
        hash_p, pass_ = self.set_signer()

        encoded_addr = json.dumps("_".join([hash_r, hash_p, self.root_b])).encode()
        hash_ = shifter_("".join(("0x", hashlib.sha256(encoded_addr).hexdigest())))
        self.address_ = hash_
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
            print("Signer Password:", pass_)
            i = 1
            for word in list_:
                print("  ", i, word)
                i += 1

        return hash_

    def gen_wallet(self) -> dict:
        wallet_ = {
            self.address_: {
                "sign_hash": self.signer_hash,
                "$DIRT": self.balance,
                "inv_data": self.inv_data,
                "txn_hist": self.txn_hist,
                "rec_hash": self.recover_hash,
                "root_b": self.root_b,
            }
        }
        self.wallet_ = wallet_
        return wallet_

    def new_txn(self):
        pass

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

    def set_signer(self):
        password = input("Enter a sign_pass: ")
        encoded_pass = json.dumps(password).encode()
        hash_ = shifter_("".join(("0x", hashlib.sha256(encoded_pass).hexdigest())))
        if self.signer_hash is None:
            self.signer_hash = hash_
        # print(password, hash_)
        return hash_, password

    def print_wallets(self, print_=True) -> list[str]:
        with open(f"{os.getcwd()}/user_data/wallet.json", "r") as file:
            wallet = dict(json.load(file))
            w_keys = [*wallet]
        if print_ is True:
            print(w_keys)
        return w_keys

    def recover_wallet(self, o_chain_g: str):
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


class Txn_:
    to_addr: str
    from_addr: str
    txn_data: dict
    amount: float
    miner_fee: float
    timestamp: str
    type_: str

    txn_hash: str
    final_txn: dict

    def __init__(self, to_addr, from_addr, txn_data, amount, miner_fee, type_) -> None:
        self.to_addr = to_addr
        self.from_addr = from_addr
        self.txn_data = txn_data
        self.amount = amount
        self.miner_fee = miner_fee
        self.type_ = type_
        self.timestamp = str(datetime.datetime.now())

        self.raw_txn = {
            "to": self.to_addr,
            "from": self.from_addr,
            "data": self.txn_data,
            "amt": self.amount,
            "fee": self.miner_fee,
            "type": self.type_,
            "time": self.timestamp,
        }
        self.txn_finalize()

    def txn_in_validator(self):
        pass

    def txn_out_validator(self):
        pass

    def txn_finalize(self):
        self.txn_hash = self.hash_txn_(self.raw_txn)
        self.final_txn = {self.txn_hash: self.raw_txn}
        if self.type_ not in ["reward"]:
            return {}
        return self.final_txn

    def txn_compression(self):
        pass

    def hash_txn_(self, raw_txn: dict) -> str:
        """
        Hash a txn and return the cryptographic hash value of the txn
            convert a string -> bytes and return encrypted hash
        """
        encoded_txn = json.dumps(raw_txn).encode()
        return shifter_("".join(("0x", hashlib.sha256(encoded_txn).hexdigest())))
