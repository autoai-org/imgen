import sys
import yaml
from modules.parser.parser import ImgenTree
from modules.utility.logger import log_info, log_error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: %s <str.yaml>' % sys.argv[0])
        sys.exit(1)
    itree = None
    with open(sys.argv[1], 'r') as f:
        itree = ImgenTree(f.read())
    log_info("Task:" + itree.title)
    itree.process()