import datetime
import time
import os

def get_current_time():
    now = datetime.datetime.now()
    return now.hour, now.minute, now.second

def format_time(hour, minute, second):
    print(f"{hour:02}:{minute:02}:{second:02}")

def display_clock():
    while True:
        os.system('cls')
        hour, minute, second = get_current_time()
        format_time(hour, minute, second)
        time.sleep(1)

def main():
    print("======== DIGITAL CLOCK ========")
    display_clock()

if __name__ == "__main__":
    main()

