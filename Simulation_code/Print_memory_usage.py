__author__ = "Mark Xiang"
__created__ = "09/01/2023"
__updated__ = "08/14/2024"

##----------- Import packages --------------##
import psutil
import sys
import time

##----------- Define functions --------------------##
def print_memory_usage(ExtraMessage = ""):
    process = psutil.Process()
    mem = process.memory_info()[0]
    sys.stderr.write(time.strftime("[%a, %b %d %Y %H:%M:%S] [Memory usage: {:.03f} Mb]\t{}\n".format(mem/(1024**2), ExtraMessage)))

if __name__ == "__main__":
    print_memory_usage()