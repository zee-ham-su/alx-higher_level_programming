#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_dic = {}
    for number in my_list:
        uniq_dic[number] = True
    total = sum(uniq_dic.keys())
    return total
