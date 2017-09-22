# coding: utf-8

from sys import argv

script, input_file = argv

def print_all(f): # f就像一个DVD机
    print f.read()

def rewind(f):
    f.seek(0) # seek()函数的处理对象是字节而非行，所以seek(0)只是转到文件的 0 byte的位置

def print_a_line(line_count, f):
    print line_count, f.readline() # readline()里面的代码会扫描文件的每一个字节，直到找到一个\n为止，
                                   # 然后它停止读取文件，并且返回此前的文件内容。文件f会记录每次调用
                                   # readline()后的读取位置，这样它就可以在下次被调用时读取接下来的一行


current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)