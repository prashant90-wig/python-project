##Alarm clock (console, sleep + print)
import time
import datetime


def get_current_time():
    now = datetime.datetime.now()
    return now.hour, now.minute

def alarm_clock():
    alarm_hour = int(input("Enter alarm hour (0-23): "))
    alarm_minute = int(input("Enter alarm minute (0-59): "))
    return alarm_hour, alarm_minute


def check_alarm(current_time, alarm_time):
    if current_time == alarm_time:
        return True
    return False


def ring_alarm():
    for i in range(5):  
        print("🚨 BEEP BEEP BEEP! WAKE UP! 🚨")
        time.sleep(0.5)  


def main():
    alarm_time = alarm_clock()
    print(f"Alarm set for {alarm_time[0]:02}:{alarm_time[1]:02}")
    while True:
        current_time = get_current_time()
        if check_alarm(current_time, alarm_time):
            ring_alarm()
            break

if __name__ == "__main__":
    main()

