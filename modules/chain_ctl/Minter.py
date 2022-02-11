# todo:
#   fix logs so they do not compound results of multiple runs


import math, datetime, os, json, dotenv
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
            "OTHERS_LIST": [420, 69, 1111, 1234, 999, 666, 123],
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

}
class Minter_:
    def __init__(self, name_:str, iters_:int, sleep_time:float, quick:bool=False) -> None:
        self.unr_16_ = [] # rares
        self.ubinrs_ = [] # binaries
        self.udbbls_ = [] # doubles
        self.utrips_ = [] # triples
        self.others_ = [] # some fun ones
        self.uppers_ = [] # over 999
        self.common_ = [] # the rest
        self.unique_ = [] # uniques in a given session
        self.master_ = []
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
        self.landed = 0
        self.start_time = float
        if quick is True:
            self.iters_ = 1
            self.sleep_time = 0
        else:
            self.iters_ = iters_
            self.sleep_time = sleep_time
            self.init_new_Minter(name_)

    def ez_rand(self) -> float:
            small_chk = (randint(1, 4096) + randint(0, 1))
            nanos_chk = ((time.time_ns() + small_chk) * math.pi)
            ez_nums = round( ( ((nanos_chk * small_chk) * (small_chk) )) % 1023 * (.0007 + randint(0, 1)), 5)
            # print(ez_nums)
            ez_rand = (ez_nums + randint(0, 212)) # adjust ceiling with this line
            return ez_rand

    def generator(self):
        print(self.unique_)
        self.run_timer()
        self.unique_ = []
        i, j = 1, self.iters_ # i is always magical
        bins_, eq_count = 0, self.landed # currently necessary 
        while i <= j:
            i+=1
            time.sleep(self.sleep_time)

            ez_rand = int(self.ez_rand())

            rando_0 = (randint(0, 256) + randint(0, 1))
            rando_1 = (randint(1, 512) + randint(0, 1))
            rando_2 = (randint(0, 1024) + randint(0, 1))
            rando_3 = (randint(1, 768) + randint(0, 1))
            self.master_.append(ez_rand)
            unique_bool = False
            if rando_0 == rando_1 and rando_2 <= rando_3:
                eq_count+=1
                unique_bool = True
                self.landed = eq_count
                if ez_rand in UBINRS_LIST:
                    bins_+=1
                    if ez_rand <= 15 and ez_rand != 0:
                        print(f"  !!!Unr_16::{UNR_16_MAP[ez_rand]}")
                        self.unr_16_.append(ez_rand)
                    elif ez_rand != 0:
                        print(f"  !!!Bnr_16::{str(ez_rand).zfill(4)}")
                        self.ubinrs_.append(ez_rand)
                    else:
                        self.zero_counter+=1
                        print(f"  !!!Zero::{UNR_16_MAP[ez_rand]}")
                        self.unr_16_.append(ez_rand)
                elif ez_rand in UDBBLS_LIST:
                    print(f"  !!!Doubles::{ez_rand}")
                    self.udbbls_.append(ez_rand)
                elif ez_rand in UTRIPS_LIST:
                    print(f"  !!!Triples::{ez_rand}")
                    self.utrips_.append(ez_rand)  
                elif ez_rand in OTHERS_LIST:
                    print(f"  !!!Rare::{ez_rand}")
                    self.others_.append(ez_rand)
                elif ez_rand > 999:
                    print(f"!!Upper::{ez_rand}")
                    self.uppers_.append(ez_rand)
                else:
                    self.common_.append(ez_rand)
            else:
                pass

            self.unique_check_(ez_rand, unique_bool)
        print("UNIQUE_FULL: ",sorted(self.unique_))

        self.end_timer()
        if self.iters_ != 1:
            self.summary_to_console()
            self.print_log_txt()
            print("  \nzero counter: ", self.zero_counter, "\n\n")
        elif self.iters_ == 1:
            if rando_0 == rando_1 and rando_2 <= rando_3:
                print("!!== ZOMG LANDED A SOLO BOII ==!!")
        return ez_rand


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

    def unique_check_(self, int_:int, bool):
        # needs to be fixed so that it does not error in 
        # summary_log_txt if missed by the bool catch
        # once fixed it will not append if not True
        if bool is True:
            if int_ not in self.unique_:
                self.unique_.append(int_)
                print(f"  -- unique: {int_} --")
            else:
                pass
        else:
            if int_ not in self.unique_:
                self.unique_.append(int_)
            else:
                pass            

    # def get_unique_heights(self, i:int):
    #     j = 0
    #     if i in self.master_:
    #         j+=1
    #     return j

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
                percent_landed -- {round(sum(self.get_percents_()), 2)}%
                landed: {self.landed}
                ceiling: {max(self.unique_)}

            Unr_16_: {len(self.unr_16_)}   \t\t{round((self.get_percents_())[0], 5)}%   
            Ubinrs_: {len(self.ubinrs_)}   \t\t{round((self.get_percents_())[1], 5)}% 
            Udbbls_: {len(self.udbbls_)}   \t\t{round((self.get_percents_())[2], 5)}%
            Utrips_: {len(self.utrips_)}   \t\t{round((self.get_percents_())[3], 5)}%   
            Others_: {len(self.others_)}   \t\t{round((self.get_percents_())[4], 5)}% 
            Uppers_: {len(self.uppers_)}   \t\t{round((self.get_percents_())[5], 5)}% 
            Common_: {len(self.common_)}   \t\t{round((self.get_percents_())[6], 5)}%

        """)


    # FILES ---
    def print_log_txt(self):
        with open(f'{os.getcwd()}/minter_data/{self.name_}_log.txt', 'a') as file:
            if self.iters_ > 750000:
                file.write(f"""
    {self.iters_}::{len(self.unique_)}  
            iterations took {self.end_timer()} sec 
            sleep_time -- {self.sleep_time} sec 
            percent_landed -- {round(sum(self.get_percents_()), 2)}% 
            landed: {self.landed}

            ceiling: {max(self.unique_)}


        Unr_16_: {len(self.unr_16_)}   \t\t{round((self.get_percents_())[0], 8)}%   
        Ubinrs_: {len(self.ubinrs_)}   \t\t{round((self.get_percents_())[1], 8)}% 
        Udbbls_: {len(self.udbbls_)}   \t\t{round((self.get_percents_())[2], 8)}%
        Utrips_: {len(self.utrips_)}   \t\t{round((self.get_percents_())[3], 8)}%   
        Others_: {len(self.others_)}   \t\t{round((self.get_percents_())[4], 8)}% 
        Uppers_: {len(self.uppers_)}   \t\t{round((self.get_percents_())[5], 8)}% 
        Common_: {len(self.common_)}     \t{round((self.get_percents_())[6], 8)}%

        """)
    # def json_init(self):
    #     try:
    #         with open(f'{os.getcwd()}/minter_data/{self.name_}.json', 'x') as file:
    #             json_obj_ = self.jsonify_()
    #             new_file = json.dumps(json_obj_, indent=4)
    #             file.write(new_file)
    #     except FileExistsError:
    #         print("Err!! Filename in use.")

    def init_new_Minter(self, name_:str):
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
                          
    def jsonify_(self) -> dict:
        new_dict = {
            f"{self.name_}": {
                "UNR_16": sorted(self.unr_16_),
                "UBINRS": sorted(self.ubinrs_),
                "UDBBLS": sorted(self.udbbls_),
                "UTRIPS": sorted(self.utrips_),
                "OTHERS": sorted(self.others_),
                "UPPERS": sorted(self.uppers_),
            }
        }
        json_list = json.dumps(new_dict, indent=4)
        return new_dict
    def update_history_json(self):
        with open(f"{os.getcwd()}/minter_data/{self.name_}_history.json", "r") as file:
            MINTER_DATA = dict(json.load(file))
            self.history["UNR_16"].extend(list(MINTER_DATA["UNR_16"]))
            self.history["UBINRS"].extend(list(MINTER_DATA["UBINRS"]))
            self.history["UDBBLS"].extend(list(MINTER_DATA["UDBBLS"]))
            self.history["UTRIPS"].extend(list(MINTER_DATA["UTRIPS"]))
            self.history["OTHERS"].extend(list(MINTER_DATA["OTHERS"]))
            self.history["UPPERS"].extend(list(MINTER_DATA["UPPERS"]))
            self.history["COMMON"].extend(list(MINTER_DATA["COMMON"]))
            self.history["UNR_16"].extend(self.unr_16_)
            self.history["UBINRS"].extend(self.ubinrs_)
            self.history["UDBBLS"].extend(self.udbbls_)
            self.history["UTRIPS"].extend(self.utrips_)
            self.history["OTHERS"].extend(self.others_)
            self.history["UPPERS"].extend(self.uppers_)
            self.history["COMMON"].extend(self.common_)

        self.write_json_data()
        return self.history            

    def jsonify_data(self) -> dict:
        self.history["UNR_16"].extend(self.unr_16_)
        self.history["UBINRS"].extend(self.ubinrs_)
        self.history["UDBBLS"].extend(self.udbbls_)
        self.history["UTRIPS"].extend(self.utrips_)
        self.history["OTHERS"].extend(self.others_)
        self.history["UPPERS"].extend(self.uppers_)
        self.history["COMMON"].extend(self.common_)

        return self.history
    def write_json_data(self):
        with open(f"{os.getcwd()}/minter_data/{self.name_}_history.json", "w") as file:
            file.write((json.dumps((self.jsonify_data()), indent=2)))        




QMINTER = Minter_("Q_MINT", 100000, .0005, True)
