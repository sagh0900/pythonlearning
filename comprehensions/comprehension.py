import os
import glob  # used to find all files specified in below extension
from pprint import pprint as pp

file_sizes = {os.path.realpath(p): os.stat(p).st_size
              for p in glob.glob('*.py')}
pp(file_sizes)