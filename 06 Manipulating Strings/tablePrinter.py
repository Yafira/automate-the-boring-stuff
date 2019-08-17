#!/usr/bin/python3
# x and y as coordinates

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidths = [0] * len(data)
    for y in range(len(data)):
        for x in data[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)
                
    for x in range(len(data[0])):
        for y in range(len(data)):
                print(data[y][x].rjust(colWidths[y]), end = ' ')
        print()

printTable(tableData)
