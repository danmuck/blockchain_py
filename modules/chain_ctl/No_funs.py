# todo:
#   fix logs so they do not compound results of multiple runs

import math, datetime, os, json, hashlib
from random import randint

UNR_16_MAP = {
    0: "0".zfill(4),
    1: "1".zfill(4),
    2: "10".zfill(4),
    3: "11".zfill(4),
    4: "100".zfill(4),
    5: "101".zfill(4),
    6: "110".zfill(4),
    7: "111".zfill(4),
    8: "1000".zfill(4),
    9: "1001".zfill(4),
    10: "1010".zfill(4),
    11: "1011".zfill(4),
    12: "1100".zfill(4),
    13: "1101".zfill(4),
    14: "1110".zfill(4),
    15: "1111".zfill(4),
}
LISTS_ = {
    "OTHERS_LIST": [1234, 123, 321, 420, 69, 360, 1112, 200, 300, 400, 500, 600, 700, 800, 900, 1200, 1212],
    "UDBBLS_LIST": [11, 22, 33, 44, 55, 66, 77, 88, 99],
    "UTRIPS_LIST": [111, 222, 333, 444, 555, 666, 777, 888, 999],
    "UBINRS_LIST": [0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15]  
}

class No_fun:
    def __init__(self, ez_num:int) -> None:
        self.ez_num = ez_num
        self.attrs = {}
        self.hash_ = str
        if ez_num > 1234:
            self.void = True
        else:
            self.void = False

    def get_attrs(self) -> dict:
        ez_num_ = self.ez_num
        time_ = str(datetime.datetime.now())
        float_ = self.get_float()
        color_ =  str
        border_ = str
        img_ = str
        trait_ = str
        if self.void is True:
            color_ = "V"
            border_ = "V"
            void_ = "VOID"
        else:
            color_, border_ = self.get_colors()
            img_ = self.get_image()
            void_ = "    "

        if ez_num_ in LISTS_['UBINRS_LIST']:
            ez_num_ = UNR_16_MAP[ez_num_]
            trait_ = ".::Unr_16::Binary::."
        elif ez_num_ in LISTS_['OTHERS_LIST']:
            trait_ = ".:Rare:."
        elif ez_num_ in LISTS_['UDBBLS_LIST']:
            trait_ = ".::Dubbs::."
        elif ez_num_ in LISTS_['UTRIPS_LIST']:
            trait_ = ".::Trippps::."
        elif ez_num_ > 999 and ez_num_ <= 1234:
            trait_ = ".Uppers."
        elif ez_num_ > 1234:
            trait_ = "::::void::::"
        else:
            trait_ = "Common"

        void_attrs:dict = {
                "num": ez_num_,
                "trait": trait_,
                "float": float_,
                "color": color_,
                "border": border_,
                "img": img_,
                "time": time_,
                "void": void_
            }
        void_hash:str = self.hash_it(void_attrs)
        final_void:dict = {void_hash: void_attrs}
        self.hash_ = void_hash
        self.attrs = void_attrs
        return final_void

    def hash_it(self, attrs_:dict) -> str:
        encoded_data = json.dumps(attrs_).encode()
        return ''.join(('0x', hashlib.sha256(encoded_data).hexdigest()))

    def get_float(self) -> str:
        float_ = randint(0, 100000000)
        if float_ >= 99999999:
            float_ = "VOID"
            self.void = True
            return float_
        else:
            float_ = "." + f"{float_}".zfill(8)
            return float_

    def get_colors(self) -> str:
        bg_ = ["Black", "White", "Grey", "Red", "Blue", "Green", "Yellow", "Orange", "Pink", "Purple"]
        border_ = ["Black", "White", "Grey", "Red", "Blue", "Green", "Yellow", "Orange", "Pink", "Purple"]
        return bg_[randint(0,9)], border_[randint(0,9)]

    def get_image(self) -> str:
        '''
            Not sure about this yet, returning a random char for now...
        '''
        img_ = ["*", "$", "+", "!", "?", "#", "@", "&", "~", "%"]
        return img_[randint(0,9)]

# i, j = 0, 100000000
# while i < j:
#     test = No_fun(99).get_float()
#     i+=1
#     # print(test)
#     if test == "VOID":
#         print("WOW")
