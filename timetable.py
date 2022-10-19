import time

class Period:
    def __init__(self,name,venue,duration:int):
        """
        Name : Name of the Subject
        Venue : Venue of the Class
        Duration : In hours

        """
        self.name = name
        self.venue = venue
        self.duration = duration

    
class Day:
    def __init__(self,day_name:str,*periods:Period):
        """
            day_name : Weekday.
            periods : All the periods to be held in the day.
        """
        self.day = day_name
        self.periods = periods
    
    def print_day(self):
        for period in self.periods:
            print(period.name,period.venue)

    def start_day(self):
        print(self.day)
        for period in self.periods:
            print(period.name,period.venue)
            time.sleep(period.duration*3)

dc = Period("D.C","430",1)
esd = Period("ESD","420",1)
co = Period("CO","303",1)
tmc = Period("TMC","336",1)
daa = Period("DAA","336",1)

dc_lab = Period("DC Lab","420",2)
esd_lab = Period("ESD Lab","320",2)
daa_lab = Period("DAA Lab","353",2)



office_hours = Period("Office Hours","Library/Labs",1)

monday = Day("Monday",tmc,esd,daa,esd_lab,office_hours,daa)
tuesday = Day("Tuesday",dc_lab,tmc,co,dc,office_hours,dc)
wednesday = Day("Wednesday",daa,dc,office_hours,daa_lab,office_hours,office_hours)
thursday = Day("Thursday",co,esd,office_hours,office_hours,dc,esd,office_hours)
friday = Day("Friday",daa,esd,office_hours,office_hours,co,tmc,office_hours)



class Week:
  def __init__(self,*days):
    self.week = days


WEEK = Week(monday,tuesday,wednesday,thursday,friday)