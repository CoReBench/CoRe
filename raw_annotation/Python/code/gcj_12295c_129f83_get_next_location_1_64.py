def get_next_location (num_of_people) :
    coordinates_list = []
    people_count = 1
    while people_count <= num_of_people :
        curr_location = raw_input("")
        curr_location = curr_location.split()
        x = int(curr_location[0])
        y = int(curr_location[1])
        dir = curr_location[2]
        if (dir == "N") :
            y += 1
        if (dir == "S") :
            y -= 1
        if (dir == "E") :
            x += 1
        if (dir == "W") :
            x -= 1
        coordinates = []
        coordinates.append(x)
        coordinates.append(y)
        coordinates_list.append(coordinates)
        people_count += 1
    next_dest = []
    next_dest_count = []
    for coordinates in coordinates_list :
        found = 0
        dest_idx = 0
        for dest in next_dest :
            if (coordinates == dest) :
                next_dest_count[dest_idx] += 1
                found = 1
                break
            dest_idx += 1
        if (found == 0) :
            next_dest.append(coordinates)
            next_dest_count.append(1)
    popular_next_dest = []
    popular_next_dest.append(next_dest[0])
    highest_count = next_dest_count[0]
    dest_count_idx = 0
    for dest_count in next_dest_count :
        if (dest_count_idx == 0) :
            dest_count_idx += 1
            continue
        if (dest_count == highest_count) :
            popular_next_dest.append(next_dest[dest_count_idx])
        if (dest_count > highest_count) :
            popular_next_dest = []
            highest_count = dest_count
            popular_next_dest.append(next_dest[dest_count_idx])
        dest_count_idx += 1
    if (len(popular_next_dest) == 1) :
        return popular_next_dest[0]
    else :
        smallest_number = popular_next_dest[0]
        dest_idx = 0
        for dest in popular_next_dest :
            if (dest_idx == 0) :
                dest_idx += 1
                continue
            if (dest < smallest_number) :
                smallest_number = dest
            dest_idx += 1
        return smallest_number
def generate_test_cases(T) :
    count = 1
    while count <= T :
        N = raw_input("")
        N = N.split()
        num_of_people = int(N[0])
        max_grid_size = int(N[1])
        coordinates = get_next_location(num_of_people)
        x = int(coordinates[0])
        y = int(coordinates[1])
        print "Case #" + str(count) + ": " + str(x) + " " + str(y)
        count += 1
T = eval(raw_input(""))
generate_test_cases(int(T))