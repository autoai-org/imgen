import sys
import yaml
from modules.parser.parser import ImgenTree
from modules.utility.logger import log_info, log_error
from modules.loader.loader import load_images

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: %s <str.yaml>' % sys.argv[0])
        sys.exit(1)
    itree = None
    with open(sys.argv[1], 'r') as f:
        itree = ImgenTree(f.read())
    log_info("Task:" + itree.title)
    idx, results = load_images(itree.source)
    if (idx == -1):
        log_error("The folder "+ itree.source +" does not exists!")
    else:
        log_info("Number of original images: " + str(idx))