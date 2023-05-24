#!/usr/bin/python3
""" fucntion that prints a text with 2 new lines after/
    each of these characters: ., ?, and : """


def text_indentation(text):
    """ prints a string of text with 2 new lines after '.', '?', and ':' """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char == '.' or char == '?' or char == ':':
            print(char, end="")
            print("\n")
        else:
            print(char, end="")
