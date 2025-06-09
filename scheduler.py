# scheduler.py
import pandas as pd

def generate_weekly_schedule(subjects, hours):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    schedule = {day: [] for day in days}
    per_day = sum(hours) / 7
    i = 0
    for day in days:
        remaining = per_day
        while remaining > 0 and i < len(subjects):
            time = min(hours[i], remaining)
            schedule[day].append(f"{subjects[i]}: {round(time, 2)} hrs")
            remaining -= time
            hours[i] -= time
            if hours[i] <= 0:
                i += 1
    return pd.DataFrame(dict([(k, pd.Series(v)) for k,v in schedule.items()]))
