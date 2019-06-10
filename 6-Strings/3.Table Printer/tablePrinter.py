#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0]*len(tableData)
    # find the maximum length of string in each list
    for i in range(len(tableData)):
        maxLen = 0
        for j in range(len(tableData[0])):
            if(len(tableData[i][j]) > maxLen):
                maxLen = len(tableData[i][j])
        colWidths[i] = maxLen

    # print the lists
    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(colWidths[i]), end=' ')
        print('\n')

printTable(tableData)