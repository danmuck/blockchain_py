import os, json, datetime

def menu_(choices:list):
    menu_opts = {}
    i, j = 0, len(choices)
    while i < j:
        if i == 0:
            menu_opts.update({i: "[QUIT]"})
        else:
            menu_opts.update({i: choices[i]})
        i+=1
    print(menu_opts)


def main():
    choices = [
        "[Tasks]",
        "[Personal]",
        "[Tools]",
        "[Projects]",
        "[Finance]",
        "[Users]",
        "[Learning Tools]",
        "[Games]",
    ]
    menu_(choices)

main()