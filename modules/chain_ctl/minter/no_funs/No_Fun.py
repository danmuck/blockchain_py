import datetime
import hashlib
import json
import math
import os
import time
from random import randint
from typing import Any

from modules.chain_ctl.utilities.Shifter import shifter_
from modules.chain_ctl.minter.no_funs.No_Fun_Utils import NO_FUN_LISTS, UNR_16_MAP

try:
    with open(f"{os.getcwd()}/minter_data/Minter_lists.json", "r") as minter_lists_file:
        jsonify = dict(json.load(minter_lists_file))
        OTHERS_LIST = jsonify["OTHERS_LIST"]
        UDBBLS_LIST = jsonify["UDBBLS_LIST"]
        UTRIPS_LIST = jsonify["UTRIPS_LIST"]
        UBINRS_LIST = jsonify["UBINRS_LIST"]
except FileNotFoundError:
    try:
        os.mkdir(f"{os.getcwd()}/minter_data")
    except FileExistsError:
        pass
    finally:
        with open(
            f"{os.getcwd()}/minter_data/Minter_lists.json", "x"
        ) as minter_lists_file:
            minter_lists_file.write(
                json.dumps(
                    NO_FUN_LISTS,
                    indent=2,
                )
            )
        with open(
            f"{os.getcwd()}/minter_data/Minter_lists.json", "r"
        ) as minter_lists_file:
            jsonify = dict(json.load(minter_lists_file))
            OTHERS_LIST = jsonify["OTHERS_LIST"]
            UDBBLS_LIST = jsonify["UDBBLS_LIST"]
            UTRIPS_LIST = jsonify["UTRIPS_LIST"]
            UBINRS_LIST = jsonify["UBINRS_LIST"]


class ez_random:
    def __init__(self) -> None:
        self.return_ = self.get_()

    def get_(self) -> int:
        small_chk = randint(1, 4096) + randint(0, 1)
        nanos_chk = (time.time_ns() + small_chk) * math.pi
        ez_nums = round(
            (nanos_chk * small_chk * small_chk) % 1023 * (0.000007 + randint(0, 1)),
            5,
        )
        ez_rand = ez_nums + randint(0, 9999)

        return round(ez_rand)


