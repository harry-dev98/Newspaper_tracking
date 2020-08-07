from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()

    scheduler.start()
