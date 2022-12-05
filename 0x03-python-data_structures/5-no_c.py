#!/usr/bin/python3

def no_c(my_string):
    copy_string = my_string[:]
    j = 0

    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            copy_string = copy_string[:(i - j)] + my_string[(i + 1):]
            j += 1

    return (copy_string)
