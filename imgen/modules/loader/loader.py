import os
import glob

def load_filelist(imagesPath, recursively=True):
    file_types = ['*.jpg', '*.bmp', '*.jpeg', '*.gif', '*.img', '*.png']
    file_types.extend([str.upper(x) for x in file_types])
    results = []
    idx = -1
    for file_type in file_types:
        results.extend(glob.glob(os.path.join(os.path.abspath(imagesPath+"/**/*"), file_type), recursive=True))

    if not len(results) == 0:
        idx = len(results)
    return idx, results