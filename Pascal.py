#Nicholas Feanny; naf16b

rows = int(input("Enter the number of rows: "))
previous = [1, 1]
next = []

def printRow(previous):
    for i in previous:
        print("{} ".format(i), end='')

def printTriangle(rows, previous, next):
    for i in range(rows):

        if i == 0:
            print("1", end='')
        else:
            printRow(previous)

            next.append(1)

            for j in range(0, i):
                next.insert(j + 1, (previous[j] + previous[j + 1]))

            next.append(1)
            
            #del previous[:]
            previous = next[:]
            del next[:]

        print('')

#why doesn't this work???????
#next[:] = []

printTriangle(rows, previous, next)
