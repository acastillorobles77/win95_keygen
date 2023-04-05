#!/usr/bin/env python

import argparse
import random

parser = argparse.ArgumentParser(description='Windows 95 CD key generator')
parser.add_argument('amount_of_keys_to_generate', type=int, help='The desired number of keys to generate')
args = parser.parse_args()

for i in range(args.amount_of_keys_to_generate):
    group1 = str(random.randint(100, 999))
    while True:
        numbers = [random.randint(0, 9) for _ in range(7)]
        result = sum(numbers)
        if result % 21 == 0:
            group2 = "".join(str(num) for num in numbers)
            break
    key = group1 + "-" + group2
    print(key)

