#!/usr/bin/env python3

import json, time, os
from random import randint
from modules.chain_ctl.Minter import Minter_, ez_random, No_fun
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Block import Block_
from modules.chain_ctl.Proof_of_Work import Proof_of_Work
from modules.chain_ctl.Transactions import Wallet_
from modules.chain_ctl.Miner import Auto_Miner_
global CHAIN, CHAIN_ID, PROOF_OF_WORK, MINER, MINTER, WALLET
CHAIN:Blockchain_
CHAIN_ID:int
PROOF_OF_WORK:Proof_of_Work
MINER:Auto_Miner_ 
MINTER:Minter_
WALLET:Wallet_

from tkinter import *
from tkinter import ttk
root = Tk()

class FeetToMeters:
    def __init__(self, root):
        root.title("Feet to Meters")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)
        
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass

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



        




# FeetToMeters(root)
DisplayCurrentBlock(root)
root.mainloop()