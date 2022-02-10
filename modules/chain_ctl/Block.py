import datetime, json, hashlib



class Block_:
    def __init__(self,
        index: int,
        previous_hash: str,
        nonce: int,
        txns: list,
        signature: str,
        chain_data: dict,
    ) -> tuple:
        self.block = {
            'index': index,
            'time': str(datetime.datetime.now()),
            'chain_data': chain_data,
            'signature': signature,
            'transactions': txns,
            'nonce': nonce,
            'previous_hash': previous_hash
            } 

        self.block_hash = self.hash_block_()

        
    def return_data(self):
        print("Hello from class Block_ \n  START PRINTS \nBLOCK: ", self.block)
        print("INDEX: ", self.block['index'])
        print("BLOCK_HASH: ", self.block_hash)
        print("  END PRINTS \n")
        return {self.block_hash: self.block}


    def hash_block_(self) -> str:
        '''
        Hash a block and return the cryptographic hash value of the block

        convert a string -> bytes and return encrypted hash
        '''
        encoded_block = json.dumps(self.block).encode()
        return ''.join(('0x', hashlib.sha256(encoded_block).hexdigest()))
        