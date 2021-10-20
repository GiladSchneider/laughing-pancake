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

def calcOps(fNum):
    f = open('Data/temp.txt', 'r') #read temp file
    sum = 0
    for line in f:
        for num in line.strip().split(','):
            if(num == ''):
                break
            else:
                sum = sum + int(num)
    f.close

    f = open('Data/data%s.txt' %(fNum), 'a') # add calc numbers to target data file
    f.write("" + str(sum) + ",")
    f = open('Data/temp.txt', 'w') #reset the temp file
    f.close()
    return

def addtemp(Count):
        f = open("Data/temp.txt" ,"a")
        f.write("" + str(Count) + ",")
        f.close
        return

def resetData(fileNum):
    f = open('Data/data%s.txt' %(fileNum), 'w')
    f.close
    return

def main():
    f = open("Data/data5.txt", "w")
    f.close
    for i in range (4):
        totalComp = analyze(i)
        averageComp = average(totalComp)
        f = open("Data/data5.txt" ,"a")
        f.write("" + str(averageComp) + ",")
        f.close


main()