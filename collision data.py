import csv
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
    data=[np.array(accident),np.array(injury),np.array(death)]
    print (data)
    num_bins = np.arange(25)-.5
    colors = ['blue', 'red', 'green']
    fig, ax1 = plt.subplots()
    ax1.hist([data[0], data[1],np.empty(1)], num_bins,  range=(0,23), color=colors, label=['Accidents', 'Injuries', 'Deaths'])
    ax2=ax1.twinx()
    ax2.hist([np.empty(1), np.empty(1),data[2]], num_bins, range=(0,23), color=colors, label=['Accidents', 'Injuries', 'Deaths'])
    ax1.xaxis.set_major_formatter(FormatStrFormatter('%02d:00'))
    ax1.set(xticks=range(0,24,4))
    ax1.set_ylabel('Accidents & Injuries')
    ax2.set_ylabel('Deaths', color='green')
    ax1.set_xlabel('Hours of the Day')
    ax2.tick_params('y', colors='green')
    ax2.legend(prop={'size': 10})
    ax2.set_title('San Diego Car Collisions')
    fig.show()


