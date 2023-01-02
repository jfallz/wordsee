import matplotlib.pyplot as plt
from datetime import datetime
def PlotData(w_list, title):
    # now plotting the data into a barH graph (horizontal bar)
    plt.barh(*zip(*w_list.items()))
    plt.title("Bar Chart with " + title + " word(s)")
    plt.xlabel('Word')
    plt.ylabel('Occurences')
    now = datetime.now()
    plt.savefig(str(now) + ".pdf")
    plt.show()

