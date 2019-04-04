import csv
import matplotlib.pyplot as plt
import sys

def main():
    data= {}
    file = csv.reader(open(sys.argv[1]))

    #grab the top line and assign it's values to keys in the data dict
    top_line = [x.strip() for x in next(file)]
    for value in top_line:
        data[value] = []

    # iterate through the file appending each colums data to its spot in the data dict
    for line in file:
        for index in range(0, len(line)):
            if index != 1:
                data[top_line[index]].append(float(line[index]))

    # convert the time MS to minutes
    data['Time'] = [x / 60000 for x in data['Time']]

    plt.plot(data[sys.argv[2]], data[sys.argv[3]])

    # naming the x axis
    plt.xlabel('x - axis: ' + sys.argv[2])
    # naming the y axis
    plt.ylabel('y - axis: ' + sys.argv[3])

    # giving a title to my graph
    plt.title(sys.argv[2] + ' VS ' + sys.argv[3])

    # function to show the plot
    plt.show()

main()
