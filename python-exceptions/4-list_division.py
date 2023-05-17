#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
    try:
        new_list.append(my_list_1[i] / my_list_2[i])
    except TypeError:
        print("Wrong type")
        new_list.append(0)
    except ZeroDivisionError:
        print("Division by 0")
        new_list.append(0)
    except IndexError:
        print("Out of range")
        new_list.append(0)
    finally:
        pass
    return new_list
