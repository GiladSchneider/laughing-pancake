import os
def analyze(fileNum):
    f = open('Data/data%s.txt' %(fileNum), 'r')
    sum = 0
    for line in f:
        for num in line.strip().split(','):
            if(num == ''):
                return sum
            else:
                sum = sum + int(num)
    f.close
    return sum


def average(total):
    avg = total//50
    return avg


def main():
    for i in range (1):
        totalComp = analyze(i)
        averageComp = average(totalComp)
        f = open("Data/data5.txt" ,"a")
        f.write("" + str(averageComp) + ",")
        f.close

main()