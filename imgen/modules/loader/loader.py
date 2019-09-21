import os

def load_images(imagesPath):
    # load_images walks the path, and returns the number of files under the path
    # it will go recursively
    # return: -1, [] if folder does not exist
    #          0, [] if folder exists, but no files found
    #          n, [image_1, image_2, ... image_n] if folder exists, and n(umber) files found
    results = []
    idx = -1
    for root, dirs, files in os.walk(imagesPath):
        for name in files:
            results.append(os.path.join(imagesPath, name))
        for name in dirs:
            path = os.path.join(imagesPath, name)
            if (os.path.isfile(path)):
                results.append(path)
    if not len(results) == 0:
        idx = len(results)
    return idx, results