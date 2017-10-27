import os
import pickle

def make_dir(path):
    """ Create a directory if there isn't one already """
    try:
        os.mkdir(path)
    except OSError:
        pass

def read_or_create(read_path, producer):
    """ Load or create an object """

    if os.path.isfile(read_path):
        print('Reading', read_path)
        with open(read_path, 'rb') as fp:
            return pickle.load(fp)
        
    result = producer()
    print('Saving', read_path)
    with open(read_path, 'wb') as fp:
        pickle.dump(result, fp)
        
    return result

