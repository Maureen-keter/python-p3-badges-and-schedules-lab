def badge_maker(name):
     return f"Hello, my name is {name}."

def batch_badge_creator(names): 
    badges=[]     
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    rooms=[]   
    for index,name in enumerate(names):
        room_number=index+1
        rooms.append(f"Hello, {name}! You'll be assigned to room {index+ 1}!")
    return rooms

def printer(names):
    badges=batch_badge_creator(names)
    rooms=assign_rooms(names)
    for badge in badges:
        print(badge)

    for room in rooms:
        print(room)