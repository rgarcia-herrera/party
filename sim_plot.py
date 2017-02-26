import argparse
import matplotlib.pyplot as plt
import csv
import networkx as nx


parser = argparse.ArgumentParser(description='plot simulation from log')
parser.add_argument('--log', type=argparse.FileType('r'), help='path to log file')
parser.add_argument('--fig', type=argparse.FileType('w'), help='path to write figure')
args = parser.parse_args()

csvr = csv.reader(args.log)

t = []
h = []
b = []
for row in csvr:
    t.append(row[0])
    h.append(row[1])
    b.append(row[2])

plt.plot(t, h, 'r', t, b, 'b')

# Two subplots, the axes array is 1-d
f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(t, h, 'r')
axarr[0].set_title('Happy party goers')
axarr[1].plot(t, b, 'b')
axarr[1].set_title('Same sex groups')

plt.savefig(args.fig)
