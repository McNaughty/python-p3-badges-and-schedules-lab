def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = f'Hello, my name is {name}.'
        badges.append(badge)
    return badges

def assign_rooms(names):
    room = 1
    assigned_rooms = []
    for name in names:
        allocation = f'Hello, {name}! You\'ll be assigned to room {room}!'
        assigned_rooms.append(allocation)
        room += 1
    return assigned_rooms
# print(assign_rooms)       
    

def printer(names):
    # Generate badges using batch_badge_creator
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)

    # Assign rooms using assign_rooms
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)


