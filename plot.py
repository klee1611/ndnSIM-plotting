#!/usr/bin/python

"""
Copyright belongs to K.Lee.
"""

import Gnuplot
import os.path
import sys
import common

def file_is_empty(path):
    result = False
    if not os.path.exists(path):
        print path + ' file not found'
        result = True
    elif not os.path.isfile(path):
        print path + ' not a file'
        result = True
    elif os.path.getsize(path) == 0 :
        print path + ' is an empty file'
        result = True
    return result

def correct_input():
    result = True
    if len(sys.argv) != 5:
        sys.stdout.write('usage: python plot.py OPTIONS DATA_TYPE TRACING_RESULT_FILE OUT_FILE_NAME\n\n\
OPTIONS:\n\
    L3  Plot the result of L3RateTracer\n\
    L2  Plot the result of L2Tracer\n\
    cs  Plot the result of CsTracer\n\
    app Plot the result of AppDelayTracer\n\n')
        result = False

    elif file_is_empty(sys.argv[3]):
        result = False
    
    return result

if __name__ == '__main__':
    if not correct_input():
        sys.exit(1)
    common.plotting_file(sys.argv[3], sys.argv[4], sys.argv[2], sys.argv[1])
