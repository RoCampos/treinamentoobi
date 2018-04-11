#capacity
capacity = int(input ())

#students
students = int(input())

#number of travelsv with full capacity
travel_full_count = students//(capacity-1)

last_travel = students % (capacity-1)

if (last_travel > 0):
    travel_full_count = travel_full_count + 1

print (travel_full_count)