# Q011
# Created by JKChang
# 23/02/2017, 14:53
# Tag: convert binary number
# Description: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
#              then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be
#              printed in a comma separated sequence.
#
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010


res = []
items = [x for x in input('pls input binary numbers: ').split(',')]
for p in items:
    dec_p = int(p, 2)
    if not dec_p % 5:
        res.append(p)
print(','.join(res))
