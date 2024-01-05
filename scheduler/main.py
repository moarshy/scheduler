from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time
import logging

# Set up basic logging
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.INFO)

def time_now():
    t = f"The current time. {datetime.now().strftime('%H:%M:%S')}"
    print(t)

def main():
    try:
        scheduler = BackgroundScheduler()

        # Schedule the job
        scheduler.add_job(time_now, 'interval', seconds=5)
        scheduler.start()

        # Keep the script running
        while True:
            time.sleep(2)

    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler shut down gracefully.")


if __name__ == '__main__':
    main()