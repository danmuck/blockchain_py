import hashlib
import os
import time
from random import randint

from .Blockchain import Blockchain_, Block_
from modules.chain_ctl.utilities.Miner_Problem import miner_problem_
from .Transactions import Txn_
from .utilities.Debug import DEBUG_MODE

"""
    Timer for testing
"""


class Timer:
    def __init__(self) -> None:
        self.start_time = time.time()

    def start_timer(self):
        self.start_time = time.time()
        return self.start_time

    def end_timer(self):
        return round(time.time() - self.start_time, 2)


TIMER = Timer()


class Proof_of_Work:
    def __init__(
        self,
        chain_: Blockchain_,
        miner_wallet: str = None,
        pay_code: str = ""
        # txns=[],
        # chain_data={}
    ) -> None:
        self.difficulty = None
        self.chain_ = chain_
        self.chain_id = self.chain_.chain_id
        self.b_reward: float = 0
        self.pay_code = pay_code
        self.miner_wallet = miner_wallet
        if miner_wallet == "_" or len(miner_wallet) != 66 or miner_wallet is None:
            self.miner_wallet = self.chain_.genesis_b
        # self.txns = txns
        # self.chain_data = chain_data
        # self.difficulty = 0

    """
        Define the difficulty of the chain 
    """

    def proof_of_work_(
        self,
        previous_nonce: int,
        index: int,
        data: str,
    ) -> int:
        new_nonce = randint(1, previous_nonce + 500)
        check_nonce = False
        TIMER.start_timer()
        if DEBUG_MODE > 2:
            print(
                f"Timer started::fishing block: {len(self.chain_.chain) - 1} -> chain_height: {len(self.chain_.chain)}"
            )

        while not check_nonce:
            # print(new_nonce)
            hash_digest = miner_problem_(
                new_nonce=new_nonce,
                previous_nonce=previous_nonce,
                index=str(index),
                data=data,
            )
            hash_value = hashlib.sha256(hash_digest).hexdigest()

            if len(self.chain_.chain) == 1:
                self.difficulty = 0
                self.b_reward = 0
                check_nonce = True
            elif len(self.chain_.chain) < 500:
                self.difficulty = 1
                self.b_reward = 0
                if hash_value[:1] == "0":
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 1000:
                self.difficulty = 2
                self.b_reward = 1
                if hash_value[:2] == "00":
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 1500:
                self.difficulty = 3
                self.b_reward = 2
                if hash_value[:3] == "000":
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 2000:
                self.difficulty = 4
                self.b_reward = 4
                if hash_value[:4] == "0000":
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 2500:
                self.difficulty = 5
                self.b_reward = 8
                if hash_value[:5] == "00001":
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 30000:
                self.difficulty = 6
                self.b_reward = 16
                if hash_value[:6] == "000013":
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 60000:
                self.difficulty = 7
                self.b_reward = 32
                if hash_value[:7] == "0000133":
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 120000:
                self.difficulty = 8
                self.b_reward = 64
                if hash_value[:8] == "00001337":
                    check_nonce = True
                else:
                    new_nonce += 1
            else:
                self.difficulty = 9
                self.b_reward = 96
                if "hellofromdanmuck" in hash_value[:]:
                    check_nonce = True
                else:
                    new_nonce += 1
        if DEBUG_MODE > 2:
            print("MINE_TIME:", round(TIMER.end_timer(), 8), "sec")
            print("MINE_TIME:", f"{round(TIMER.end_timer() // 60, 8)}ish min")
            print("MINE_DIFF: lvl", self.difficulty)
        try:
            with open(
                f"{os.getcwd()}/chain_data/Block_times_{self.chain_id}.txt", "x"
            ) as file:
                file.write(
                    f"{str(TIMER.end_timer())}s\t\t: {self.difficulty} :: {self.b_reward} \n"
                )
        except FileExistsError:
            with open(
                f"{os.getcwd()}/chain_data/Block_times_{self.chain_id}.txt", "a+"
            ) as file:
                file.write(
                    f"{str(TIMER.end_timer())}s\t\t: {self.difficulty} :: {self.b_reward} \n"
                )

        return new_nonce

    """
        Convert floats to strings to avoid exponential notation when possible
    """

    def float_to_str(self, f):
        float_string = repr(f)
        if "e" in float_string:  # detect scientific notation
            digits, exp = float_string.split("e")
            digits = digits.replace(".", "").replace("-", "")
            exp = int(exp)
            zero_padding = "0" * (
                abs(int(exp)) - 1
            )  # minus 1 for decimal point in the sci notation
            sign = "-" if f < 0 else ""
            if exp > 0:
                float_string = "{}{}{}.0".format(sign, digits, zero_padding)
            else:
                float_string = "{}0.{}{}".format(sign, zero_padding, digits)
        return float_string

    """
        Define the block reward and apply any pay code modifiers
    """

    def b_reward_txn(self, miner_w: str, txn_data: dict = None):
        if self.pay_code == "0001":
            self.b_reward = self.b_reward * 1.18  # miner
        elif self.pay_code == "0010":
            self.b_reward = self.b_reward * 0.75  # minter
        else:
            self.b_reward = self.float_to_str(self.b_reward)
        self.b_reward = self.float_to_str(
            self.b_reward + (len(self.chain_.chain) * 0.0000016)
        )
        txn = Txn_(miner_w, self.chain_.genesis_b, txn_data, self.b_reward, 0, "reward")
        return txn.final_txn

    """
        Define the block itself and prepare it for appendage
            the mock block is irrelevant to the chain itself.
    """

    def mine_block(
        self, txns: dict = None, txn_data: dict = None, chain_data: dict = None
    ) -> Block_:
        wallet_address = self.miner_wallet

        previous_block = self.chain_.get_tallest_block()[0]
        previous_nonce = previous_block["nonce"]
        mock = Block_(
            index=0,
            previous_hash="",
            nonce=previous_nonce * 3,
            signature=f"MOCK_BLOCK_{randint(0, 69420)}",
            txns={},
            chain_data={},
        )
        previous_hash = mock.hash_block_(previous_block)
        index = len(self.chain_.chain)
        nonce = self.proof_of_work_(previous_nonce, index, str(mock))

        miner_sig: str
        if wallet_address is not None:
            miner_sig = wallet_address
            txn = self.b_reward_txn(miner_sig, txn_data)
            txns.update(txn)
        else:
            miner_sig = self.chain_.genesis_b
            txn = self.b_reward_txn(miner_sig, txn_data)
            txns.update(txn)

        block = Block_(
            index=index,
            previous_hash=previous_hash,
            nonce=nonce,
            signature=miner_sig,
            txns=txns,
            chain_data=chain_data,
        )

        self.chain_.append_block_(block)

        return block
