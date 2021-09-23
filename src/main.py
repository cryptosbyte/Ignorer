#!/usr/bin/python3

import sys
import requests


def send_request(filename) -> str:

    res = requests.get(
        f"https://raw.githubusercontent.com/github/gitignore/master/{filename}.gitignore")

    return res.text


def write_file(data) -> None:

    with open(".gitignore", "w") as file:

        file.write(data) and exit(0)

    return


def main():

    gitignore_file = sys.argv[1]
    res = send_request(gitignore_file)

    if "404: Not Found" in res:
        print("Invalid GitIgnore File") 
        exit(1)

    if res.endswith(".gitignore"):
        res = send_request(res[:-10])

        write_file(res)

    else:

        write_file(res)


main()
