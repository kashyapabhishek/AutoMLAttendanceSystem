from logging_module.log import Log
from data_import.face_dataset_imports import FaceDatasetImports
import os


def home():
    file_object = open("logs.txt", "w+")
    log_file_object = Log(file_object)
    data_dir_path = os.path.join(os.getcwd(), 'data')
    face_data_imports = FaceDatasetImports(log_file_object, data_dir_path,kaggle=True)
    face_data_imports.download()


if __name__ == '__main__':
    home()
    print('test')