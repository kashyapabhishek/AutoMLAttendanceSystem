import datetime


class Log:
    """
    Log class use to save the loges in files

    Attributes:
         file_object: File
            file object use to write the log in files

    Methods:
        __init__() constructor methode
    """

    def __init__(self, file_object):
        """
        :param file_object: File
            file object use to write the log in files
        """
        self.file_object = file_object

    def error(self, message, exception):
        """
        :param message: string
            custom message to be save in file
        :param exception: Exception
            exception be save in file
        """
        self.file_object.write(f"[Error] => {datetime.datetime.now()} | {message} | {exception} \n")

    def warning(self, message):
        """
        :param message: string
            custom message to be save in file
        """
        self.file_object.write(f"[warning] => {datetime.datetime.now()} | {message}  \n")

    def info(self, message):
        """
        :param message: string
            custom message to be save in file
        """
        self.file_object.write(f"[Info] => {datetime.datetime.now()} | {message}  \n")
