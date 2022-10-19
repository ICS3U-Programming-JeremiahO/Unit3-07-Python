#!/usr/bin/env python3
# Created By: Jeremiah omoike
# Date: October 18 2022
# This program gets an age from user and calculates whether a person who is that age is eligible to date my grand child 


from logging import exception


def main():
    # input age
    user_age_as_string = input("please input age here : ")
    try:
        # cast user input from string to an int
        user_age_as_int = int(user_age_as_string)
        # process and output: check whether age is less than 25 AND more than 40 or not
        if user_age_as_int > 25 and user_age_as_int < 40:
            print("I approve of you dating my grandchild.")
        else:
            print("You are not fit to date my grandchild.")
    except Exception:
        print("this is not an integer")
    finally:
        print("Thank you for taking an interest in dating my grandchild.")


if __name__ == "__main__":
    main()
