import yaml

class ImgenTree():
    def __init__(self, configStr):
        self.title = ""
        self.source = ""
        self.config = self._parse(configStr)
        
    def _parse(self, configStr):
        config = yaml.safe_load(configStr)
        self.title = config["title"]
        self.source = config["source"]
        return config