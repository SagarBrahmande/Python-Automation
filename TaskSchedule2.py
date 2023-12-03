import datetime
import schedule
import time

def Schedule_Minute():
    print("Schedular schedules after a minute...")
    print("Current time is : ",datetime.datetime.now())

def Schedule_Hour():
    print("Schedular schedules after a hour...")
    print("Current time is : ",datetime.datetime.now())

def main():
    print("Automations using Python")
    
    schedule.every(1).minutes.do(Schedule_Minute)
    

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()