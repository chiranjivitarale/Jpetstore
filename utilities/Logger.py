import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\USER\\PycharmProjects\\Jpetstore_project\\Logs\\JPetStore.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
#
#
#
#
#
#
#
#
#
#
#
#
