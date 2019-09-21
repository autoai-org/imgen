class Operation():
    def __init__(self, probability):
        self.probability = probability

    def __str__(self):
        return self.__class__.__name__
    
    def perform_operation(self, images):
        raise RuntimeError("Illegal call to base class.")