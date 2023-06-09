import datetime
import hashlib
import json

from modules.chain_ctl.utilities.Shifter import shifter_


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
