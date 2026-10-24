import heapq

def can_attend_all(events):
    events=sorted(events)
    for i in range(1,len(events)):
        if events[i-1][1]>events[i][0]:
            return False
    return True
def min_rooms_required(events):
    if not events:
        return 0
    events=sorted(events)
    end_times=[]
    max_rooms=0
    for start,end in events:
        while end_times and end_times[0]<=start:
            heapq.heappop(end_times)
        heapq.heappush(end_times,end)
        max_rooms=max(max_rooms,len(end_times))
    return max_rooms
if __name__=='__main__':
    events=[(9,10),(9,11),(10,12)]
    print(can_attend_all(events))   
    print(min_rooms_required(events))  
    print(can_attend_all([(9,10),(10,11)])) 
    print(min_rooms_required([(9,10),(10,11)]))  
    print(can_attend_all([]))         
    print(min_rooms_required([]))     
    print(min_rooms_required([(9,12),(9,11),(9,10)]))  