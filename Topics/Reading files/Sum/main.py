# read sums.txt
with open("sums.txt", "r") as f:
    for line in f:
        print(sum(int(a) for a in line.split()))
