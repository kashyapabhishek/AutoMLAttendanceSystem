import opendatasets as db
import os
import shutil


class FaceDatasetImports:
    """
    Import face data sets from different sources

    Attributes:
        file_object: File
            file object for logs
        data_dir: string
            path to save the data
        kaggle: boolean
            pipeline helper

    Methods:
    import_from_kaggle: (url:string) => None
        download the file from kaggle and save it in current directory,
        Need to give username and pass key from kaggle in commandline during download
    """

    def __init__(self, file_object, data_dir, kaggle=False):
        self.file_object = file_object
        self.data_dir = data_dir
        self.kaggle = kaggle

    def import_from_kaggle(self, url):
        """
        Import data from kaggle and save it to Data folder
        :param url: string
            url of the kaggle datasets
        :return: None
        """
        try:
            db.download(url)
            self.file_object.info(f"file download done form {url}")
        except Exception as ex:
            self.file_object.error(f'In FaceDatasetImports class => import_from_kaggle', ex)

    def move_data_to_url(self):
        """
        move the data from current directory to given dir location
        :return: None
        """
        try:
            file_name = input("Enter file name: ")
            current_dir_path = os.path.join(os.getcwd(), 'logging_module', file_name)
            shutil.copytree(current_dir_path, self.data_dir)
            self.file_object.info(f"file moved from {current_dir_path} to {self.data_dir}")
        except Exception as ex:
            self.file_object.error(f'In FaceDatasetImports class => move_data_to_url', ex)

    def download(self):
        """
        pipeline to download the datasets
        :return: None
        """
        try:
            if self.kaggle:
                url = input("Enter kaggle url:")
                if url:
                    self.import_from_kaggle(url)
                    self.move_data_to_url()
                else:
                    raise Exception("input not be empty")
        except Exception as ex:
            self.file_object.error(f'In FaceDatasetImports class => download', ex)


