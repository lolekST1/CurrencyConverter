# read sample.txt and print the number of lines
with open("sample.txt", "r") as f:
    print(len(f.readlines()))
