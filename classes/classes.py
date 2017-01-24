# Cooper Anderson
# Time and Date Classes


class Time(object):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours if 0 <= hours <= 12 else 0
        self.minutes = minutes if 0 <= hours <= 60 else 0
        self.seconds = seconds if 0 <= hours <= 60 else 0

    def print_time(self):
        print repr(self)

    def convert_to_seconds(self):
        print str((self.hours * 3600) + (self.minutes * 60) + self.seconds)

    def __repr__(self):
        return str(self.hours) + ':' + Time.format_number(self.minutes) + ':' + Time.format_number(self.seconds)

    @staticmethod
    def format_number(number):
        return str(number) if number > 9 else '0' + str(number)


class Date(object):
    def __init__(self, month=0, day=0, year=0):
        self.month = month if 1 <= month <= 12 else 1
        self.day = day if 1 <= day <= 31 else 1
        self.year = year

    def print_date(self):
        print repr(self)

    def __repr__(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "November", "December"]
        return months[self.month - 1] + ' ' + str(self.day) + ", " + str(self.year)
