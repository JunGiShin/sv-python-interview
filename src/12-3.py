class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class ConferenceBooking:
    def __init__(self):
        self.schedules = []
    
    def booking(self, event):
        if event.start > event.end:
            return False
        low, high = 0, len(self.schedules) - 1
        while low <= high:
            mid = (low + high) // 2
            if event.start >= self.schedules[mid].end:
                low = mid + 1
            elif event.end <= self.schedules[mid].start:
                low = mid - 1
            else:
                return False
        self.schedules.insert(low, event)
        return True


if __name__ == "__main__":
    solution = ConferenceBooking()
    
    event1 = Event(10, 20)
    res = solution.booking(event1)
    assert res == True
    
    event2 = Event(20, 30)
    res = solution.booking(event2)
    assert res == True
    
    event3 = Event(5, 15)
    res = solution.booking(event3)
    assert res == False