#! /usr/bin/python3
# Passwords are ahashast1234, bkkindustries, amongus-je-sus

import sys, os, random


def main():
    if payload_exists() == False:
        print("Creating payload")
        create_ducky_script()
        print("Payload created into current directory.")
    else:
        print("Payload already exists")
        sys.exit()


def payload_exists():
    if os.path.exists("payload.dd"):
        return True
    else:
        return False


def generate_password():
    STRINGS = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""

    for i in range(random.randint(8, 16)):
        password += random.choice(STRINGS)

    return password


def create_ducky_script(file="payload.dd"):
    f = open(file, "w")
    f.write(
        """REM Title: Bruteforcer
REM Author:	foglar
REM Description: Tries random times to hack a pc
REM Target:	Linux
REM Version:	1.0
REM Category:	Prank
REM Source: https://github.com/foglar/
CTRL
DELAY 2000
"""
    )

    for i in range(random.randint(10, 30)):
        password = generate_password()
        f.write(
            f"""
STRING {password}
ENTER
DELAY 3000
"""
        )

    PASSWORDS = ["ahast1234", "bkkindustries", "amongus-je-sus"]
    for password in PASSWORDS:
        f.write(
            f"""
STRING {password}
ENTER
DELAY 3000
            """
        )
    f.close()


if __name__ == "__main__":
    main()
