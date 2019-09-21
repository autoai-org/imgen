import datetime

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def log_info(string):
    print(str(datetime.datetime.now()) + " " + OKGREEN + '[IMGEN]: ' + ENDC + string)

def log_error(string):
    print(str(datetime.datetime.now()) + " " +  FAIL + '[IMGEN]: ' + ENDC + string)
