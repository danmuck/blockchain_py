# todo:
#   fix logs so they do not compound results of multiple runs


import math, datetime, os, json, dotenv
from random import randint
import time

try:
    with open(f"{os.getcwd()}/sandbox_/Minter_lists.json", "r") as file:
        jsonify = dict(json.load(file))
        OTHERS_LIST = jsonify['OTHERS_LIST']
        UDBBLS_LIST = jsonify["UDBBLS_LIST"]
        UTRIPS_LIST = jsonify["UTRIPS_LIST"]
        UBINRS_LIST = jsonify["UBINRS_LIST"]
except FileNotFoundError:
    try:
        os.mkdir(f"{os.getcwd()}/sandbox_")
    except FileExistsError:
        pass
    finally:
        with open(f'{os.getcwd()}/sandbox_/Minter_lists.json', 'x') as file:
            file.write(json.dumps({
            "OTHERS_LIST": [420, 69, 1111, 1234, 999, 666, 123],
            "UDBBLS_LIST": [11, 22, 33, 44, 55, 66, 77, 88, 99],
            "UTRIPS_LIST": [111, 222, 333, 444, 555, 666, 777, 888, 999],
            "UBINRS_LIST": [0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111]                
            }, indent=2))
        with open(f"{os.getcwd()}/sandbox_/Minter_lists.json", "r") as file:
            jsonify = dict(json.load(file))
            OTHERS_LIST = jsonify['OTHERS_LIST']
            UDBBLS_LIST = jsonify["UDBBLS_LIST"]
            UTRIPS_LIST = jsonify["UTRIPS_LIST"]
            UBINRS_LIST = jsonify["UBINRS_LIST"]
        


