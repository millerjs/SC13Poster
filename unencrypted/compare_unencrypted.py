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
    )

performance = (
    0.8222425,
    1.13264705882,
    1.22,
    4.894,
    5.41,
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

plt.title('Comparison of Average Unencrpyted \n Transfer Rates', weight='bold')

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0),
plt.savefig("compare_unencrypted.png")
# plt.show()