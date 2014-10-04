#!/usr/bin/env python
# -*- coding: utf-8 -*-
from act import act

act = act()
# print act.segment('年来 中希贸易始终处于较低的水平 希腊几乎没有在中国投资')
output = open('./seg_word_p.txt', 'aw+')
for line in open('./msr/msr_test'):
    line = line.strip('\n')
    output.write(act.segment(line, False)+'\n')
output.close()