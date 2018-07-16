import csv
def load_file (file_name):
    with open (file_name) as a:
        for line in a :
            # line=line.replace (''',' ')
            for word in (line.split(',')):
                print (word, end='')
    a.close

if __name__=="__main__":
    load_file('collisions')