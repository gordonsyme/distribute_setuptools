import sys
import time
from datetime import datetime, timedelta

def slowly_slowly_outputee_monkey(character, duration=timedelta(minutes=1), sleep_time=timedelta(seconds=1)):
    end = datetime.utcnow() + duration
    while datetime.utcnow() < end:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(sleep_time.total_seconds())

if __name__ == '__main__':
    slowly_slowly_outputee_monkey(".", duration=timedelta(minutes=30), sleep_time=timedelta(milliseconds=100))
