#!/bin/bash
rm -rf chain_data/ minter_data/;

read -p "This option will also nuke Master_chain and Wallet data.. Clean all? (y/N): " clean_all
if [ "$clean_all" == "y" ]
then
    rm -rf Master_chain.json user_data/
elif [ "$clean_all" == "Y" ]
then
    rm -rf Master_chain.json user_data/
elif [ "$clean_all" == "" ]
then
    :
else
    :
fi

./ctl_center.py