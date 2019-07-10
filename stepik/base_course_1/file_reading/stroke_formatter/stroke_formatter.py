import os
import re

path_to_read_file = os.path.join('in.txt')
path_to_write_file = os.path.join('out.txt')
words_pattern = re.compile(r'[0-9+]')
numbers_pattern = re.compile(r'[^0-9]')
result = ''

with open(path_to_read_file, 'r') as file_reader:
    s = file_reader.readline().strip()

words_list = re.sub(words_pattern, " ", s).split()
numbers_list = [int(i) for i in re.sub(numbers_pattern, " ", s).split()]

for i in range(len(words_list)):
    result += words_list[i] * numbers_list[i]

with open(path_to_write_file, 'w') as file_writer:
    file_writer.write(result)
