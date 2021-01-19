import glob
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
os.chdir(THIS_FOLDER)
myFiles = glob.glob('*.txt')
myFiles.sort()

key=[]
for i in myFiles:
    m=open(os.path.join(THIS_FOLDER,i), 'r').read().split(",")
    a=[i.strip(" ") for i in m]
    
    key.append("|".join(a))
    

Count=len(key)