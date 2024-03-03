import os
import sys
import logging #inbuilt login module

logging_str = "[%(asctime)s: %(levelname)s: %(module)s:%(message)s]"
#%(asctime)s:it will save time stamp,%(levelname)s: level name,%(module)s:%(message)s gives the root module
log_dir = "logs" # the directory
log_filepath = os.path.join(log_dir,"running_logs.log") 
os.makedirs(log_dir,exist_ok=True) #it will create the directory

logging.basicConfig(    
    level=logging.INFO,
    format=logging_str,
    
    handlers= [
        logging.FileHandler(log_filepath),#it will be logged inside a file
        logging.StreamHandler(sys.stdout) #it will show inside the terminal)

    ])

logger = logging.getLogger("textSummarizerLogger")