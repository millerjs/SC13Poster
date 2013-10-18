import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

tests = (
    "rsync",
    "udr \n(1 thread)",
    "udr \n(16 threads)",
    "udt \n(1 thread)",
    "udt \n(16 threads)",
    )

performance = (
    


y_pos = np.arange(len(tests))
performance = 3 + 10 * np.random.rand(len(tests))
error = np.random.rand(len(tests))


plt.barh(y_pos, performance, color='#174990', xerr=0, align='center', alpha=1.)
plt.yticks(y_pos, tests, weight='bold')
plt.xlabel('Average Transfer Rate', weight='bold')


for i in range(len(tests)):
    
    plt.text(performance[i]-.2, i, "%.2f Gbps" % performance[i], horizontalalignment="right",
             verticalalignment='center', color="white", weight='bold')


plt.title('Comparison of Average Transfer Rates \n Disk to Disk', weight='bold')

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0),

plt.savefig("temp3.png")
plt.show()
