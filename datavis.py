import matplotlib.pyplot as plt
from pylab import rcParams
from datetime import datetime
import base64
from io import BytesIO
def PlotData(w_list, title, lim):
    # now plotting the data into a barH graph (horizontal bar)
    plt.title("Bar Chart with " + title + " word(s)")
    plt.xlabel('Word')
    plt.ylabel('Occurences')
    now = datetime.now()
    if(len(w_list) > lim):
        for i in range(len(w_list) - lim):
            w_list.popitem()
    plt.barh(*zip(*w_list.items()))
    plt.tight_layout()
    plt.gcf().set_size_inches(10, 30)
    plt.savefig("pics/" + str(now) + ".png", bbox_inches='tight', dpi=1000)
    plt.show()
