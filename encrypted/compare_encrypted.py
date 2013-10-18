import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


from pylab import *
rcParams['figure.figsize'] = 30, 12

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 36}

matplotlib.rc('font', **font)

tests = (
    "rsync",
    "scp",
    "UDR[rsync] threaded & single-thread",
    "UDR[scp] threaded & single-thread",
    "UDTCAT (disk to disk)",
    "UDTCAT threaded (disk to disk)",
    "UDTCAT (memory to memory)",
    "UDTCAT threaded (memory to memory)",
    )

performance = (
0.194176126761,
0.191090869565,
1.26881889764,
1.24770186335,
0.954241380952,
3.29617647059,
0.809574539474,
4.58362318841,
)

y_pos = np.arange(len(tests))
error = np.random.rand(len(tests))

plt.barh(y_pos, performance, color='#174990', xerr=0, align='center', alpha=1.)
plt.yticks(y_pos, tests, weight='bold')
plt.xlim(0, 8)
plt.xlabel('Average Transfer Rate', weight='bold')


for i in range(len(tests)):
    
    plt.text(performance[i]+.2, i, "%.2f Gbps" % performance[i], horizontalalignment="left",
             verticalalignment='center', color="black", weight='bold')


plt.title('Comparison of Average Encrypted \nTransfer Rates ', weight='bold')

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0),

plt.savefig("compare_encrypted.png")
# plt.show()
