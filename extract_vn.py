import csv
import sys
from pylab import *
from numpy import *
from scipy import *
from scipy import optimize


resolution=5


def vntoi(x, label):
    if "k" in label:
        return float(x)/1e6
    if "M" in label:
        return float(x)/1e3
    if "G" in label:
        return float(x)

def find_bit(row):
    bits = []
    for x in range(len(row)):
        if "bit" in row[x]:
            bits.append(x)
    return bits


path=sys.argv[1]

rxs = []
txs = []
with open(path, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        bits = find_bit(row)
        RX_LOC = bits[0]
        TX_LOC = bits[1]
        rx_string = row[RX_LOC-1]
        rx_label = row[RX_LOC]
        tx_string =  row[TX_LOC-1]
        tx_label =  row[TX_LOC]
        rx = vntoi(rx_string, rx_label)
        tx = vntoi(tx_string, tx_label)
        rxs.append(rx)
        txs.append(tx)

print  "%.2f\t%.2f" % (mean(rxs),std(rxs))
