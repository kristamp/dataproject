import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
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
    num_bins = 24
    fig, axes = plt.subplots()
    colors = ['blue', 'red', 'green']
    w0=np.ones_like(data[0])
    w1 = np.ones_like(data[1])
    w2 = np.ones_like(data[2])
    w2[0:]=10
    # n, bins, patches = axes.hist(data)
    n, bins, patches = axes.hist(data, num_bins, alpha=0.5, color=colors, label=['Accidents', 'Injuries', 'Death(x10)'], weights=[w0, w1, w2] )

    axes.legend(prop={'size': 10})
    axes.set_title('San Diego Car Collisions')
    # ax3.hist(x_multi, n_bins, histtype='bar')
    # ax3.set_title('different sample sizes')
    plt.show()