class No_fun:
    def __init__(self, ez_num: ez_random) -> None:
        self.ez_num = ez_num.return_
        self.attrs = {}
        self.hash_ = str
        self.time_ = str(datetime.datetime.now())
        if self.ez_num > 1234:
            self.void = True
        else:
            self.void = False

    def get_attrs(self) -> dict:
        ez_num_ = self.ez_num
        float_ = self.get_float()
        color_ = str
        border_ = str
        img_ = str
        spec_ = str
        trait_ = str
        void_ = str
        if self.void is True and ez_num_ > 15:
            color_ = "black"
            border_ = "black"
            void_ = "(V/O/I/D)"
            img_ = "[    ]"
            spec_ = self.get_colors()
        elif ez_num_ not in UBINRS_LIST:
            color_, border_, spec_ = self.get_colors()
            img_ = self.get_image()
            if self.void is not True:
                void_ = "(        )"
        else:
            void_ = "(        )"

        if ez_num_ in UBINRS_LIST:
            ez_num_ = UNR_16_MAP[ez_num_]
            trait_ = ".::$Bills::."
            if ez_num_ == "0000":
                color_ = "white"
                border_ = "white"
                spec_ = "cue"
                img_ = self.get_image()
            elif ez_num_ == "0001":
                color_ = "yellow"
                border_ = "yellow"
                spec_ = "solid"
                img_ = self.get_image()
            elif ez_num_ == "0010":
                color_ = "blue"
                border_ = "blue"
                spec_ = "solid"
                img_ = self.get_image()
            elif ez_num_ == "0011":
                color_ = "red"
                border_ = "red"
                spec_ = "solid"
                img_ = self.get_image()
            elif ez_num_ == "0100":
                color_ = "violet"
                border_ = "violet"
                spec_ = "solid"
                img_ = self.get_image()
            elif ez_num_ == "0101":
                color_ = "orange"
                border_ = "orange"
                spec_ = "solid"
                img_ = self.get_image()
            elif ez_num_ == "0110":
                color_ = "green"
                border_ = "green"
                spec_ = "solid"
                img_ = self.get_image()
            elif ez_num_ == "0111":
                color_ = "cyan"
                border_ = "cyan"
                spec_ = "solid"
                img_ = self.get_image()
            elif ez_num_ == "1000":
                color_ = "black"
                border_ = "black"
                spec_ = "eight"
                img_ = self.get_image()
            elif ez_num_ == "1001":
                color_ = "yellow"
                border_ = "yellow"
                spec_ = "stripe"
                img_ = self.get_image()
            elif ez_num_ == "1010":
                color_ = "blue"
                border_ = "blue"
                spec_ = "stripe"
                img_ = self.get_image()
            elif ez_num_ == "1011":
                color_ = "red"
                border_ = "red"
                spec_ = "stripe"
                img_ = self.get_image()
            elif ez_num_ == "1100":
                color_ = "violet"
                border_ = "violet"
                spec_ = "stripe"
                img_ = self.get_image()
            elif ez_num_ == "1101":
                color_ = "orange"
                border_ = "orange"
                spec_ = "stripe"
                img_ = self.get_image()
            elif ez_num_ == "1110":
                color_ = "green"
                border_ = "green"
                spec_ = "stripe"
                img_ = self.get_image()
            elif ez_num_ == "1111":
                color_ = "cyan"
                border_ = "cyan"
                spec_ = "stripe"
                img_ = self.get_image()
            else:
                color_ = "borked"
                border_ = "borked"
                spec_ = "borked"
                img_ = f"[{ez_num_}]"

        elif ez_num_ in OTHERS_LIST:
            ez_num_ = str(ez_num_)
            trait_ = ".:Rare:."
        elif ez_num_ in UDBBLS_LIST:
            ez_num_ = str(ez_num_)
            trait_ = ".:Dubbs:."
        elif ez_num_ in UTRIPS_LIST:
            ez_num_ = str(ez_num_)
            trait_ = ".:Trippps:."
        elif 999 < ez_num_ <= 1234:
            ez_num_ = str(ez_num_)
            trait_ = ".unCommon."
        elif ez_num_ > 1234:
            ez_num_ = str(ez_num_)
            if trait_ != "":
                trait_ = "".join(["(V/O/", trait_, "/I/D)"])
            else:
                trait_ = "::(V/O/I/D)::"
        else:
            ez_num_ = str(ez_num_)
            trait_ = "Common"

        void_attrs: dict = {
            "num": str(ez_num_),
            "trait": str(trait_),
            "float": str(float_),
            "color": str(color_),
            "border": str(border_),
            "img": str(img_),
            "special": str(spec_),
            "void": str(void_),
        }
        void_hash: str = self.hash_it(void_attrs)
        final_void: dict = {void_hash: void_attrs}
        self.hash_ = void_hash
        self.attrs = void_attrs
        return final_void

    def hash_it(self, attrs_: dict) -> str:
        attrs_t = {"time": self.time_}
        attrs_t.update(attrs_)
        encoded_data = json.dumps(attrs_t).encode()
        return shifter_("".join(("0x", hashlib.sha256(encoded_data).hexdigest())))

    def get_float(self) -> str:
        float_ = randint(0, 100000000)
        if float_ >= 99999985 or float_ <= 15 or self.void is True:
            float_ = "VOID"
            self.void = True
            return float_
        else:
            float_ = "." + f"{float_}".zfill(8)
            return float_

    def get_colors(self) -> tuple[str | Any, str | Any, str]:
        bg_ = [
            "Black",
            "White",
            "Grey",
            "Red",
            "Blue",
            "Green",
            "Yellow",
            "Orange",
            "Violet",
            "Cyan",
            "Gold",
            "Silver",
            "None",
        ]
        border_ = [
            "Black",
            "White",
            "Grey",
            "Red",
            "Blue",
            "Green",
            "Yellow",
            "Orange",
            "Violet",
            "Cyan",
            "Gold",
            "Silver",
            "None",
        ]
        spec_ = [
            "Camo",
            "Web",
            "Vertigo",
            "Horizon",
            "Slash",
            "Broke",
            "Rich",
            "Stripe",
            "Solid",
        ]
        none_value = 8
        roll_t = randint(0, 1024)
        i = 0
        while i < none_value:
            bg_.append("Grey")
            border_.append("White")
            i += 1

        def get_spec() -> str:
            if roll_t <= len(spec_) - 1:
                return spec_[roll_t]
            else:
                return "None"

        return (
            bg_[randint(0, len(bg_) - 1)],
            border_[randint(0, len(border_) - 1)],
            get_spec(),
        )

    def get_image(self) -> str:
        img_ = [
            "[*void*]",
            "[$void$]",
            "[+void+]",
            "[!void!]",
            "[?void?]",
            "[#void#]",
            "[@void@]",
            "[&void&]",
            "[~void~]",
            "[%void%]",
            "[$DIRT]",
            "[#VOIDS]",
            "[dirt_Ranch^_]",
            "[!RTFM]",
            "[?FUD]",
            "[..fear]",
            "[..uncertainty]",
            "[..doubt]",
            "[RATFM!]",
            "[the_mound]",
            "[the_pit]",
        ]
        none_value = 16
        i = 0
        while i < none_value:
            img_.append("None")
            i += 1

        return img_[randint(0, len(img_) - 1)]
