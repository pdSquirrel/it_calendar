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
    month = month.capitalize() # Make sure first letter is capitalized in the string
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    #create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    
    return render(request, 'home.html', {
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal
    })
