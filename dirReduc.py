def dir_reduce(directions_list):
    directions_values = {"NORTH": -1, "SOUTH": 1, "WEST": -5, "EAST": 5}
    reduced_directions_list = [directions_list[0]] if len(directions_list) else None
    if reduced_directions_list is None:
        return []
    for direction in directions_list[1:]:
        if (not len(reduced_directions_list)
                or directions_values[reduced_directions_list[-1]] + directions_values[direction]):
            reduced_directions_list.append(direction)
        else:
            del reduced_directions_list[-1]
    return reduced_directions_list


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
u = ["NORTH", "WEST", "SOUTH", "EAST"]

for arr in a, u:
    print(dir_reduce(arr))
