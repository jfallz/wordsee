import matplotlib.pyplot as plt
from pylab import rcParams
from datetime import datetime
import base64
from io import BytesIO
import time

def PlotData(w_list, title, lim):
    # now plotting the data into a barH graph (horizontal bar)
    plt.title("Bar Chart with " + title + " word(s)")
    plt.xlabel('Occurrences')
    plt.ylabel('Word')
    now = datetime.now()
    # if(len(w_list) > lim):
    #     for i in range(len(w_list) - lim):
    #         w_list.popitem()
    plt.barh(*zip(*w_list.items()))
    plt.tight_layout()
    if(len(w_list)/3 > 35):
        length = 35
    else:
        length = len(w_list)/3
    plt.gcf().set_size_inches(12, length)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    CreateHTML(data, w_list)
    plt.clf()

def CreateHTML(datainput, your_dict):
    html = "<div>\n <img src=\"data:image/png;base64, " + str(datainput) + "\" alt=\"Graph\"/>\n<p>"
    for item in your_dict.items():
        html += str(item) + "<br>"
    html += "</p></div>"
    f = open("pages/" + str(datetime.now()) + ".html", "w")
    f.write(html)
    f.close()

