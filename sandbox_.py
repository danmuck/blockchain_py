import math, datetime, os, json
from random import randint
import time

'''
        4 places 00.00




'''
# int(time.strftime('%M%H%S%j%I%m'))

def hmm_idea(iters_:int):

    common_ = []
    unr_16_ = [] # rares
    ovr999_ = [] # over 999
    zeroes_ = [] # literal zeroes
    others_ = [] # some fun ones


    others_list = [
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
    start_time = time.time()
    nanos_ = (time.time_ns() + randint(1, 4096) * math.pi)
    i, j = 1, iters_
    while i <= j:
        i+=1
        time.sleep(.002)
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
        elif ez_nums in others_list:
            print(f"!! --   {ez_nums}   \t -- !!")
            others_.append(ez_nums)
        else:
            # print(ez_nums)
            common_.append(ez_nums)

    unr_16_p = (len(unr_16_) / j) * 100
    zeroes_p = (len(zeroes_) / j) * 100
    ovr999_p = (len(ovr999_) / j) * 100
    others_p = (len(others_) / j) * 100
    common_p = (len(common_) / j) * 100

    percents_ = [
        unr_16_p,
        zeroes_p,
        ovr999_p,
        others_p,
        common_p,
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

        Ez_nums: {len(unr_16_)}   \t\t{round(unr_16_p, 2)}%   
        Zeros__: {len(zeroes_)}   \t\t{round(zeroes_p, 2)}% 
        Ovr999_: {len(ovr999_)}   \t\t{round(ovr999_p, 2)}% 
        Others_: {len(others_)}   \t\t{round(others_p, 2)}% 
        Common_: {len(common_)}   \t\t{round(common_p, 2)}%   
    """)


# FILES ---

    with open(f'{os.getcwd()}/sandbox_/iterations.txt', 'a') as file:
        file.write(f"""
    {j} Iterations took {round(time.time() - start_time, 2)}sec 
        accuracy check -- {round(sum(percents_), 2)}%

        Ez_nums: {len(unr_16_)}   \t\t{round(unr_16_p, 2)}%   
        Zeros__: {len(zeroes_)}   \t\t{round(zeroes_p, 2)}% 
        Ovr999_: {len(ovr999_)}   \t\t{round(ovr999_p, 2)}% 
        Others_: {len(others_)}   \t\t{round(others_p, 2)}% 
        Common_: {len(common_)}   \t\t{round(common_p, 2)}%   
    """)
    with open(f'{os.getcwd()}/sandbox_/nc_data.txt', 'a') as file:
        file.write(f"""
Data:

Ez_nums: {sorted(unr_16_)}

Zeros__: {sorted(zeroes_)}

Ovr999_: {sorted(ovr999_)}

Others_: {sorted(others_)}

Common_: {sorted(common_)}

    """)


        


def main():
    hmm_idea(20000)
main()