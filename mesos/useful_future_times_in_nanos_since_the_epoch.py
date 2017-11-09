#!/usr/bin/env python3

import time
import datetime
import sys

a_billion = 1000 * 1000 * 1000  #  a billion!

def epoch_to_human(tt):
    return datetime.datetime.fromtimestamp(tt)




now = int(time.time())
now_plus_five_mins = now + ( 5 * 60 )
now_plus_one_hour = now + ( 60 * 60 )
now_plus_24_hours = now + (24 * 60 * 60 )

print('{!s:<25}{:16s}{:25s}{:25s}'.format('NOW:', 'SECONDS', 'NANOSECONDS', 'HUMAN TIME'))
print('{!s:<25}{:16s}{:25s}{:25s}'.format('---', '-------', '-----------', '----------'))
print('{!s:<20}{:15d}{:25d}{!s:>25}'.format('NOW:', now, now * a_billion, epoch_to_human(now)))
print('{!s:<20}{:15d}{:25d}{!s:>25}'.format('NOW+5min:', now_plus_five_mins, now_plus_five_mins * a_billion, epoch_to_human(now_plus_five_mins)))
print('{!s:<20}{:15d}{:25d}{!s:>25}'.format('NOW+1hr:', now_plus_one_hour, now_plus_one_hour * a_billion, epoch_to_human(now_plus_one_hour)))
print('{!s:<20}{:15d}{:25d}{!s:>25}'.format('NOW+1day:', now_plus_24_hours, now_plus_24_hours * a_billion, epoch_to_human(now_plus_24_hours)))

#def print_one_ut(useful_t):
#    print('{!s:<20}{:15d}{:25d}{!s:<20}'.format('NOW+5min:', now_plus_five_mins, now_plus_five_mins * a_billion, epoch_to_human(now_plus_five_mins))
    





sys.exit(0)

# Set maintenance window to start five minutes from now
#print(int(time.time()*1000000000)+60000000000)")





def nanos_since_epoch():
    epoch_time =  time.time()
    return epoch_time


def epoch_to_human(tt):
    return time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(time.time()))


if len(sys.argv) != 2:
    print('ERROR: Insufficient arguments', file=sys.stderr)
    print('Usage: {} <timestring>'.format(sys.argv[0]))
    print('For example, right now it is:',  nanos_since_epoch())
    sys.exit(0)


time_provided = sys.argv[1]

if len(time_provided) < 10:
    print('You provided a number with only {} digits, thats too few!'.format(len(time_provided)))
    sys.exit(1)
elif len(time_provided)  > 19:
    print('You provided a number with {} digits, thats too many!'.format(len(time_provided)))
    sys.exit(2)
elif len(time_provided) == 10:
    print('{}\tSECONDS(since the epoch):\t{}'.format( time_provided, epoch_to_human(int(time_provided) )))
elif len(time_provided) == 19:
    a_billion = 1000 * 1000 * 1000  #  a billion!
    print('{}\tNANOSECONDS(since the epoch):\t{}'.format( time_provided, epoch_to_human(int(time_provided) // a_billion)))
else:
    print("Wait.... I'm confused! = {} digits??? seconds since the epoch is typically 10, nanoseconds is 19.".format(len(time_provided)))





#fmt = "%Y-%m-%d %H:%M:%S"
#print('A', datetime.datetime.fromtimestamp(int(epoch_time)/a_billion).strftime('%c'))
#print('B', datetime.datetime.fromtimestamp(int(epoch_time)/a_billion).strftime('%c'))



