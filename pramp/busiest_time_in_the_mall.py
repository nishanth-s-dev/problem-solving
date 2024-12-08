def find_busiest_period(data):
    timestamps = {}
    for element in data:
        timestamp, no_of_people, in_or_out = element
        _no_of_people = no_of_people if in_or_out == 1 else -1 * no_of_people
        if timestamp not in timestamps:
            timestamps[timestamp] = [_no_of_people]
        else:
            timestamps[timestamp].append(_no_of_people)
    
    current_people_count = 0
    max_people_timestamp = None
    max_people_count = float("-inf")

    for timestamp, no_of_people in timestamps.items():
        for people_count in no_of_people:
            current_people_count += people_count

        if max_people_count < current_people_count:
            max_people_count = current_people_count
            max_people_timestamp = timestamp

    return max_people_timestamp

data = [ 
        [1487799425, 14, 1], 
        [1487799425, 4,  0],
        [1487799425, 2,  0],
        [1487800378, 10, 1],
        [1487801478, 18, 0],
        [1487801478, 18, 1],
        [1487901013, 1,  0],
        [1487901211, 7,  1],
        [1487901211, 7,  0] 
    ]

print(find_busiest_period(data))