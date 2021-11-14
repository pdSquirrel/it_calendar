from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# To do this in swedish, handle with locale
# >>> import locale
# >>> locale.setlocale(locale.LC_ALL, 'de_DE')
# 'de_DE'
# >>> import calendar
# >>> calendar.month_name[10]
# 'Oktober'
# >>> calendar.day_name[1]
# 'Dienstag'

def home(request, year, month):
    name = "Roger"
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    print(month_number)
    return render(request, 'home.html', {
        "name": name,
        "year": year,
        "month_number": month_number,
    })
