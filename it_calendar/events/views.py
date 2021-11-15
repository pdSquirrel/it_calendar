from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# To do this in swedish, handle with locale
# >>> import locale
# >>> locale.setlocale(locale.LC_ALL, 'de_DE')
# 'de_DE'
# >>> import calendar
# >>> calendar.month_name[10]
# 'Oktober'
# >>> calendar.day_name[1]
# 'Dienstag'

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    #create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    
    return render(request, 'events/home.html', {
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal
    })
