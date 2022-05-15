
def get_display_outputs(filepath):
    with open(filepath, 'r') as f:
        return [(line.split('|')[0].strip(), line.split('|')[1].strip()) for line in f.readlines()]

def part_one(display_outputs):
    return len([o for output in display_outputs for o in output[1].split(' ') if len(o) in (2,4,3,7)])

def part_two(display_outputs):
    total2 = 0
    for output in display_outputs:
        values = {}
        
        for i in output[0].split(' '):
            if len(i) == 2:
                values[1] = i
            if len(i) == 4:
                values[4] = i
            if len(i) == 3:
                values[7] = i
            if len(i) == 7:
                values[8] = i
        while len(values) != 10:
            for i in output[0].split(' '):
                if len(i) == 5 and all((c in i for c in values[1])):
                    values[3] = i
                if len(i) == 5 and values.get(6, None):
                    if len([c for c in values[6] if c in i]) == 5:
                        values[5] = i

                if len(i) == 5 and values.get(5, None) and values.get(3, None):
                    if i != values[5] and i != values[3]:
                        values[2] = i
                if len(i) == 6:
                    missing_digits = [c for c in values[1] if c not in i]
                    if missing_digits:
                        values[6] = i
                    if values.get(3, None) and values.get(6, None):
                        if all([c in i for c in values[3]]):
                            values[9] = i
                        elif values[6] != i:
                            values[0] = i

        z = ''
        for o in output[1].split(' '):
            for k, v in values.items():
                if all([c in v for c in o]) and len(v) == len(o):
                    z += str(k)
        total2 += int(z)
    return total2
