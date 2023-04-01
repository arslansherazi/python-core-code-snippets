"""
    Important points::
    => schedule==0.6.0 is used for below code
"""
import schedule
import datetime


def job(scheduling_no):
    current_datetime = datetime.datetime.now()
    current_datetime = current_datetime.strftime('%b %d,%Y %H:%M:%S')
    job_result = 'Scheduling{no}:: {current_datetime} I am working'.format(
        no=scheduling_no, current_datetime=current_datetime
    )
    print(job_result)


if __name__ == '__main__':
    # schedule job
    schedule.every().minute.at(':20').do(job, scheduling_no=1)  # run job func every 20th second of minute
    schedule.every(5).minutes.do(job, scheduling_no=2)  # run job func after every 5 minutes
    schedule.every().monday.at('20:00').do(job, scheduling_no=3)  # run job func every monday at 08:00 pm
    schedule.every().day.at('20:20').do(job, scheduling_no=4)  # run job func every day at 08:20 pm

    # run scheduler
    while True:
        schedule.run_pending()
