import math, datetime, os, json, dotenv
from random import randint
import time
# dotenv.load_dotenv()
# UDBBLS_LIST = os.environ.get("UDBBLS_LIST")
# UTRIPS_LIST = os.environ.get("UTRIPS_LIST")
# OTHERS_LIST = os.environ.get("OTHERS_LIST")

OTHERS_LIST = [
        420,
        69,
        1111,
        1234,
        999,
        666,
        123,

    ]
UDBBLS_LIST = [
        11,
        22,
        33,
        44,
        55,
        66,
        77,
        88,
        99,

    ]
UTRIPS_LIST = [
        111,
        222,
        333,
        444,
        555,
        666,
        777,
        888,
        999,

    ]

class Minter:
    def __init__(self, name_:str, iters_:int, sleep_time:float) -> None:
        self.unr_16_ = [] # rares
        self.ubinrs_ = [] # binaries
        self.udbbls_ = [] # doubles
        self.utrips_ = [] # triples
        self.others_ = [] # some fun ones
        self.ovr999_ = [] # over 999
        self.common_ = [] # the rest
        self.unique_ = [] # uniques in a given run
        self.master_ = []
        self.name_ = name_
        self.zero_counter = 0
        self.start_time = float
        self.iters_ = iters_
        self.sleep_time = sleep_time

    def generator(self, to_json:bool=False):
        self.run_timer()
        i, j = 1, self.iters_
        while i <= j:
            small_chk = (randint(1, 4096) + randint(0, 1))
            nanos_chk = ((time.time_ns() + small_chk) * math.pi)
            i+=1
            time.sleep(self.sleep_time)
            ez_nums = int( ( ((nanos_chk * small_chk) * (small_chk) )) % 1023 )
            
            self.master_.append(ez_nums)
            self.get_uniques(ez_nums)

            if ez_nums <= 15 and ez_nums != 0:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.unr_16_.append(ez_nums)
            elif ez_nums in UDBBLS_LIST:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.udbbls_.append(ez_nums)
            elif ez_nums in UTRIPS_LIST:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.utrips_.append(ez_nums)  
            elif ez_nums in OTHERS_LIST:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.others_.append(ez_nums)
            elif ez_nums == 0:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.ubinrs_.append(ez_nums)
            elif ez_nums > 999:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.ovr999_.append(ez_nums)
            else:
                # print(ez_nums)
                self.common_.append(ez_nums)

            
        self.end_timer()
        self.summary_to_console()
        self.print_log_txt()
        if to_json is True:
            self.json_init()

    def generator_hm(self, to_json:bool=False):
        self.run_timer()
        i, j = 1, self.iters_
        r0_is_r1_counter = 0
        bins_ = 0
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
            bin_list = [1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111]
            if ez_rand in bin_list:
                if rando_0 == rando_1 and rando_2 <= rando_3 and ez_rand != 0:
                    bins_ += 1 
                    self.ubinrs_.append(ez_rand)
            elif ez_rand <= 15 and ez_rand != 0:
                if rando_0 == rando_1 and rando_2 <= rando_3:
                    print(f"!! --   {ez_rand}   \t -- !!")
                    self.unr_16_.append(ez_rand)
                else:
                    pass                    
            elif ez_rand in UDBBLS_LIST:
                if rando_0 == rando_1 and rando_2 <= rando_3:
                    print(f"!! --   {ez_rand}   \t -- !!")
                    self.udbbls_.append(ez_rand)
                else:
                    pass                    
            elif ez_rand in UTRIPS_LIST:
                if rando_0 == rando_1 and rando_2 <= rando_3:
                    print(f"!! --   {ez_rand}   \t -- !!")
                    self.utrips_.append(ez_rand)  
                else:
                    pass                    
            elif ez_rand in OTHERS_LIST:
                if rando_0 == rando_1 and rando_2 <= rando_3:
                    print(f"!! --   {ez_rand}   \t -- !!")
                    self.others_.append(ez_rand)
                else:
                    pass                   
            elif ez_rand == 0:
                if rando_0 == rando_1 and rando_2 <= rando_3:
                    self.zero_counter+=1
                    self.ubinrs_.append(ez_rand)
                else:
                    pass                    
            elif ez_rand > 999:
                if rando_0 == rando_1 and rando_2 <= rando_3:
                    print(f"!! --   {ez_rand}   \t -- !!")
                    self.ovr999_.append(ez_rand)
                else:
                    pass
            else:
                if rando_0 == rando_1 and rando_2 <= rando_3:
                    self.common_.append(ez_rand)
                elif rando_0 == rando_1:
                    r0_is_r1_counter += 1
                else:
                    pass
        print("binary counter: ", bins_, "\n  zero counter: ", self.zero_counter)
        print("r0/r1 counter: ", r0_is_r1_counter)


        self.end_timer()
        self.summary_to_console()
        self.print_log_txt()
        if to_json is True:
            self.json_init()

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
            print(f"!! -- UNQ:{int_}::{self.master_.count(int_)} -- !!")
            # print(f"{int_}::",len(self.unique_))
        else:
            pass

    def single_unq_len(self, i:int):
        j = 0
        if i in self.master_:
            j+=1
        return j

    def check_unqs(self):
        some_dict = {}
        for i in sorted(self.unique_):
            j = self.master_.count(i)
            some_dict.update({i: j})
        for i, j in some_dict.items():
            print(f"{i}:\tx{j}")
        print(len(some_dict), " total uniques")

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
    Common_: {sorted(self.common_)}
        """)
        print(f"""
      [iters::uniques]
        {self.iters_}::{len(self.unique_)} Iterations took {self.end_timer()} sec -- 
                sleep_time -- {self.sleep_time} sec
                accuracy check -- {round(sum(self.get_percents_()), 2)}%
                top_end: {max(self.unique_)}

            Unr_16_: {len(self.unr_16_)}   \t\t{round((self.get_percents_())[0], 2)}%   
            Ubinrs_: {len(self.ubinrs_)}   \t\t{round((self.get_percents_())[4], 2)}% 
            Udbbls_: {len(self.udbbls_)}   \t\t{round((self.get_percents_())[1], 2)}%
            Utrips_: {len(self.utrips_)}   \t\t{round((self.get_percents_())[2], 2)}%   
            Others_: {len(self.others_)}   \t\t{round((self.get_percents_())[3], 2)}% 
            Ovr999_: {len(self.ovr999_)}   \t\t{round((self.get_percents_())[5], 2)}% 
            Common_: {len(self.common_)}   \t\t{round((self.get_percents_())[6], 2)}%

        """)


    # FILES ---
    def print_log_txt(self):
        with open(f'{os.getcwd()}/sandbox_/{self.name_}.txt', 'a') as file:
            file.write(f"""
    {self.iters_}::{len(self.unique_)}  
            iterations took {self.end_timer()} sec -- 
            sleep_time -- {self.sleep_time} sec --
            accuracy check -- {round(sum(self.get_percents_()), 2)}% --
            top_end: {max(self.unique_)}


        Unr_16_: {len(self.unr_16_)}   \t\t{round((self.get_percents_())[0], 2)}%   
        Ubinrs_: {len(self.ubinrs_)}   \t\t{round((self.get_percents_())[4], 2)}% 
        Udbbls_: {len(self.udbbls_)}   \t\t{round((self.get_percents_())[1], 2)}%
        Utrips_: {len(self.utrips_)}   \t\t{round((self.get_percents_())[2], 2)}%   
        Others_: {len(self.others_)}   \t\t{round((self.get_percents_())[3], 2)}% 
        Ovr999_: {len(self.ovr999_)}   \t\t{round((self.get_percents_())[5], 2)}% 
        Common_: {len(self.common_)}     \t{round((self.get_percents_())[6], 2)}%

        """)

    def json_init(self):
        try:
            with open(f'{os.getcwd()}/sandbox_/{self.name_}.json', 'x') as file:
                json_obj_ = self.jsonify_()
                new_file = json.dumps(json_obj_, indent=4)
                file.write(new_file)
        except FileExistsError:
            print("Err!! Filename in use.")

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




def main():
    # hmm_idea(250)
    trial = Minter("Test_Minter", 50000, .00005)
    trial.generator_hm()
    trial.generator_hm()
    trial.generator_hm()

    # trial.generator()
    # trial.check_unqs()



    print(trial.unr_16_)
    print(trial.ubinrs_)
    print(trial.udbbls_)
    print(trial.utrips_)
    print(trial.others_)
    print(trial.ovr999_)

main()