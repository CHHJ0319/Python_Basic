#예제1
import os

def read_folder(path):
    output1 = os.listdir(path)
    for element in output1:
        if os.path.isdir(element):
            read_folder(element)
        else:
            print("파일: ", element)

read_folder(".")