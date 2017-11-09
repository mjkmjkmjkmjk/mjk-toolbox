#!/usr/bin/env python3

import datetime
import time
import sys
from pprint import pprint

a_billion = 1000 * 1000 * 1000

def secs_since_ep():
    epoch_time = time.time()
    return int('%.0f' % epoch_time)


def epoch_to_human(tt):
    #return time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(time.time()))
    #return time.strftime("%Z - %Y/%m/%d, %H:%M:%S", tt)
    return datetime.datetime.fromtimestamp(tt)


if len(sys.argv) != 2:
    print('ERROR: Insufficient arguments', file=sys.stderr)
    print('Usage: {} <timestring>'.format(sys.argv[0]))
    secs = secs_since_ep()
    nans = secs_since_ep() * a_billion
    print('For example, right now it is:',  secs, ' seconds and ', nans, ' since the epoch.')
    sys.exit(0)


time_provided = sys.argv[1]

if len(time_provided) < 10:
    print('You provided a number with only {} digits, thats too few!'.format(len(time_provided)))
    sys.exit(1)
elif len(time_provided)  > 19:
    print('You provided a number with {} digits, thats too many!'.format(len(time_provided)))
    sys.exit(2)
elif len(time_provided) == 10:
    print('{}\tSECONDS(since the epoch) is:\t{}'.format( time_provided, epoch_to_human(int(time_provided) )))
elif len(time_provided) == 19:
    a_billion = 1000 * 1000 * 1000  #  a billion!
    print('{}\tNANOSECONDS(since the epoch) is:\t{}'.format( time_provided, epoch_to_human(int(time_provided) // a_billion)))
else:
    print("Wait.... I'm confused! = {} digits??? Seconds since the epoch is typically 10, nanoseconds is 19.".format(len(time_provided)))


