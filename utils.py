import os

def open_file(filename: str):
    return open(filename).read()

def split_lines(filename: str):
    return open(filename).read().splitlines()
