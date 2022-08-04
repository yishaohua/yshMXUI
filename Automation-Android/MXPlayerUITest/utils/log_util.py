import logging
import datetime
import os


class LogUtil(object):

    def __init__(self, name="reco_auto_case"):
        self.file_tail = datetime.datetime.now().strftime("%Y-%m-%d")
        self.logger = logging.getLogger(name)
        if os.path.exists("./log/") is not True:
            os.makedirs("./log/")

        if not os.access("./log/", os.W_OK):
            return

        if not self.logger.handlers:
            fh = logging.FileHandler("./log/%s%s.log" % ("auto_case.", self.file_tail))
            formatter = logging.Formatter(
                "{time:%(asctime)s, message:%(message)s}")
            fh.setFormatter(formatter)
            self.logger.setLevel(logging.INFO)
            print('Add logger handler')
            self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger
