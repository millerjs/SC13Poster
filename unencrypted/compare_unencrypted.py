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
    "netcat",
    "UDR[rsync]",
    "UDR[scp]",
    "UDTCAT disk to disk",
    "UDTCAT memory to memory"
    # "UDTCAT RTT = 1ms memory to memory",
    )

performance = (
    0.8222425,
    1.28,
    1.25,
    4.894,
    5.41,
    # 7.46,
)

stddev = (
.03,
.28,
.04,
.75,
.05,
# 1.07,
)


y_pos = np.arange(len(tests))
error = np.random.rand(len(tests))

plt.barh(y_pos, performance, color='#174990', xerr=0, align='center', alpha=1.)
plt.yticks(y_pos, tests, weight='bold')
plt.xlim(0, 6.5)
# plt.xlim(0, 8.5)
plt.xlabel('Average Transfer Rate', weight='bold')

for i in range(len(tests)):
    
    plt.text(performance[i]+.5, i, "%.2f Gbps\n$\sigma=%.2f$ $Gbps$" % (performance[i], stddev[i]), horizontalalignment="center",
             verticalalignment='center', color="black", weight='bold')

plt.title('Comparison of Average Unencrpyted \n Transfer Rates', weight='bold')

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0),
plt.savefig("compare_unencrypted.png")
# plt.show()
