from .models import *


def chooseClass(location):
    switcher = {
        "Talamban": Tmbcamcount,
        "Labangon": Labcamcount,
        "Kalimpyo": Kalcamcount,
        "Goldswan": Goldswancamcount,
    }

    return switcher.get(location, "")
