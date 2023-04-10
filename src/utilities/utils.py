import logging
import inspect

class Utils:

    def custom_logger(logLevel=logging.DEBUG):
        
        logger_name = inspect.stack()[1][3]

        # Create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # Create console handler
        fh = logging.FileHandler('automation.log')
        
        # Create fotmatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        
        # Add formatter
        fh.setFormatter(formatter)    

        # Add console handler to logger
        logger.addHandler(fh)
        return logger

