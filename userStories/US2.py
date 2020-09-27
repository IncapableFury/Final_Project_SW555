# from models import Family
# from models import Gedcom
# from models import Individual
import datetime

#d1 as birthday
#d2 as death date or marriage date
def dateCompare(date1, date2):
    
    if(not isinstance(date1, datetime.date) or not isinstance(date2, datetime.date) ):
        raise ValueError("Input date not in datetime format!")
    if(date1 < date2):
        return True
    else:
        return False
