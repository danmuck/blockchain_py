from pycoingecko import CoinGeckoAPI
import os, json, datetime 
from datetime import date
cg = CoinGeckoAPI()
date_time = date.today()
# List All Supported Coins 
# all_coins = cg.get_coins_list()


coins_ = cg.get_coins_markets('usd')
new_dict = {}
for i in coins_:
    item = {i['name']: { date_time: i}}
    new_dict.update(item)
print(new_dict)
new_json = json.dumps(new_dict, indent=4, sort_keys=True)

get_my_coins = cg.get_price(ids=['bitcoin', 'dogecoin', 'ethereum'], vs_currencies=['usd'])



whole_market, choice_market = str
file_opts = [
    whole_market,
    choice_market
]

def _init_file(file_name:str) -> list:
    """
        Look for the appropriate JSON file or create a new one.

    """
    try:
        with open(f'{os.getcwd()}/coin_data/{file_name}.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        with open(f'{os.getcwd()}/coin_data/{file_name}.json', 'x') as file:
            print('new_file_created')
            return json.load(file)


def _write_market_doc(file_name, data):
    try:
        with open(f'{os.getcwd()}/coin_data/{file_name}.json', 'w') as file:
            file.write(data)
    except FileNotFoundError:
        _init_file(file_name)
        
def main():
    _write_market_doc("market_data_",new_json)
    # print(_init_file("market_data_"))

    print(get_my_coins['ethereum']['usd'])

main()
