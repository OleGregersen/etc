#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = sorted(input().strip())
    c = Counter(s).most_common()
    c = sorted(c, key=lambda x: (x[1] * -1, x[0]))
    for i in range(0, 3):
        print(c[i][0], c[i][1])
