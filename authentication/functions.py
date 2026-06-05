import datetime
import random


# function for create unique name based on date
def generate_image_name():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d%H%M%S" + str(random.randint(0,10)))