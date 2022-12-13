# https://www.codewars.com/kata/52742f58faf5485cae000b9a
# Rules there^

def format_duration(seconds):
    if seconds == 0:
        return "now"

    def format_duration1(seconds):
        years = seconds / 31536000

        if years >= 1:
            seconds -= 31536000 * int(years)
            years = int(years)

        days = seconds / 86400

        if days >= 1:
            seconds -= 86400 * int(days)
            days = int(days)

        hours = seconds / 3600

        if hours >= 1:
            seconds -= 3600 * int(hours)
            hours = int(hours)

        minutes = seconds / 60

        if minutes >= 1:
            seconds -= 60 * int(minutes)
            minutes = int(minutes)

        seconds = int(seconds)

        return years, days, hours, minutes, seconds

    time = format_duration1(seconds)

    years = time[0]
    days = time[1]
    hours = time[2]
    minutes = time[3]
    seconds = time[4]

    if isinstance(years, int):
        if years > 1:
            years = (str(years) + " years, ")
        elif years == 1:
            years = (str(years) + " year, ")
    else:
        years = ""
    if isinstance(days, int):
        if days > 1:
            days = (str(days) + " days, ")
        elif days == 1:
            days = (str(days) + " day, ")
    else:
        days = ""
    if isinstance(hours, int):
        if hours > 1:
            hours = (str(hours) + " hours, ")
        elif hours == 1:
            hours = (str(hours) + " hour, ")
    else:
        hours = ""
    if isinstance(minutes, int):
        if minutes > 1:
            minutes = (str(minutes) + " minutes, ")
        elif minutes == 1:
            minutes = (str(minutes) + " minute, ")
    else:
        minutes = ""
    if isinstance(seconds, int):
        if seconds > 1:
            seconds = (str(seconds) + " seconds")
        elif seconds == 1:
            seconds = (str(seconds) + " second")
        elif seconds == 0:
            seconds = ""
    else:
        seconds = ""

    full_time = (str(years) + str(days) + str(hours) + str(minutes) + str(seconds))

    # Right there we adjust to rules from our exercise, deleting "," and adding "and" if necessary

    if full_time[-2] == ",":
        full_time = full_time[:-2]
    finder = full_time.rfind(", ")

    if finder != -1:

        optional_time = (full_time[:finder] + " and" + full_time[finder + 1:])
        optional_time = optional_time.replace(" and 0", "")
        return optional_time

    else:
        return full_time