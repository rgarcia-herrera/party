import argparse
import matplotlib.pyplot as plt
import csv
import networkx as nx


parser = argparse.ArgumentParser(description='plot simulation from log')
parser.add_argument('log', type=argparse.FileType('r'), help='log file')
args = parser.parse_args()

csvr = csv.reader(args.log)

t = []
h = []
b = []
for row in csvr:
    t.append(row[0])
    h.append(row[1])
    b.append(row[2])

# scatter plots
plt.plot(t, h, 'r', t, b, 'b')
plt.show()
#plt.title("node levels")
#plt.ylabel("level")
#plt.xlabel("seconds")

#plt.axes([0.45,0.45,0.45,0.45])
#plt.axis('off')
