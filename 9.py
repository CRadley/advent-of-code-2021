def is_valid_lowest(index, value, values, offset):
    outputs = []
    if index % offset:
        outputs.append(value < values[index - 1])
    if index % offset < offset - 1 and index < len(values):
        outputs.append(value < values[index + 1])
    if index >= offset:
        outputs.append(value < values[index - offset])
    if index < len(values) - 1 - offset and index + offset < len(values):
        outputs.append(value < values[index + offset])
    return all(outputs)


def determine_basin_size(index, values, offset, searched_index):
    if index not in searched_index:
        searched_index.append(index)
    else:
        return 0
    size = 1
    if index % offset and values[index - 1] < 9:
        size += determine_basin_size(index - 1, values, offset, searched_index)
    if index % offset < offset - 1 and index < len(values) and values[index + 1] < 9:
        size += determine_basin_size(index + 1, values, offset, searched_index)
    if index >= offset and values[index - offset] < 9:
        size += determine_basin_size(index - offset, values, offset, searched_index)
    if index < len(values) - 1 - offset and index + offset < len(values) and values[index + offset] < 9:
        size += determine_basin_size(index + offset, values, offset, searched_index)
    return size

with open('inputs/9.txt', 'r') as f:
    lines = f.readlines()
    width = len(lines[0]) - 1
    rows = [int(y) for line in lines for y in line.replace('\n', '')]

low_points = [z for i, z in enumerate(rows) if is_valid_lowest(i, z, rows, width)]
print(sum(low_points) + len(low_points))
basins = [determine_basin_size(i, rows, width, []) for i, z in enumerate(rows) if is_valid_lowest(i, z, rows, width)]
sorted_basins = sorted(basins, reverse=True)
print(sorted_basins[0] * sorted_basins[1] * sorted_basins[2])


#585
#827904