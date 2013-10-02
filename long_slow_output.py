import sys
import time
from datetime import datetime, timedelta

def output_madly_long_string(character_count):
    for i in xrange(character_count):
        print "*",

def slowly_slowly_outputee_monkey(character, duration=timedelta(minutes=1), sleep_time=timedelta(seconds=1)):
    end = datetime.utcnow() + duration
    while datetime.utcnow() < end:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(sleep_time.total_seconds())

if __name__ == '__main__':
    output_madly_long_string(25000)
    slowly_slowly_outputee_monkey(".", duration=timedelta(minutes=30), sleep_time=timedelta(milliseconds=100))
