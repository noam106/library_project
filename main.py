import pickle
import os

import frontend.input_function
import library_backend
from frontend import *
if __name__ == '__main__':

    library = None
    if os.path.exists('library.pickle'):
        with open('library.pickle', 'rb') as f:
            library = pickle.load(f)
    else:
        print('Hello, this the first time you start library program.')
        library = frontend.input_function.start_library()


    try:
        # very long code with menus etc
        pass
    except:
        print("error occurred, saving and exiting")
    finally:
        with open('library.pickle', 'wb') as f:
            pickle.dump(library, f)