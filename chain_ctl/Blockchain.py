import datetime, hashlib, json, os

from .Block import Block_

class Blockchain_:

    def __init__(self, chain_id:int) -> None:

        self.chain_id = chain_id
        self.chain = {}
        # self.chain = some_function_to_call_chain_data()

        self.genesis_block = Block_(
            index=0,
            previous_hash = "0x" + str(self.chain_id).zfill(64),
            nonce = 0,
            txns = [],
            signature = 'im the genesis block :)',
            chain_data = {},
        )
        self.chain.update((self.genesis_block.return_data()))
        print("\n\n  Hello from class Blockchain_\n  CHAIN: ",self.chain, "\n\n")

    def append_block_(self):
        pass

def main():
    bc = Blockchain_(0)
    print(bc)
main()