class Minter:
    def __init__(self, name_:str, iters_:int, sleep_time:float) -> None:
        self.unr_16_ = [] # rares
        self.ubinrs_ = [] # binaries
        self.udbbls_ = [] # doubles
        self.utrips_ = [] # triples
        self.others_ = [] # some fun ones
        self.ovr999_ = [] # over 999
        self.common_ = [] # the rest
        self.unique_ = [] # uniques in a given session
        self.master_ = []
        self.history = {
            "UNR_16": [],
            "UBINRS": [],
            "UDBBLS": [],
            "UTRIPS": [],
            "OTHERS": [],
            "OVR999": [],
            "COMMON": [],

        }
        self.name_ = name_
        self.zero_counter = 0
        self.landed = 0
        self.start_time = float
        self.iters_ = iters_
        self.sleep_time = sleep_time
        self.init_new_Minter(name_)

    def generator(self):
        self.run_timer()
        i, j = 1, self.iters_
        bins_, eq_count = 0, self.landed # necessary 
        while i <= j:
            small_chk = (randint(1, 4096) + randint(0, 1))
            nanos_chk = ((time.time_ns() + small_chk) * math.pi)
            i+=1
            time.sleep(self.sleep_time)
            ez_nums = int( ( ((nanos_chk * small_chk) * (small_chk) )) % 1023 )
            
            ez_rand = (ez_nums + randint(0, 212))
            rando_0 = (randint(0, 256) + randint(0, 1))
            rando_1 = (randint(1, 512) + randint(0, 1))
            rando_2 = (randint(0, 1024) + randint(0, 1))
            rando_3 = (randint(1, 768) + randint(0, 1))

            self.master_.append(ez_rand)
            self.get_uniques(ez_rand)

            if rando_0 == rando_1 and rando_2 <= rando_3:
                eq_count+=1
                self.landed = eq_count
                if ez_rand in UBINRS_LIST:
                    bins_+=1
                    self.ubinrs_.append(ez_rand)
                elif ez_rand <= 15 and ez_rand != 0:
                    print(f"  !!Rare::{ez_rand}")
                    self.unr_16_.append(ez_rand)
                elif ez_rand in UDBBLS_LIST:
                    print(f"  !!Rare::{ez_rand}")
                    self.udbbls_.append(ez_rand)
                elif ez_rand in UTRIPS_LIST:
                    print(f"  !!Rare::{ez_rand}")
                    self.utrips_.append(ez_rand)  
                elif ez_rand in OTHERS_LIST:
                    print(f"  !!Rare::{ez_rand}")
                    self.others_.append(ez_rand)
                elif ez_rand == 0:
                    print(f"  !!Rare::{ez_rand}")
                    self.ubinrs_.append(ez_rand)
                    self.zero_counter+=1
                elif ez_rand > 999:
                    print(f"!!Rare::{ez_rand}")
                    self.ovr999_.append(ez_rand)
                else:
                    self.common_.append(ez_rand)
            else:
                pass

        print("binary counter: ", bins_, "\n  zero counter: ", self.zero_counter)
        print("landed: ", eq_count)

        self.end_timer()
        self.summary_to_console()
        self.print_log_txt()


    def get_percents_(self) -> list:
        unr_16_p = (len(self.unr_16_) / self.iters_) * 100
        ubinrs_p = (len(self.ubinrs_) / self.iters_) * 100
        udbbls_p = (len(self.udbbls_) / self.iters_) * 100
        utrips_p = (len(self.utrips_) / self.iters_) * 100
        others_p = (len(self.others_) / self.iters_) * 100
        ovr999_p = (len(self.ovr999_) / self.iters_) * 100
        common_p = (len(self.common_) / self.iters_) * 100
        percents_ = [
            unr_16_p,
            ubinrs_p,
            udbbls_p,
            utrips_p,
            others_p,
            ovr999_p,
            common_p,
        ]
        return percents_

    def get_uniques(self, int_:int):
        if int_ not in self.unique_:
            self.unique_.append(int_)
            print(f"!!Unique::{int_}")
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

    Unr_16_: {sorted(self.unr_16_)}   
    Ubinrs_: {sorted(self.ubinrs_)}  
    Udbbls_: {sorted(self.udbbls_)}  
    Utrips_: {sorted(self.utrips_)}   
    Others_: {sorted(self.others_)}  
    Ovr999_: {sorted(self.ovr999_)}  
    Common_: [disabled]
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
            Ovr999_: {len(self.ovr999_)}   \t\t{round((self.get_percents_())[5], 5)}% 
            Common_: {len(self.common_)}   \t\t{round((self.get_percents_())[6], 5)}%

        """)


    # FILES ---
    def print_log_txt(self):
        with open(f'{os.getcwd()}/sandbox_/{self.name_}_log.txt', 'a') as file:
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
        Ovr999_: {len(self.ovr999_)}   \t\t{round((self.get_percents_())[5], 8)}% 
        Common_: {len(self.common_)}     \t{round((self.get_percents_())[6], 8)}%

        """)
    # def json_init(self):
    #     try:
    #         with open(f'{os.getcwd()}/sandbox_/{self.name_}.json', 'x') as file:
    #             json_obj_ = self.jsonify_()
    #             new_file = json.dumps(json_obj_, indent=4)
    #             file.write(new_file)
    #     except FileExistsError:
    #         print("Err!! Filename in use.")

    def init_new_Minter(self, name_:str):
        try:
            with open(f'{os.getcwd()}/sandbox_/{name_}_log.txt', 'x') as file:
                file.write(f"Minter_{name_}")
        except FileExistsError:
            pass
        try:
            with open(f'{os.getcwd()}/sandbox_/{name_}_history.json', 'x') as file:
                file.write(json.dumps({
                    "UNR_16": [],
                    "UBINRS": [],
                    "UDBBLS": [],
                    "UTRIPS": [],
                    "OTHERS": [],
                    "OVR999": [],
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
                "OVR999": sorted(self.ovr999_),
            }
        }
        json_list = json.dumps(new_dict, indent=4)
        return new_dict
    def update_history_json(self):
        with open(f"{os.getcwd()}/sandbox_/{self.name_}_history.json", "r") as file:
            MINTER_DATA = dict(json.load(file))
            self.history["UNR_16"].extend(list(MINTER_DATA["UNR_16"]))
            self.history["UBINRS"].extend(list(MINTER_DATA["UBINRS"]))
            self.history["UDBBLS"].extend(list(MINTER_DATA["UDBBLS"]))
            self.history["UTRIPS"].extend(list(MINTER_DATA["UTRIPS"]))
            self.history["OTHERS"].extend(list(MINTER_DATA["OTHERS"]))
            self.history["OVR999"].extend(list(MINTER_DATA["OVR999"]))
            self.history["COMMON"].extend(list(MINTER_DATA["COMMON"]))
            self.history["UNR_16"].extend(self.unr_16_)
            self.history["UBINRS"].extend(self.ubinrs_)
            self.history["UDBBLS"].extend(self.udbbls_)
            self.history["UTRIPS"].extend(self.utrips_)
            self.history["OTHERS"].extend(self.others_)
            self.history["OVR999"].extend(self.ovr999_)
            self.history["COMMON"].extend(self.common_)

        self.write_json_data()
        return self.history            

    def jsonify_data(self) -> dict:
        self.history["UNR_16"].extend(self.unr_16_)
        self.history["UBINRS"].extend(self.ubinrs_)
        self.history["UDBBLS"].extend(self.udbbls_)
        self.history["UTRIPS"].extend(self.utrips_)
        self.history["OTHERS"].extend(self.others_)
        self.history["OVR999"].extend(self.ovr999_)
        self.history["COMMON"].extend(self.common_)

        return self.history
    def write_json_data(self):
        with open(f"{os.getcwd()}/sandbox_/{self.name_}_history.json", "w") as file:
            file.write((json.dumps((self.jsonify_data()), indent=2)))        





def main():
    trial = Minter("Minter_Sleep", 1000000, .000002)

    trial.generator()


    # trial.check_for_uniques()


    trial.update_history_json()

main()