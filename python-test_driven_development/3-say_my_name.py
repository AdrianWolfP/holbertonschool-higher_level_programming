#!/usr/bin/python3
""" function that prints My name is <first name> <last name> """


ErrMsgFirst = "first_name must be a string"
ErrMsgLast = "last_name must be a string"


def say_my_name(first_name, last_name=""):
    """ function that prints My name is <first name> <last name> """
    if type(first_name) is not str:
        raise TypeError(ErrMsgFirst)
    if type(last_name) is not str:
        raise TypeError(ErrMsgLast)
    else:
        print("My name is {} {}".format(first_name, last_name))
