# todo:
#   fix logs so they do not compound results of multiple runs

from .Proof_of_Work import Proof_of_Work, Blockchain_
from .Transactions import Wallet_
from .Shifter import shifter_
# from .No_funs import No_fun
import math, datetime, os, json, hashlib
from operator import itemgetter
from random import randint
import time

try:
    with open(f"{os.getcwd()}/minter_data/Minter_lists.json", "r") as file:
        jsonify = dict(json.load(file))
        OTHERS_LIST = jsonify['OTHERS_LIST']
        UDBBLS_LIST = jsonify["UDBBLS_LIST"]
        UTRIPS_LIST = jsonify["UTRIPS_LIST"]
        UBINRS_LIST = jsonify["UBINRS_LIST"]
except FileNotFoundError:
    try:
        os.mkdir(f"{os.getcwd()}/minter_data")
    except FileExistsError:
        pass
    finally:
        with open(f'{os.getcwd()}/minter_data/Minter_lists.json', 'x') as file:
            file.write(json.dumps({
            "OTHERS_LIST": [1234, 123, 321, 420, 69, 360, 1112, 200, 300, 400, 500, 600, 700, 800, 900, 1200, 1212],
            "UDBBLS_LIST": [11, 22, 33, 44, 55, 66, 77, 88, 99],
            "UTRIPS_LIST": [111, 222, 333, 444, 555, 666, 777, 888, 999],
            "UBINRS_LIST": [0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15]                
            }, indent=2))
        with open(f"{os.getcwd()}/minter_data/Minter_lists.json", "r") as file:
            jsonify = dict(json.load(file))
            OTHERS_LIST = jsonify['OTHERS_LIST']
            UDBBLS_LIST = jsonify["UDBBLS_LIST"]
            UTRIPS_LIST = jsonify["UTRIPS_LIST"]
            UBINRS_LIST = jsonify["UBINRS_LIST"]

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
    100: "100".zfill(4), 
    101: "101".zfill(4), 
    110: "110".zfill(4), 
    111: "111".zfill(4), 
    1000: "1000".zfill(4), 
    1001: "1001".zfill(4), 
    1010: "1010".zfill(4), 
    1011: "1011".zfill(4), 
    1100: "1100".zfill(4), 
    1101: "1101".zfill(4), 
    1110: "1110".zfill(4), 
    1111: "1111".zfill(4)
}
class ez_random:
    def __init__(self) -> None:
        self.return_ = self.get_()
    def get_(self) -> float:
            small_chk = (randint(1, 4096) + randint(0, 1))
            nanos_chk = ((time.time_ns() + small_chk) * math.pi)
            ez_nums = round( ( ((nanos_chk * small_chk) * (small_chk) )) % 1023 * (.000007 + randint(0, 1)), 5)
            ez_rand = (ez_nums + randint(0, 9999))
            return round(ez_rand)

