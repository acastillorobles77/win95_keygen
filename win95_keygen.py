#!/usr/bin/env python

import argparse
import random

parser = argparse.ArgumentParser(description='Windows 95 key generator')
parser.add_argument('amount_of_keys_to_generate', type=int, help='The desired number of keys to generate')
args = parser.parse_args()

for i in range(args.amount_of_keys_to_generate):
    group1 = str(random.randint(100, 366)) + str(random.randint(10, 95))
    while True:
        numbers = [random.randint(0, 9) for _ in range(6)]
        result = sum(numbers)
        if result % 7 == 0:
            st = "".join(str(num) for num in numbers)
            group2 = "0" + st
            break
    group3 = str(random.randint(10000, 99999))
    key = group1 + "-OEM-" + group2 + "-" + group3
    print(key)
