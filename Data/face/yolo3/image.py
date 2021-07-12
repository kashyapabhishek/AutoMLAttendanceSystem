import os
import shutil
os.chdir("images")

for i in zip(range(len(os.listdir())), os.listdir()):
    os.rename(i[1], str(i[0]+1)+'.jpg')