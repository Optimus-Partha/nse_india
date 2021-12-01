from option_chain import *
import schedule
import time,datetime

schedule.every(60).seconds.do(update_excel)
# schedule.every(10).minutes.do(job)


if __name__ == '__main__':
    while datetime.datetime.now().time() < datetime.time(15, 10, 00, 00):
        try: schedule.run_pending()
        except: pass
        time.sleep(1)


