import os
import shutil

path = os.path.join(os.getcwd(), 'Data/face/yolo3', 'images')
train_len = int(len(os.listdir(path)) * .8)
train_file = open("train.txt", "w+")
test_file = open("test.txt", "w+")
for i in os.listdir(path):
    if train_len > 0:
        train_file.write(f'{os.path.join(path, i)}\n')
        train_len -= 1
    else:
        test_file.write(f'{os.path.join(path, i)}\n')
train_file.close()
test_file.close()

copy_file_dir = os.path.join(os.getcwd(), 'training/darknet/training')
shutil.move(os.path.join(os.getcwd(), 'train.txt'), copy_file_dir)
shutil.move(os.path.join(os.getcwd(), 'test.txt'), copy_file_dir)