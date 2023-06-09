# todo:
#   fix logs so they do not compound results of multiple runs

# from .No_funs import No_fun
import json
import os
import time
from operator import itemgetter
from random import randint

from modules.chain_ctl.minter.no_funs.No_Fun import (
    No_fun,
    ez_random,
    UBINRS_LIST,
    UDBBLS_LIST,
    UTRIPS_LIST,
    OTHERS_LIST,
)
from modules.chain_ctl.minter.no_funs.No_Fun_Utils import UNR_16_MAP
from modules.chain_ctl.Proof_of_Work import Proof_of_Work, Blockchain_
from modules.chain_ctl.utilities.Debug import DEBUG_MODE


class Minter_:
    unr_16_ = []  # < 16
    ubinrs_ = []  # binaries
    udbbls_ = []  # doubles
    utrips_ = []  # triples
    others_ = []  # some fun ones
    uppers_ = []  # > 999
    common_ = []  # the rest
    master_ = []
    chain: Blockchain_
    name_: str
    wallet_: str

    def __init__(
        self,
        chain: Blockchain_,
        wallet: str = "_",
        name_: str = "Minter",
        iters_: int = 256000,
        sleep_time: float = 0,
        quick: bool = False,
    ) -> None:
        self.chain = chain
        self.wallet_ = wallet
        self.unique_ = []  # uniques in a given session
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
        self.start_time = time.time()
        if quick is True:
            self.iters_ = 1
            self.sleep_time = 0
        else:
            self.iters_ = iters_
            self.sleep_time = sleep_time
            self.init_new_minter(name_)

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
        i, j = 1, self.iters_  # i is always magical
        bins_, eq_count = 0, self.landed  # currently necessary
        rando_0, rando_1, rando_2, rando_3 = 0, 0, 0, 0
        ez_rand = ez_random()
        while i <= j:
            i += 1
            time.sleep(self.sleep_time)
            # ez_rand = self.ez_rand()
            ez_rand = ez_random()

            rando_0 = randint(0, 256) + randint(0, 1)
            rando_1 = randint(1, 512) + randint(0, 1)
            rando_2 = randint(0, 1024) + randint(0, 1)
            rando_3 = randint(1, 768) + randint(0, 1)
            self.master_.append(ez_rand.return_)
            unique_bool = False
            if rando_0 == rando_1 and rando_2 <= rando_3:
                self.landed = eq_count
                unique_bool = True
                if ez_rand.return_ <= 1234 or (
                    ez_rand.return_ > 1234 and ez_rand.return_ == randint(0, 9999999)
                ):
                    block_chain_data = No_fun(ez_rand).get_attrs()
                    eq_count += 1
                    if ez_rand.return_ > 1234:
                        if DEBUG_MODE > 0:
                            print("\t\t  !!Wowzers::")
                        self.others_.append("VOID")
                else:
                    block_chain_data = {}
                proof = Proof_of_Work(self.chain, self.wallet_, "0010")
                # init no_fun txn
                # txn = Txn_("to_address", self.chain.get_tallest_block[0], block_chain_data, amount, miner_fee)
                proof.mine_block(txns={}, txn_data=block_chain_data)

                # logs stuff
                self.print_minter_heys(ez_rand.return_)
                if DEBUG_MODE > 2:
                    print(f"iter_count: {i}")
            else:
                pass
            self.unique_check_(ez_rand.return_, unique_bool)
        # print("UNIQUE_FULL: ",sorted(self.unique_))

        self.end_timer()
        if self.iters_ != 1:
            if DEBUG_MODE > 2:
                self.summary_to_console()
            self.print_log_file()
            if DEBUG_MODE > 2:
                print("  \nzero counter: ", self.zero_counter, "\n\n")
        elif self.iters_ == 1:
            if rando_0 == rando_1 and rando_2 <= rando_3:
                if DEBUG_MODE > 0:
                    print("!!== ZOMG LANDED A SOLO BOII ==!!")
        return ez_rand.return_

    def print_minter_heys(self, ez_rand: int):
        bins_ = 0
        if ez_rand in UBINRS_LIST:
            bins_ += 1
            self.real_binaries_landed_ = bins_
            if ez_rand <= 15 and ez_rand != 0:
                if DEBUG_MODE > 0:
                    print(f"\n!!Hey Unr_16::{UNR_16_MAP[ez_rand]}  !!\n")
                self.unr_16_.append(ez_rand)
            elif ez_rand != 0:
                if DEBUG_MODE > 0:
                    print(f"\n!!Hey Bnr_16::{str(ez_rand).zfill(4)}  !!\n")
                self.ubinrs_.append(ez_rand)
            else:
                self.zero_counter += 1
                if DEBUG_MODE > 0:
                    print(f"!!Hey Zero::{UNR_16_MAP[ez_rand]}  !!\n")
                self.unr_16_.append(ez_rand)
        elif ez_rand in UDBBLS_LIST:
            if DEBUG_MODE > 0:
                print(f"!!Hey Doubles::{ez_rand}  !!\n")
            self.udbbls_.append(ez_rand)
        elif ez_rand in UTRIPS_LIST:
            if DEBUG_MODE > 0:
                print(f"!!Hey Triples::{ez_rand}  !!\n")
            self.utrips_.append(ez_rand)
        elif ez_rand in OTHERS_LIST:
            if DEBUG_MODE > 0:
                print(f"!!Hey Rare::{ez_rand}  !!\n")
            self.others_.append(ez_rand)
        elif 999 < ez_rand <= 1234:
            if DEBUG_MODE > 0:
                print(f"!!Hey Upper::{ez_rand}  !!\n")
            self.uppers_.append(ez_rand)
        elif ez_rand <= 1234:
            if DEBUG_MODE > 0:
                print(f"!!Hey Common::{ez_rand}  !!\n")
            self.common_.append(ez_rand)
        else:
            if DEBUG_MODE > 0:
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
        totals_p = sum(main_list_)
        real_binary_p = sum(main_list_[0:2])

        percents_ = [totals_p, real_binary_p]
        percents_.extend(main_list_)
        return percents_

    def unique_check_(self, int_: int, check: bool):
        """

        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!! REDUNDANT BOOLEAN CHECK                !!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        """
        if check is True:
            if int_ not in self.unique_ and int_ <= 1234:
                self.unique_.append(int_)
                if DEBUG_MODE > 2:
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
        if DEBUG_MODE > 2:
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
        if DEBUG_MODE > 2:
            for i, j in some_dict.items():
                print(f"{i}:\t{j}")
            print(len(some_dict), "/1235 total uniques (excluding commons)")

    def run_timer(self):
        self.start_time = time.time()
        return self.start_time

    def end_timer(self):
        return round(time.time() - self.start_time, 2)

    def summary_to_console(self):
        print(
            f"""
    # Data:
        [showing only unique lands]
    Unr_16_: {sorted(list(set(self.unr_16_)))}   
    Ubinrs_: {sorted(list(set(self.ubinrs_)))}  
    Udbbls_: {sorted(list(set(self.udbbls_)))}  
    Utrips_: {sorted(list(set(self.utrips_)))}   
    Others_: {sorted(list(set(self.others_)))}  
    Uppers_: {sorted(list(set(self.uppers_)))}  
    Common_: {sorted(list(set(self.common_)))}
        """
        )
        print(
            f"""
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

        """
        )

    # FILES ---
    def history_counts(self):
        hist_dict = []
        if self.name_ != "Q_MINT":
            for i in range(0, 1235):
                for j in self.history.keys():
                    if i in self.history.get(j):
                        hist_dict.append(
                            {"num": i, "count": self.history.get(j).count(i)}
                        )
                        # time.sleep(self.sleep_time)
            sorted_list = sorted(hist_dict, key=itemgetter("count"))
            with open(
                f"{os.getcwd()}/minter_data/{self.name_}_counts.json", "w"
            ) as file:
                file.write(json.dumps(sorted_list, indent=2))

    def print_log_file(self):
        if self.name_ != "Q_MINT":
            with open(f"{os.getcwd()}/minter_data/{self.name_}_log.txt", "a") as file:
                if self.iters_ > 750:
                    file.write(
                        f"""
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

            """
                    )

    def init_new_minter(self, name_: str):
        if self.name_ != "Q_MINT":
            try:
                with open(f"{os.getcwd()}/minter_data/{name_}_log.txt", "x") as file:
                    file.write(f"Minter_{name_}")
            except FileExistsError:
                pass
            finally:
                try:
                    with open(
                        f"{os.getcwd()}/minter_data/{name_}_history.json", "x"
                    ) as file:
                        file.write(
                            json.dumps(
                                {
                                    "UNR_16": [],
                                    "UBINRS": [],
                                    "UDBBLS": [],
                                    "UTRIPS": [],
                                    "OTHERS": [],
                                    "UPPERS": [],
                                    "COMMON": [],
                                },
                                indent=2,
                            )
                        )
                except FileExistsError:
                    pass

    def update_history_json(self):
        if self.name_ != "Q_MINT":
            with open(
                f"{os.getcwd()}/minter_data/{self.name_}_history.json", "r"
            ) as file:
                minter_data = dict(json.load(file))
                self.history["UNR_16"].extend(list(minter_data["UNR_16"]))
                self.history["UBINRS"].extend(list(minter_data["UBINRS"]))
                self.history["UDBBLS"].extend(list(minter_data["UDBBLS"]))
                self.history["UTRIPS"].extend(list(minter_data["UTRIPS"]))
                self.history["OTHERS"].extend(list(minter_data["OTHERS"]))
                self.history["UPPERS"].extend(list(minter_data["UPPERS"]))
                self.history["COMMON"].extend(list(minter_data["COMMON"]))
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
