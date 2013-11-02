import csv
import sys
from pylab import *
from numpy import *
from scipy import *
from scipy import optimize


resolution=5


rcParams['figure.figsize'] = 30, 12

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 42}

matplotlib.rc('font', **font)



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



# Create plot
plt = matplotlib.pyplot.figure()
ax = axes()

def plotter(path, label):
    print "Adding %s to plot" % path
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

    rxs_ = []
    txs_ = []
    for i in range(0,len(rxs)-resolution, resolution):
        rxs_.append(mean(rxs[i:i+resolution]))
        txs_.append(mean(txs[i:i+resolution]))

    rxs=rxs_
    txs=txs_

    x = array(range(len(rxs)))*resolution
            
    bbox_to_anchor_props = dict(boxstyle="round4,pad=0.8", fc="cyan", ec="k", lw=2)
    
    xaxis = "Time (s) [%d s resolution]" % resolution
    yaxis = "Speed (Gbps)"
    
    ax.set_xlabel(xaxis)
    ax.set_ylabel(yaxis)
    
    rx_label = label
    tx_label = label
    
    if max(rxs) > .1:
        plot(x, rxs, alpha=.7, linewidth=10, label=rx_label)
    if max(txs) > .1:
        plot(x, txs, alpha=.7, linewidth=10, label=tx_label)


# Label PLot
# for i in range(1,len(sys.argv)-1):
files=[
    ["udtcat_disk_unencrypted_32.dat", "UDTCAT disk to disk unencrypted"], 
    ["udtcat_disk_encrypted_32.dat", "UDTCAT disk to disk threaded encrypytion"],
  ]


for arg in files:
    plotter(arg[0], arg[1])


# Title Plot

title="Sample data transfer with selected parameters"
ax.set_title(title)
ylim(0,10)
xlim(0,100)
# plt.tight_layout(pad=10)


# handles, labels = ax.get_legend_handles_labels()
# lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-.2))
# ax.grid('on')


# Create Legend
ax.legend( bbox_to_anchor=(1, 1),
          ncol=1, fancybox=True, shadow=True)
# , borderaxespad=1.)


ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

# Save  plot
title = insert
plt.set_facecolor('white')
plt.savefig("sample.png")
# savefig(title+".png", box_extra_artists=(lgd,), bbox_inches='tight')
# show()
        
        
