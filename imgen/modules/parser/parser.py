import os
import yaml
import importlib
from PIL import Image

from modules.loader.loader import load_filelist
from modules.utility.logger import log_info, log_error

class ImgenTree():
    def __init__(self, configStr):
        self.config = self._parse(configStr)
        idx, results = load_filelist(self.config['source'])
        if (idx == -1):
            log_error("The folder "+ self.config['source'] +" does not exists!")
        else:
            log_info("Number of original images: " + str(idx))
        self.ongoing_filelist = results

    def _parse(self, configStr):
        config = yaml.safe_load(configStr)
        self.title = config["title"]
        self.source = config["source"]
        self.dest = config["dest"]
        self.operations_list = config["operations"]
        return config
    
    def _get_operation_list(self):
        self.operations = []
        """
        operation is params looks like
        {
            'rotate': {
                'probability': 0.5
                'rotate_angle': -1
            }
        }
        """
        for each in self.operations_list:
            for key in each:
                full_module_name = "modules.augment." + key
                operationModule = importlib.import_module(full_module_name)
                ip_module_cls = getattr(operationModule, key.capitalize())
                cls_obj = ip_module_cls(**each[key])
                self.operations.append(cls_obj)

    def process(self):
        # Read images that will be processed
        self.ongoing_images = []
        for each in self.ongoing_filelist:
            self.ongoing_images.append(Image.open(each))
        self._get_operation_list()
        for each in self.operations:
            self.ongoing_images = each.perform_operation(self.ongoing_images)
        # save result
        for index, each in enumerate(self.ongoing_images):
            each.save(os.path.join(self.dest, "imgen-"+str(index)+".JPG"))
        log_info("Finished!")