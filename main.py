import time
from datetime import datetime, timedelta, date
import psutil
import ctypes



def killProcess(processName):
    try:
        for process in (process for process in psutil.process_iter() if process.name()==processName):
            process.kill()
    except:
        pass

def getTime(mins):
    timeNow = datetime.now().time()  # time object
    timeLater = datetime.combine(date.today(), timeNow) + timedelta(minutes = mins)
    return timeLater

def getStudyPeriodInMinutes():
    while True:
        try:
            minutes = int(input("How long do you want your study periods to be? (In minutes): \n"))
            return minutes
        except:
            print("Invalid number. Only use integers.")

def getBreakPeriodInMinutes():
    while True:
        try:
            minutes = int(input("How long do you want your break periods to be? (In minutes): \n"))
            return minutes
        except:
            print("Invalid number. Only use integers.")
def getProcessName():
    while True:
            processName = input("What process do you want to kill on your breaks?: \n")
            if processName[(len(processName) - 4):] == ".exe":
                return processName
            print("Invalid process. Example would be process.exe")

def incrementTimeByOneSecond(datetime):
    return datetime + timedelta(seconds = 1)


def main():
    breakInMinutes = getBreakPeriodInMinutes()
    studyPeriodInMinutes = getStudyPeriodInMinutes()
    processToKill = getProcessName()
    while True:
        now = datetime.now()
        later = getTime(studyPeriodInMinutes)
        boolean = True
        while boolean:
            if now < later:
                now = incrementTimeByOneSecond(now)
                killProcess(processToKill)
                time.sleep(1)
            else:
                boolean = False
        ctypes.windll.user32.MessageBoxW(0, f"It's break time! {processToKill} has been unblocked for {breakInMinutes} minutes", "Break!", 0x40000)
        time.sleep(breakInMinutes*60)
        ctypes.windll.user32.MessageBoxW(0, f"Back to studying. {processToKill} has been blocked for {studyPeriodInMinutes} minutes ", "Study!", 0x40000)

if __name__ == "__main__":
    main()