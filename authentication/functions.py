import datetime
import random


def generate_image_name():
    """Generate unique name for image based on current time"""
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d%H%M%S" + str(random.randint(0, 10)))
