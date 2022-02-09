import math, datetime, os, json
from random import randint
import time

'''
        4 places 00.00

'''
# int(time.strftime('%M%H%S%j%I%m'))


OTHERS_LIST = [
        420,
        69,
        1111,
        1234,
        999,
        666,
        123,
        111,
        222,
        333,
        444,
        555,
        666,
        777,
        888,
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
class Minter:
    def __init__(self, iters_:int) -> None:
        self.unr_16_ = [] # rares
        self.udbbls_ = [] # uncommon
        self.others_ = [] # some fun ones
        self.zeroes_ = [] # literal zeroes
        self.ovr999_ = [] # over 999
        self.common_ = []
        self.start_time = time.time()
        self.iters_ = iters_

    def generator(self):
        nanos_ = (time.time_ns() + randint(1, 4096) * math.pi)
        i, j = 1, self.iters_
        while i <= j:
            i+=1
            time.sleep(.0025)
            ez_nums = int( ((nanos_ * randint(1, 4097)) * int(time.strftime('%S'))) % 1023 )
            if ez_nums <= 15 and ez_nums != 0:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.unr_16_.append(ez_nums)
            elif ez_nums in UDBBLS_LIST:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.udbbls_.append(ez_nums)            
            elif ez_nums in OTHERS_LIST:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.others_.append(ez_nums)
            elif ez_nums == 0:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.zeroes_.append(ez_nums)
            elif ez_nums > 999:
                print(f"!! --   {ez_nums}   \t -- !!")
                self.ovr999_.append(ez_nums)
            else:
                # print(ez_nums)
                self.common_.append(ez_nums)        

    def get_percents_(self) -> list:
        unr_16_p = (len(self.unr_16_) / self.iters_) * 100
        udbbls_p = (len(self.udbbls_) / self.iters_) * 100
        others_p = (len(self.others_) / self.iters_) * 100
        zeroes_p = (len(self.zeroes_) / self.iters_) * 100
        ovr999_p = (len(self.ovr999_) / self.iters_) * 100
        common_p = (len(self.common_) / self.iters_) * 100
        percents_ = [
            unr_16_p,
            udbbls_p,
            others_p,
            zeroes_p,
            ovr999_p,
            common_p,
        ]
        return percents_


    def summary_to_console(self):
        print(f"""
    Data:

    Ez_nums: {sorted(self.unr_16_)}

    Zeros__: {sorted(self.zeroes_)}

    Ovr999_: {sorted(self.ovr999_)}

    Others_: {sorted(self.others_)}

    Common_: [disabled for now]
        """)
        print(f"""
        {j} Iterations took {round(time.time() - self.start_time, 2)}sec 
            accuracy check -- {round(sum(self.get_percents_()), 2)}%

            Ez_nums: {len(self.unr_16_)}   \t\t{round((self.get_percents_())[0], 2)}%   
            udbbls_: {len(self.udbbls_)}   \t\t{round((self.get_percents_())[1], 2)}%   
            Others_: {len(self.others_)}   \t\t{round((self.get_percents_())[2], 2)}% 
            Zeros__: {len(self.zeroes_)}   \t\t{round((self.get_percents_())[3], 2)}% 
            Ovr999_: {len(self.ovr999_)}   \t\t{round((self.get_percents_())[4], 2)}% 
            Common_: {len(self.common_)}     \t{round((self.get_percents_())[5], 2)}%

        """)


    # FILES ---
    def print_log_txt(self):
        with open(f'{os.getcwd()}/sandbox_/iterations.txt', 'a') as file:
            file.write(f"""
        {j} Iterations took {round(time.time() - start_time, 2)}sec 
            accuracy check -- {round(sum(self.get_percents_()), 2)}%

            Ez_nums: {len(self.unr_16_)}   \t\t{round((self.get_percents_())[0], 2)}%   
            udbbls_: {len(self.udbbls_)}   \t\t{round((self.get_percents_())[1], 2)}%   
            Others_: {len(self.others_)}   \t\t{round((self.get_percents_())[2], 2)}% 
            Zeros__: {len(self.zeroes_)}   \t\t{round((self.get_percents_())[3], 2)}% 
            Ovr999_: {len(self.ovr999_)}   \t\t{round((self.get_percents_())[4], 2)}% 
            Common_: {len(self.common_)}     \t{round((self.get_percents_())[5], 2)}%

        """)







def hmm_idea(iters_:int):

    common_ = []
    unr_16_ = [] # rares
    ovr999_ = [] # over 999
    zeroes_ = [] # literal zeroes
    others_ = [] # some fun ones
    udbbls_ = [] # uncommon

    start_time = time.time()
    nanos_ = (time.time_ns() + randint(1, 4096) * math.pi)
    i, j = 1, iters_
    while i <= j:
        i+=1
        time.sleep(.0025)
        ez_nums = int( ((nanos_ * randint(1, 4097)) * int(time.strftime('%S'))) % 1023 )

        if ez_nums <= 15 and ez_nums != 0:
            print(f"!! --   {ez_nums}   \t -- !!")
            unr_16_.append(ez_nums)
        elif ez_nums == 0:
            print(f"!! --   {ez_nums}   \t -- !!")
            zeroes_.append(ez_nums)
        elif ez_nums > 999:
            print(f"!! --   {ez_nums}   \t -- !!")
            ovr999_.append(ez_nums)
        elif ez_nums in OTHERS_LIST:
            print(f"!! --   {ez_nums}   \t -- !!")
            others_.append(ez_nums)
        elif ez_nums in UDBBLS_LIST:
            print(f"!! --   {ez_nums}   \t -- !!")
            udbbls_.append(ez_nums)            
        else:
            # print(ez_nums)
            common_.append(ez_nums)

    unr_16_p = (len(unr_16_) / j) * 100
    zeroes_p = (len(zeroes_) / j) * 100
    ovr999_p = (len(ovr999_) / j) * 100
    others_p = (len(others_) / j) * 100
    common_p = (len(common_) / j) * 100
    udbbls_p = (len(udbbls_) / j) * 100


    percents_ = [
        unr_16_p,
        zeroes_p,
        ovr999_p,
        others_p,
        common_p,
        udbbls_p,
    ]





    print(f"""
Data:

Ez_nums: {sorted(unr_16_)}

Zeros__: {sorted(zeroes_)}

Ovr999_: {sorted(ovr999_)}

Others_: {sorted(others_)}

Common_: [disabled for now]
    """)

    print(f"""
    {j} Iterations took {round(time.time() - start_time, 2)}sec 
        accuracy check -- {round(sum(percents_), 2)}%

        Common_: {len(common_)}     \t{round(common_p, 2)}%
        Ez_nums: {len(unr_16_)}   \t\t{round(unr_16_p, 2)}%   
        Zeros__: {len(zeroes_)}   \t\t{round(zeroes_p, 2)}% 
        Ovr999_: {len(ovr999_)}   \t\t{round(ovr999_p, 2)}% 
        Others_: {len(others_)}   \t\t{round(others_p, 2)}% 
        udbbls_: {len(udbbls_)}   \t\t{round(udbbls_p, 2)}%   

    """)


# FILES ---

    with open(f'{os.getcwd()}/sandbox_/iterations.txt', 'a') as file:
        file.write(f"""
    {j} Iterations took {round(time.time() - start_time, 2)}sec 
        accuracy check -- {round(sum(percents_), 2)}%

        Common_: {len(common_)}     \t{round(common_p, 2)}%   
        Ez_nums: {len(unr_16_)}   \t\t{round(unr_16_p, 2)}%   
        Zeros__: {len(zeroes_)}   \t\t{round(zeroes_p, 2)}% 
        Ovr999_: {len(ovr999_)}   \t\t{round(ovr999_p, 2)}% 
        Others_: {len(others_)}   \t\t{round(others_p, 2)}% 
        udbbls_: {len(udbbls_)}   \t\t{round(udbbls_p, 2)}%   

    """)
    with open(f'{os.getcwd()}/sandbox_/nc_data.txt', 'a') as file:
        file.write(f"""
Data:

Ez_nums: {sorted(unr_16_)}

Zeros__: {sorted(zeroes_)}

Ovr999_: {sorted(ovr999_)}

Others_: {sorted(others_)}

Common_: disabled

    """)

def json_record(file_name:str):
    try:
        with open(f'{os.getcwd()}/sandbox_/data.json', 'x') as file:
            json_obj_ = jsonify_("init_run", unr_16_, udbbls_, others_, zeroes_, ovr999_)
            new_file = json.dumps(json_obj_, indent=2)
            file.write(new_file)
    except FileExistsError:
        print("Err!! Filename in use.")
    except FileNotFoundError:
        with open(f'{os.getcwd()}/sandbox_/data.json', 'x') as file:
            json_fp = jsonify_("init_run", unr_16_, udbbls_, others_, zeroes_, ovr999_)
            file.write(json_fp)

def jsonify_(title:str, unr_16:list, udbbls:list, others:list, zeroes:list, ovr999:list) -> dict:
    new_dict = {
        f"{title}": {
            "UNR_16": unr_16,
            "udbbls": udbbls,
            "others": others,
            "zeroes": zeroes,
            "ovr999": ovr999,
        }
    }
    json_list = json.dumps(new_dict, indent=4)
    return new_dict




def main():
    hmm_idea(250)
main()