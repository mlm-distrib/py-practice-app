# Working with files in Python is the open() function
# open() takes two parameters
# 1.File name
# 2.mode
# Modes:
# r => read, Default value. Opens a file for reading, error if the file does not exist
# a => append, Opens a file for appending, creates the file if it does not exist
# w => write, Opens a file for writing, creates the file if it does not exist
# x => Creates the specified file, returns an error if the file exists
# t => text mode
# b => binary mode (eg. images)

import os

# write file

f = open('test.txt', 'w')
f.write('this is a test message')
f.close()

# read file
f = open('test.txt', 'r')
print(f.read())
f.close()

if os.path.exists('test.txt'):
    print('file exists')
    os.remove('test.txt')
    print('file deleted')
