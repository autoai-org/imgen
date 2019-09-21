import random
from modules.augment.operation import Operation

class Rotate(Operation):
    def __init__(self, probability, rotation_angle):
        """
        rotation angle could be one of:
        90  :
        180 :
        270 :
        -1  : randomly
        """
        Operation.__init__(self, probability)
        self.rotation = rotation_angle
    
    def __str__(self):
        return "Rotate " + str(self.rotation)
    
    def perform_operation(self, images):
        random_factor = random.randint(1, 3)
        def do(image):
            if self.rotation == -1:
                return image.rotate(90 * random_factor, expand=True)
            else:
                return image.rotate(self.rotation, expand=True)
        
        augmented_images = []
        for image in images:
            augmented_images.append(do(image))
        
        return augmented_images