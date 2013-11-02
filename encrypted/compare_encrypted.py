import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


from pylab import *
rcParams['figure.figsize'] = 30, 16

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 36}

matplotlib.rc('font', **font)

tests = (
    "rsync",
    "scp",
    "UDR[rsync] threaded",
    "UDR[scp] threaded",
    "UDTCAT (disk to disk)",
    "UDTCAT (memory to memory)",
    "UDTCAT threaded (disk to disk)",
    "UDTCAT threaded (memory to memory)",
    )

performance = (
0.194176126761,
0.191090869565,
1.26881889764,
1.24770186335,
.95,
.95,
3.41,
4.58362318841,
)

stddev = (
.01,
.01,
.27,
.18,
.36,
.33,
.07,
.18
)

y_pos = np.arange(len(tests))
error = np.random.rand(len(tests))


plt.barh(y_pos, performance, color='#174990', xerr=0, align='center', alpha=1.)
plt.yticks(y_pos, tests, weight='bold')
plt.xlim(0, 6.5)
plt.xlabel('Average Transfer Rate', weight='bold')


# yaxis.grid(color='gray', linestyle='dashed
# plt.xaxis.grid(color='gray', linestyle='dashed')



for i in range(len(tests)):
    plt.text(performance[i]+.6, i, "%.2f Gbps\n$\sigma=%.2f$ $Gbps$" % (performance[i], stddev[i]), horizontalalignment="center",
             verticalalignment='center', color="black", weight='bold')



plt.title('Comparison of Average Encrypted \nTransfer Rates ', weight='bold')

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0),

plt.savefig("compare_encrypted.png")
# plt.show()
