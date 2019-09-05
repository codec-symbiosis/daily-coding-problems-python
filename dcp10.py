'''
This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly
overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''
def find_min_rooms(time_list):
    start = sorted([num[0] for num in time_list])
    end = sorted([num[1] for num in time_list])

    room_occupied = max_room_num = 0
    i = j = 0
    n = len(time_list)

    while i < n and j < n:
        if start[i] < end[j]:
            room_occupied += 1
            max_room_num = max(room_occupied, max_room_num)
            i += 1
        else:
            room_occupied -= 1
            j += 1

    return max_room_num


def main():
    time_list = [(30, 75), (0, 50), (60, 150)]
    print(find_min_rooms(time_list))

if __name__ == '__main__':
    main()