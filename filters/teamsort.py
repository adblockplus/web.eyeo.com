import random
from datetime import datetime


def teamsort(value, basedate="1970-01-01", column=0):
    base = datetime.strptime(basedate, "%Y-%m-%d")

    def randdiff(entry):
        date = datetime.strptime(entry[column], "%Y-%m-%d")
        diff = (date - base).days
        return diff * 0.2 + random.randrange(diff) * 0.8

    return sorted(value, key=randdiff)
