#!/bin/bash

read -p "This option will also nuke Master_chain and Wallet data.. Clean all? (Y/n): " clean_all
if [ "$clean_all" == "y" ]
then
    rm -rf Master_chain.json user_data/
    rm -rf chain_data/ minter_data/;

elif [ "$clean_all" == "Y" ]
then
    rm -rf Master_chain.json user_data/
    rm -rf chain_data/ minter_data/;

elif [ "$clean_all" == "" ]
then
    rm -rf Master_chain.json user_data/
    rm -rf chain_data/ minter_data/;

else
    :
fi

#./ctl_center.py