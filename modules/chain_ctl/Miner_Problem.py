




def miner_problem_(new_nonce: int, previous_nonce: int, index: str, data: str) -> bytes:
    # make more difficult
    miner_problem = str(new_nonce ** 2 - previous_nonce ** 2 + index) + data

    return miner_problem.encode()