import arrow
from enum import Enum


class event_compare_result(Enum):
    within = 0
    without = 1



class calendar_event:

    duration = None
    start = None
    start_time = None
    end = None
    end_time = None
    flag = False

    def __init__(self, start, end):
        self.start = arrow.get(start).to('local')
        self.start_time = arrow.get(self.start.format("HH:mm"), "HH:mm")

        self.end = arrow.get(end).to('local')
        self.end_time = arrow.get(self.end.format("HH:mm"), "HH:mm")

        self.duration = (self.end - self.start).total_seconds()
        self.time_duration = (self.end_time - self.start_time).total_seconds()
        
        if self.duration >= 86400:
            self.flag = True
        if self.time_duration < 0: # prepare for time range setting like 23:00 ~ 1:00
            self.time_duration = -self.time_duration
            self.end_time = self.end_time.shift(days=1)

    def __str__(self):
        result = "(Start: %s    " % self.start
        result += "End: %s    " % self.end
        result += "Duration: %ss    );" %self.duration
        return result

    def compare_to(self, eventB):
        if eventB.flag: # eventB has more than 1 day, it must be on our range
            return event_compare_result.within
        
        if eventB.start_time >= self.end_time or self.start_time >= eventB.end_time:
            return event_compare_result.without
        
        return event_compare_result.within


'''
a = calendar_event('2017-11-15T09:20:24.889989-08:00', '2017-11-20T13:20:24.889989-08:00')
b = calendar_event('2017-11-15T12:20:24.889989-08:00', '2017-11-16T12:21:24.889989-08:00')
print(a.compare_to(b))
b = calendar_event('2017-11-16T13:20:24.889989-08:00', '2017-11-16T16:20:24.889989-08:00')
print(a.compare_to(b))
'''
