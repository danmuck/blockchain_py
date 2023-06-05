#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

import json, time, os
from random import randint
from modules.chain_ctl.Minter import Minter_, ez_random, No_fun
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Block import Block_
from modules.chain_ctl.Proof_of_Work import Proof_of_Work
from modules.chain_ctl.Transactions import Wallet_
from modules.chain_ctl.Miner import Auto_Miner_
global CHAIN, CHAIN_ID, PROOF_OF_WORK, MINER, MINTER, WALLET

CHAIN: Blockchain_
CHAIN_ID: int
PROOF_OF_WORK: Proof_of_Work
MINER: Auto_Miner_
MINTER: Minter_
WALLET: Wallet_

root = Tk()


class DisplayCurrentBlock:
    def __init__(self, root) -> None:
        root.title('Block Height')

        global CHAIN, CHAIN_ID
        CHAIN_ID = 0
        CHAIN = Blockchain_(CHAIN_ID)
        CHAIN.validate_chain()

        block_frame = ttk.Frame(root, padding='4 4 8 8')
        block_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.block_data = StringVar()
        self.block_height = StringVar()

        block_print = ttk.Label(block_frame).grid(column=0, row=0)

        block_print['textvariable'] = self.block_data
        self.block_data.set("ajksdhfkjashdfkj")

        for child in block_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)


DisplayCurrentBlock(root)
root.mainloop()
