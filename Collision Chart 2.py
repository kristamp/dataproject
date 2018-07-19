import csv
from collections import Counter

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
accident=[]
injury=[]
death=[]
class Accidents:
    def __init__(self, time, injury, death):
        self.time=time
        self.injury=injury
        self.death=death
def load_file (file_name):
    global data
    line_number = 0
    with open (file_name) as a:
        for line in a :
            try:
                collision_time=line.split(',')[1].split()[1]
                collision_injury=int(line.split(',')[13][1:2])
                collision_death=int(line.split(',')[14][1:2])
                line_number+=1
                print (line_number, collision_time, collision_injury, collision_death)
                if collision_time=='00:01:00"':
                    continue
                accident.append(int(collision_time[:2]))
                if collision_injury>0:
                    injury.append(int(collision_time[:2]))
                if collision_death>0:
                    death.append(int(collision_time[:2]))
            except:
                pass
    a.close()

if __name__=="__main__":
    load_file('collisions')
    a=Counter(accident)
    i=Counter(injury)
    d=Counter(death)
    data=[[],[]]
    for hour in range(24):
        print(i[hour]/a[hour])
        print(d[hour]/a[hour])
        if (i[hour]/a[hour])> 0:
            data[0].append(i[hour]/a[hour])
        if (d[hour]/a[hour])> 0:
            data[1].append(d[hour]/a[hour])
    # data=[np.array(injury),np.array(death)]
    print (data)
    num_bins = np.arange(25)-.5
    colors = ['red', 'green']
    fig, ax1 = plt.subplots()
    ax1.bar(range(24), data[0], color='red', width=.4)
    ax1.bar(np.arange(.5,24), data[1], color='green', width=.4)
    ax1.xaxis.set_major_formatter(FormatStrFormatter('%02d:00'))
    ax1.set(xticks=range(0,24,4))
    ax1.set(yticks=np.arange(0,1.1,.2))
    plt.gca().set_yticklabels(['{:.0f}%'.format(x * 100) for x in plt.gca().get_yticks()])
    ax1.set_ylabel('Accidents & Injuries')
    ax1.legend(prop={'size': 10})
    ax1.set_title('Percentage of Injuries and Deaths in San Diego Car Collisions')
    fig.show()