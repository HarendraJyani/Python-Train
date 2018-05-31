from collections import Counter
import math
import os
import random
import re
import sys

    
string = sorted(Counter(input()).items(), key= lambda x: (-x[1],x[0]))[:3]
print("\n".join(x[0]+" "+str(x[1]) for x in string))
