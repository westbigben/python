"""Schedule example — run a quick job every second for a few iterations."""
import schedule, time

def job():
    print('Scheduled job: Hello from schedule!')

def main():
    print('Schedule demo — we will run the job 3 times rapidly.')
    schedule.every(1).seconds.do(job)
    count = 0
    start = time.time()
    while count < 3:
        schedule.run_pending()
        time.sleep(0.5)
        count += 1
    print('Done with schedule demo.')

if __name__ == '__main__':
    main()