class No_fun:
    def __init__(self, ez_num:ez_random) -> None:
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
        color_ =  str
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
            if ez_num_ == '0000':
                color_ = 'white'
                border_ = 'white'
                spec_ = 'cue'
                img_ = self.get_image()
            elif ez_num_ == '0001':
                color_ = 'yellow'
                border_ = 'yellow'
                spec_ = 'solid'
                img_ = self.get_image()   
            elif ez_num_ == '0010':
                color_ = 'blue'
                border_ = 'blue'
                spec_ = 'solid'
                img_ = self.get_image()   
            elif ez_num_ == '0011':
                color_ = 'red'
                border_ = 'red'
                spec_ = 'solid'
                img_ = self.get_image()
            elif ez_num_ == '0100':
                color_ = 'violet'
                border_ = 'violet'
                spec_ = 'solid'
                img_ = self.get_image()
            elif ez_num_ == '0101':
                color_ = 'orange'
                border_ = 'orange'
                spec_ = 'solid'
                img_ = self.get_image()
            elif ez_num_ == '0110':
                color_ = 'green'
                border_ = 'green'
                spec_ = 'solid'
                img_ = self.get_image()
            elif ez_num_ == '0111':
                color_ = 'cyan'
                border_ = 'cyan'
                spec_ = 'solid'
                img_ = self.get_image()
            elif ez_num_ == '1000':
                color_ = 'black'
                border_ = 'black'
                spec_ = 'eight'
                img_ = self.get_image()
            elif ez_num_ == '1001':
                color_ = 'yellow'
                border_ = 'yellow'
                spec_ = 'stripe'
                img_ = self.get_image()
            elif ez_num_ == '1010':
                color_ = 'blue'
                border_ = 'blue'
                spec_ = 'stripe'
                img_ = self.get_image()
            elif ez_num_ == '1011':
                color_ = 'red'
                border_ = 'red'
                spec_ = 'stripe'
                img_ = self.get_image()
            elif ez_num_ == '1100':
                color_ = 'violet'
                border_ = 'violet'
                spec_ = 'stripe'
                img_ = self.get_image()
            elif ez_num_ == '1101':
                color_ = 'orange'
                border_ = 'orange'
                spec_ = 'stripe'
                img_ = self.get_image()
            elif ez_num_ == '1110':
                color_ = 'green'
                border_ = 'green'
                spec_ = 'stripe'
                img_ = self.get_image()
            elif ez_num_ == '1111':
                color_ = 'cyan'
                border_ = 'cyan'
                spec_ = 'stripe'
                img_ = self.get_image()
            else:
                color_ = 'borked'
                border_ = 'borked'
                spec_ = 'borked'
                img_ = f'[{ez_num_}]'

        elif ez_num_ in OTHERS_LIST:
            ez_num_ = str(ez_num_)
            trait_ = ".:Rare:."
        elif ez_num_ in UDBBLS_LIST:
            ez_num_ = str(ez_num_)
            trait_ = ".:Dubbs:."
        elif ez_num_ in UTRIPS_LIST:
            ez_num_ = str(ez_num_)
            trait_ = ".:Trippps:."
        elif ez_num_ > 999 and ez_num_ <= 1234:
            ez_num_ = str(ez_num_)
            trait_ = ".unCommon."
        elif ez_num_ > 1234:
            ez_num_ = str(ez_num_)
            if trait_ != "":
                trait_ = ''.join(["(V/O/", trait_, "/I/D)"])
            else:
                trait_ = "::(V/O/I/D)::"
        else:
            ez_num_ = str(ez_num_)
            trait_ = "Common"


        void_attrs:dict = {
                "num": str(ez_num_),
                "trait": str(trait_),
                "float": str(float_),
                "color": str(color_),
                "border": str(border_),
                "img": str(img_),
                "special": str(spec_),
                "void": str(void_),
            }
        void_hash:str = self.hash_it(void_attrs)
        final_void:dict = {void_hash: void_attrs}
        self.hash_ = void_hash
        self.attrs = void_attrs
        return final_void

    def hash_it(self, attrs_:dict) -> str:
        attrs_t = {"time": self.time_}
        attrs_t.update(attrs_)
        encoded_data = json.dumps(attrs_t).encode()
        return shifter_(''.join(('0x', hashlib.sha256(encoded_data).hexdigest())))

    def get_float(self) -> str:
        float_ = randint(0, 100000000)
        if float_ >= 99999985 or float_ <= 15 or self.void is True:
            float_ = "VOID"
            self.void = True
            return float_
        else:
            float_ = "." + f"{float_}".zfill(8)
            return float_

    def get_colors(self) -> str:
        bg_ = ["Black", "White", "Grey", "Red", "Blue", "Green", "Yellow", "Orange", "Violet", "Cyan", "Gold", "Silver", "None"]
        border_ = ["Black", "White", "Grey", "Red", "Blue", "Green", "Yellow", "Orange", "Violet", "Cyan", "Gold", "Silver", "None"]
        spec_ = ["Camo", "Web", "Vertigo", "Horizon", "Slash", "Broke", "Rich", "Stripe", "Solid"]
        none_value = 8
        roll_t = randint(0, 1024)
        i = 0
        while i < none_value:
            bg_.append('Grey')
            border_.append('White')
            i+=1
        def get_spec() -> str:
            if roll_t <= len(spec_)-1:
                return spec_[roll_t]
            else:
                return "None"
        return bg_[randint(0, len(bg_)-1)], border_[randint(0, len(border_)-1)], get_spec()

    def get_image(self) -> str:
        img_ = ["[*void*]", "[$void$]", "[+void+]", "[!void!]", "[?void?]", "[#void#]", "[@void@]", "[&void&]", "[~void~]", "[%void%]", "[$DIRT]", "[#VOIDS]", "[dirt_Ranch^_]", "[!RTFM]", "[?FUD]", "[..fear]", "[..uncertainty]", "[..doubt]", "[RATFM!]", "[the_mound]", "[the_pit]"]
        none_value = 16
        i =0
        while i < none_value:
            img_.append('None')
            i+=1
        return img_[randint(0, len(img_)-1)]


