import arrow


class time_chunk:

    def __init__(self, start, end):
        '''
        start : isoformat
        end : isoformat
        '''
        self.start = arrow.get(start).timestamp
        self.end = arrow.get(end).timestamp
        self.duration = self.end - self.start
        assert self.duration > 0

    def is_in(self, another_time_chunk):
        return (self.start - another_time_chunk.end) * (self.end - another_time_chunk.start) < 0



'''
busy_lists = [[{'start': '2017-11-07T23:30:00Z', 'end': '2017-11-08T23:00:00Z'}, {'start': '2017-11-08T23:30:00Z',
                                                                                  'end': '2017-11-09T00:30:00Z'}, {'start': '2017-11-10T23:30:00Z', 'end': '2017-11-11T00:30:00Z'}], []]
date_range = time_chunk("2017-11-15T13:11:00-08:00",
                        "2017-11-20T13:11:00-08:00")

for calendar in busy_lists:
    for one_time_chunt in calendar:
        temp_chunk = time_chunk(one_time_chunt['start'], one_time_chunt['end'])
        print(temp_chunk.is_in(date_range))
'''

