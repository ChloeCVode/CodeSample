#  Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
# You can find some examples in the test fixtures.

def make_readable(seconds):
    def convert_to_hours(seconds):
        full_hours = int(seconds / 3600)
        rest_of_seconds = seconds % 3600
        return full_hours,rest_of_seconds

    full_hours = convert_to_hours(seconds)[0]
    rest_of_seconds = convert_to_hours(seconds)[1]

    def convert_to_minutes(rest_of_seconds):
        full_minutes = int(rest_of_seconds / 60)
        rest_of_seconds = rest_of_seconds % 60
        return full_minutes,rest_of_seconds


    full_minutes = convert_to_minutes(rest_of_seconds)[0]
    rest_of_seconds = convert_to_minutes(rest_of_seconds)[1]

    # .zfill is python built in method

    list = str(full_hours).zfill(2) + ":" + str(full_minutes).zfill(2) + ":" + str(rest_of_seconds).zfill(2)
    return list



