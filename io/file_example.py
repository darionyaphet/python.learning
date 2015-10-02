#! usr/bin/python
#coding=utf-8

'''
    File objects are implemented using C’s stdio package and can be created with the built-in open() function
'''


with open('resource/file/input') as input_file:
    for line in input_file:
        print line
