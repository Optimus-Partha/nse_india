from option_chain import *
import schedule
import time, datetime
from plotly_graph import *
from multiprocessing import Process

schedule.every(60).seconds.do(update_excel)


# schedule.every(10).minutes.do(job)
def data():
    while datetime.datetime.now().time() < datetime.time(15, 10, 00, 00):
        try:
            schedule.run_pending()
        except:
            pass
        time.sleep(1)


def dashboard():
    app.run_server(port=8065, debug=False)


if __name__ == '__main__':
    p1 = Process(target=data)
    p1.start()
    p2 = Process(target=dashboard)
    p2.start()
    p1.join()
    p2.join()
