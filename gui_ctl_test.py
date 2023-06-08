#!/usr/bin/env python3

import json
import tkinter as tk
from tkinter import ttk

from ttkbootstrap import Style

from ctl_center import wallet_quick_login
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Miner import Auto_Miner_
from modules.chain_ctl.Minter import Minter_
from modules.chain_ctl.Proof_of_Work import Proof_of_Work
from modules.chain_ctl.Transactions import Wallet_

global CHAIN, CHAIN_ID, PROOF_OF_WORK, MINER, MINTER, WALLET
CHAIN: Blockchain_
CHAIN_ID: int
PROOF_OF_WORK: Proof_of_Work
MINER: Auto_Miner_
MINTER: Minter_
WALLET: Wallet_


def chain_init(chain_id: int = 0):
    global CHAIN, CHAIN_ID, WALLET
    CHAIN_ID = chain_id
    CHAIN = Blockchain_(CHAIN_ID)
    wallet_quick_login()


def center_tkscreen(root, width, height) -> str:
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    return f"{width}x{height}+{x}+{y}"


def create_layout(frame, menu_widgets: dict):
    frame.columnconfigure(0, weight=1, uniform="base", minsize=25)
    frame.columnconfigure(1, weight=2, uniform="a")
    frame.columnconfigure(2, weight=1, uniform="base", minsize=25)
    frame.rowconfigure(0, weight=1, uniform="a")

    for i, key in enumerate(menu_widgets.keys()):
        if type(menu_widgets[key]) == ttk.Label:
            menu_widgets[key].grid(row=0, column=0, sticky="nsew", columnspan=3)
        else:
            menu_widgets[key].grid(row=i + 1, column=1, sticky="ew", columnspan=1)


class Office(ttk.Frame):
    def __init__(self, parent, switch):
        super().__init__(parent, relief="solid", padding=5)
        self.grid(row=1, column=1, sticky="nsew")
        self.switch = switch

        global WALLET
        WALLET = wallet_quick_login()
        chain_datas, all_txns, txn_splits, invent_splits = CHAIN.join_data(WALLET.gen_wallet())
        CHAIN.user_journal_update()
        out_data = {
            "TRANSACTIONS": all_txns,
            "CHAIN_DATA": chain_datas,
            "INVENTORY": invent_splits,
            "BALANCES": txn_splits
        }
        block_frame = tk.Text(self, width=80)
        block_frame.grid(row=1, column=0, sticky="nsew")

        scroll = tk.Scrollbar(self, command=block_frame.yview)
        scroll.grid(row=1, column=1, sticky="ns")

        block_frame.configure(yscrollcommand=scroll.set)
        for key, value in out_data.items():
            block_frame.insert("end", f"\n\n---------------->\n{key}\n")
            block_frame.insert("end", json.dumps(value, indent=4))

        close_btn = ttk.Button(self, text="X", command=self.close_frame)
        close_btn.grid(row=1, sticky="nw")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid(row=1, column=1, columnspan=1)

    def close_frame(self):
        self.switch(Menu)
        self.destroy()


class DirtRanch_Welcome(ttk.Frame):
    def __init__(self, parent, switch):
        super().__init__(parent, relief="solid", padding=10)
        self.switch = switch
        self.grid(row=1, column=1, sticky="nsew")
        create_layout(self, self.create_widgets())
        print(self.switch)

    def create_widgets(self) -> dict:
        menu_heading = ttk.Label(
            self,
            text="-- Welcome to dirt_Ranch^_ ..!\n\n Which wagon you ridin' today?\n",
            font="Courier 22",
            padding=2,
        )
        menu_button_1 = ttk.Button(
            self, text="Enter Chain_id", command=self.enter_chain
        )
        menu_button_2 = ttk.Button(
            self, text="Master::chain_id=0 (default)", command=self.default_chain
        )
        menu_button_3 = ttk.Button(self, text="Advanced_Mode_Autorun")
        menu_button_0 = ttk.Button(self, text="Exit")

        menu_widgets = {
            "heading": menu_heading,
            "1": menu_button_1,
            "2": menu_button_2,
            "3": menu_button_3,
            "0": menu_button_0,
        }

        return menu_widgets

    def enter_chain(self):
        entry_int = tk.IntVar()
        chain_entry = ttk.Entry(self, textvariable=entry_int)
        chain_entry.grid(row=0, column=0)

        def handle_return(event):
            entry_value = entry_int.get()
            chain_init(entry_value)
            self.switch_frame()

        chain_entry.bind("<Return>", handle_return)
        self.wait_variable(entry_int)

    def default_chain(self):
        chain_init(0)
        self.switch_frame()

    def switch_frame(self):
        self.switch(Menu)


class Menu(ttk.Frame):
    def __init__(self, parent, switch):
        super().__init__(parent, relief="solid", padding=5)
        self.switch = switch
        self.place(anchor="center", relx=0.5, rely=0.5, relwidth=0.3)
        create_layout(self, self.create_widgets())
        print(self.switch)

    def create_widgets(self) -> dict:
        menu_heading = ttk.Label(
            self, text="Where to next?", font="Calibri 22", padding=2
        )
        menu_button_1 = ttk.Button(
            self, text="Office", command=self.to_office
        )
        menu_button_2 = ttk.Button(
            self, text="Workshop"
        )
        menu_button_3 = ttk.Button(self, text="Crafting Bench")
        menu_button_4 = ttk.Button(self, text="Throw $DIRT")
        menu_button_5 = ttk.Button(self, text="Trading Post")
        menu_button_6 = ttk.Button(self, text="Message Board")
        menu_button_7 = ttk.Button(self, text="The Mound")
        menu_button_8 = ttk.Button(self, text="The Pit")
        menu_button_9 = ttk.Button(self, text="Wallet Options")
        menu_button_0 = ttk.Button(self, text="Exit")

        menu_widgets = {
            "heading": menu_heading,
            "1": menu_button_1,
            "2": menu_button_2,
            "3": menu_button_3,
            "4": menu_button_4,
            "5": menu_button_5,
            "6": menu_button_6,
            "7": menu_button_7,
            "8": menu_button_8,
            "9": menu_button_9,
            "0": menu_button_0,
        }

        return menu_widgets

    def to_office(self):
        self.switch(Office)


class Single_Block(ttk.Frame):
    def __init__(self, parent, chain_id: int = 0):
        super().__init__(parent, relief="solid", padding=5)
        close_btn = ttk.Button(self, text="X", command=self.close_frame)
        close_btn.grid(row=0, sticky="nw")
        self.grid(row=1, column=0)

        chain: Blockchain_ = CHAIN
        chain.validate_chain()
        top_block, _ = chain.get_tallest_block()

        block_frame = tk.Text(self, width=120, height=120)

        block_frame.grid()
        block_frame.insert(1.0, json.dumps(top_block, indent=2))

    def close_frame(self):
        self.destroy()


class App(tk.Tk):
    def __init__(self):
        # init
        super().__init__()
        Style(theme="darkly")
        self.title("Blockchain.py")
        geo = center_tkscreen(self, 800, 600)
        self.geometry(geo)

        # widgets
        self.current_frame = None
        self.switch_frame(DirtRanch_Welcome)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self, self.switch_frame)

        if self.current_frame is not None:
            self.current_frame.destroy()

        new_frame.grid(row=1, column=1, sticky="nsew")
        border_size = 25
        self.grid_rowconfigure(0, weight=1, minsize=border_size)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1, minsize=border_size)
        self.grid_columnconfigure(0, weight=1, minsize=border_size)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1, minsize=border_size)

        self.current_frame = new_frame


# start app
app = App()
app.mainloop()