class Minter_:
    unr_16_ = [] # < 16
    ubinrs_ = [] # binaries
    udbbls_ = [] # doubles
    utrips_ = [] # triples
    others_ = [] # some fun ones
    uppers_ = [] # > 999
    common_ = [] # the rest
    master_ = []
    chain:Blockchain_
    name_:str
    wallet_:str
    def __init__(self, 
        chain:Blockchain_,
        wallet:str='_', 
        name_:str="Minter", 
        iters_:int=256000, 
        sleep_time:float=0, 
        quick:bool=False
    ) -> None:
        self.chain = chain
        self.wallet_ = wallet
        self.unique_ = [] # uniques in a given session
        self.real_binaries_landed_ = []
        self.history = {
            "UNR_16": [],
            "UBINRS": [],
            "UDBBLS": [],
            "UTRIPS": [],
            "OTHERS": [],
            "UPPERS": [],
            "COMMON": [],

        }
        self.name_ = name_
        self.zero_counter = 0
        self.landed = 1
        self.start_time = float
        if quick is True:
            self.iters_ = 1
            self.sleep_time = 0
        else:
            self.iters_ = iters_
            self.sleep_time = sleep_time
            self.init_new_Minter(name_)

    # def ez_rand(self) -> float:
    #         small_chk = (randint(1, 4096) + randint(0, 1))
    #         nanos_chk = ((time.time_ns() + small_chk) * math.pi)
    #         ez_nums = round( ( ((nanos_chk * small_chk) * (small_chk) )) % 1023 * (.000007 + randint(0, 1)), 5)
    #         ez_rand = (ez_nums + randint(0, 9999))
    #         return round(ez_rand)

    def generator(self):
        # print(self.unique_)
        self.run_timer()
        self.unique_ = []
        i, j = 1, self.iters_ # i is always magical
        bins_, eq_count = 0, self.landed # currently necessary
        ez_rand = ez_random()
        while i <= j:
            i+=1
            time.sleep(self.sleep_time)
            # ez_rand = self.ez_rand()
            ez_rand = ez_random()

            rando_0 = (randint(0, 256) + randint(0, 1))
            rando_1 = (randint(1, 512) + randint(0, 1))
            rando_2 = (randint(0, 1024) + randint(0, 1))
            rando_3 = (randint(1, 768) + randint(0, 1))
            self.master_.append(ez_rand.return_)
            unique_bool = False
            if rando_0 == rando_1 and rando_2 <= rando_3:
                self.landed = eq_count
                unique_bool = True
                if ez_rand.return_ <= 1234 or (ez_rand.return_ > 1234 and ez_rand.return_ == randint(0, 9999999)):
                    block_chain_data = No_fun(ez_rand).get_attrs()
                    eq_count+=1
                    if ez_rand.return_ > 1234:
                        print("\t\t  !!Wowzers::")
                        self.others_.append("VOID")
                else:
                    block_chain_data = {}
                proof = Proof_of_Work(self.chain, self.wallet_, '0010')
                # init no_fun txn
                # txn = Txn_("to_address", self.chain.get_tallest_block[0], block_chain_data, amount, miner_fee)
                proof.mine_block(txns={}, txn_data=block_chain_data)

                # logs stuff
                self.print_minter_Heys(ez_rand.return_)
                print(f"iter_count: {i}")
            else:
                pass
            self.unique_check_(ez_rand.return_, unique_bool)
        # print("UNIQUE_FULL: ",sorted(self.unique_))

        self.end_timer()
        if self.iters_ != 1:
            self.summary_to_console()
            self.print_log_txt()
            print("  \nzero counter: ", self.zero_counter, "\n\n")
        elif self.iters_ == 1:
            if rando_0 == rando_1 and rando_2 <= rando_3:
                print("!!== ZOMG LANDED A SOLO BOII ==!!")
        return ez_rand.return_

    def print_minter_Heys(self, ez_rand:int):
        bins_ = 0
        if ez_rand in UBINRS_LIST:
            bins_+=1
            self.real_binaries_landed_ = bins_
            if ez_rand <= 15 and ez_rand != 0:
                print(f"\n!!Hey Unr_16::{UNR_16_MAP[ez_rand]}  !!\n")
                self.unr_16_.append(ez_rand)
            elif ez_rand != 0:
                print(f"\n!!Hey Bnr_16::{str(ez_rand).zfill(4)}  !!\n")
                self.ubinrs_.append(ez_rand)
            else:
                self.zero_counter+=1
                print(f"!!Hey Zero::{UNR_16_MAP[ez_rand]}  !!\n")
                self.unr_16_.append(ez_rand)
        elif ez_rand in UDBBLS_LIST:
            print(f"!!Hey Doubles::{ez_rand}  !!\n")
            self.udbbls_.append(ez_rand)
        elif ez_rand in UTRIPS_LIST:
            print(f"!!Hey Triples::{ez_rand}  !!\n")
            self.utrips_.append(ez_rand)  
        elif ez_rand in OTHERS_LIST:
            print(f"!!Hey Rare::{ez_rand}  !!\n")
            self.others_.append(ez_rand)
        elif ez_rand > 999 and ez_rand <= 1234:
            print(f"!!Hey Upper::{ez_rand}  !!\n")
            self.uppers_.append(ez_rand)
        elif ez_rand <= 1234:
            print(f"!!Hey Common::{ez_rand}  !!\n")
            self.common_.append(ez_rand)
        else:
            print("  .::[rip]::.")
            print("  u no winner ")
        

    def get_percents_(self) -> list:
        unr_16_p = (len(self.unr_16_) / self.iters_) * 100
        ubinrs_p = (len(self.ubinrs_) / self.iters_) * 100
        udbbls_p = (len(self.udbbls_) / self.iters_) * 100
        utrips_p = (len(self.utrips_) / self.iters_) * 100
        others_p = (len(self.others_) / self.iters_) * 100
        uppers_p = (len(self.uppers_) / self.iters_) * 100
        common_p = (len(self.common_) / self.iters_) * 100
        percents_ = [
            unr_16_p,
            ubinrs_p,
            udbbls_p,
            utrips_p,
            others_p,
            uppers_p,
            common_p,
        ]
        return percents_

    def get_percents_landed_(self) -> list:

        main_list_ = self.get_percents_()
        totals_p = (sum(main_list_))
        real_binary_p = (sum(main_list_[0:2]))
        
        percents_ = [
            totals_p,
            real_binary_p
        ]
        percents_.extend(main_list_)
        return percents_

    def unique_check_(self, int_:int, bool):
        # needs to be fixed so that it does not error in 
        # summary_log_txt if missed by the bool catch
        # once fixed it will not append if not True
        if bool is True:
            if int_ not in self.unique_ and int_ <= 1234:
                self.unique_.append(int_)
                print(f"  -- unique: {int_} --")
            else:
                pass
        else:
            if int_ not in self.unique_ and int_ <= 1234:
                self.unique_.append(int_)
            else:
                pass            

    def check_for_uniques_full(self):
        some_dict = {}
        for i in sorted(self.unique_):
            j = self.master_.count(i)
            some_dict.update({i: j})
        for i, j in some_dict.items():
            print(f"{i}:\tx{j}")
        print(len(some_dict), "/1235 total uniques")

    def check_for_uniques(self):
        some_dict = {}
        for i in sorted(self.unique_):
            if i not in list(self.history["COMMON"]):
                j = self.master_.count(i)
                some_dict.update({i: j})
            else:
                pass
        for i, j in some_dict.items():
            print(f"{i}:\t{j}")
        print(len(some_dict), "/1235 total uniques (exluding commons)")

    def run_timer(self):
        self.start_time = time.time()
        return self.start_time

    def end_timer(self):
        return round(time.time() - self.start_time, 2)

    def summary_to_console(self):
        print(f"""
    # Data:
        [showing only unique lands]
    Unr_16_: {sorted(list(set(self.unr_16_)))}   
    Ubinrs_: {sorted(list(set(self.ubinrs_)))}  
    Udbbls_: {sorted(list(set(self.udbbls_)))}  
    Utrips_: {sorted(list(set(self.utrips_)))}   
    Others_: {sorted(list(set(self.others_)))}  
    Uppers_: {sorted(list(set(self.uppers_)))}  
    Common_: {sorted(list(set(self.common_)))}
        """)
        print(f"""
        {len(self.unique_)}_u::{self.iters_} Iterations took {self.end_timer()} sec 
                sleep_time -- {self.sleep_time} sec
                percent_landed -- {round(sum(self.get_percents_()), 2)}% -- acc {self.get_percents_landed_()[7]}%
                ceiling: {max(self.unique_)}
                landed: {self.landed - 1}
                binaries landed: {self.real_binaries_landed_} -- {round(self.get_percents_landed_()[8], 5)}%

            Unr_16_: {len(self.unr_16_)}   \t\t{round((self.get_percents_landed_())[0], 5)}%   
            Ubinrs_: {len(self.ubinrs_)}   \t\t{round((self.get_percents_landed_())[1], 5)}% 
            Udbbls_: {len(self.udbbls_)}   \t\t{round((self.get_percents_landed_())[2], 5)}%
            Utrips_: {len(self.utrips_)}   \t\t{round((self.get_percents_landed_())[3], 5)}%   
            Others_: {len(self.others_)}   \t\t{round((self.get_percents_landed_())[4], 5)}% 
            Uppers_: {len(self.uppers_)}   \t\t{round((self.get_percents_landed_())[5], 5)}% 
            Common_: {len(self.common_)}   \t\t{round((self.get_percents_landed_())[6], 5)}%

        """)

    # FILES ---
    def history_counts(self):
        j = 0
        hist_dict = []
        if self.name_ != "Q_MINT":
            for i in range(0, 1235):
                for j in self.history.keys():
                    if i in self.history.get(j):
                        hist_dict.append({"num": i ,"count" : self.history.get(j).count(i)})
                        # time.sleep(self.sleep_time)
            sorted_list = sorted(hist_dict, key=itemgetter("count"))
            with open(f'{os.getcwd()}/minter_data/{self.name_}_counts.json', "w") as file:
                file.write(json.dumps(sorted_list, indent=2))

    def print_log_txt(self):
        if self.name_ != "Q_MINT":
            with open(f'{os.getcwd()}/minter_data/{self.name_}_log.txt', 'a') as file:
                if self.iters_ > 750:
                    file.write(f"""
        {self.iters_}::{len(self.unique_)}  
                iterations took {self.end_timer()} sec 
                sleep_time -- {self.sleep_time} sec 
                percent_landed -- {round(sum(self.get_percents_()), 2)}%
                ceiling: {max(self.unique_)}
                landed: {self.landed - 1}
                binaries landed: {self.real_binaries_landed_}


            Unr_16_: {len(self.unr_16_)}   \t\t{round((self.get_percents_())[0], 8)}%   
            Ubinrs_: {len(self.ubinrs_)}   \t\t{round((self.get_percents_())[1], 8)}% 
            Udbbls_: {len(self.udbbls_)}   \t\t{round((self.get_percents_())[2], 8)}%
            Utrips_: {len(self.utrips_)}   \t\t{round((self.get_percents_())[3], 8)}%   
            Others_: {len(self.others_)}   \t\t{round((self.get_percents_())[4], 8)}% 
            Uppers_: {len(self.uppers_)}   \t\t{round((self.get_percents_())[5], 8)}% 
            Common_: {len(self.common_)}     \t{round((self.get_percents_())[6], 8)}%

            """)

    def init_new_Minter(self, name_:str):
        if self.name_ != "Q_MINT":
            try:
                with open(f'{os.getcwd()}/minter_data/{name_}_log.txt', 'x') as file:
                    file.write(f"Minter_{name_}")
            except FileExistsError:
                pass
            finally:
                try:
                    with open(f'{os.getcwd()}/minter_data/{name_}_history.json', 'x') as file:
                        file.write(json.dumps({
                            "UNR_16": [],
                            "UBINRS": [],
                            "UDBBLS": [],
                            "UTRIPS": [],
                            "OTHERS": [],
                            "UPPERS": [],
                            "COMMON": []

                        }, indent=2))
                except FileExistsError:
                    pass
                          
    def update_history_json(self):
        if self.name_ != "Q_MINT":
            with open(f"{os.getcwd()}/minter_data/{self.name_}_history.json", "r") as file:
                MINTER_DATA = dict(json.load(file))
                self.history["UNR_16"].extend(list(MINTER_DATA["UNR_16"]))
                self.history["UBINRS"].extend(list(MINTER_DATA["UBINRS"]))
                self.history["UDBBLS"].extend(list(MINTER_DATA["UDBBLS"]))
                self.history["UTRIPS"].extend(list(MINTER_DATA["UTRIPS"]))
                self.history["OTHERS"].extend(list(MINTER_DATA["OTHERS"]))
                self.history["UPPERS"].extend(list(MINTER_DATA["UPPERS"]))
                self.history["COMMON"].extend(list(MINTER_DATA["COMMON"]))
            self.write_json_data()
            return self.history            

    def write_json_data(self):
        with open(f"{os.getcwd()}/minter_data/{self.name_}_history.json", "w") as file:
            file.write((json.dumps((self.jsonify_data()), indent=2)))        

    def jsonify_data(self) -> dict:
        self.history["UNR_16"].extend(self.unr_16_)
        self.history["UBINRS"].extend(self.ubinrs_)
        self.history["UDBBLS"].extend(self.udbbls_)
        self.history["UTRIPS"].extend(self.utrips_)
        self.history["OTHERS"].extend(self.others_)
        self.history["UPPERS"].extend(self.uppers_)
        self.history["COMMON"].extend(self.common_)

        return self.history



