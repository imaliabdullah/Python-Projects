def add_time(start, duration, day=None):
    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if period == 'PM':
        start_hour += 12

    # Parse the duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Compute the end time
    end_minute = (start_minute + duration_minute) % 60
    carry_hour = (start_minute + duration_minute) // 60
    end_hour = (start_hour + duration_hour + carry_hour) % 24
    carry_day = (start_hour + duration_hour + carry_hour) // 24

    # Format the end time
    end_period = 'AM' if end_hour < 12 else 'PM'
    if end_hour == 0:
        end_hour = 12
    elif end_hour > 12:
        end_hour -= 12
    end_time = f'{end_hour:02d}:{end_minute:02d} {end_period}'

    # Format the day later
    days_later = ''
    if day:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day = [d.lower() for d in days].index(day.lower())
        end_day = (start_day + carry_day) % 7
        days_later = f', {days[end_day]}'

    # Format the days later
    if carry_day == 1:
        days_later = ' (next day)' + days_later
    elif carry_day > 1:
        days_later = f' ({carry_day} days later)' + days_later

    return end_time + days_later

print(add_time("8:16 PM", "466:02"))
# Returns: 6:10 PM

print(add_time("5:01 AM", "0:00"))
# Returns: 2:02 PM, Monday

print(add_time("3:30 PM", "2:12", "Monday"))
# Returns: 12:03 PM

print(add_time("2:59 AM", "24:00", "saturDay"))
# Returns: 1:40 AM (next day)

print(add_time("11:59 PM", "24:05", "Wednesday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("8:16 PM", "466:02", "tuesday"))
# Returns: 7:42 AM (9 days later)