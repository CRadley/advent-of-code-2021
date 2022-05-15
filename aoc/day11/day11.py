RESOLUTION = 10
ROWS = 10

def get_octopi(filepath):
    with open(filepath, "r", encoding="utf-8") as input_file:
        return [int(y) for x in input_file.readlines() for y in x.strip()]

def part_one(inputs):
    octopi = inputs[:] # Prevents mutating input_file_content
    step_count = 100
    flashes = 0
    for _ in range(step_count):
        to_flash = []
        has_flashed = []
        for i, _ in enumerate(octopi):
            octopi[i] += 1
            if octopi[i] > 9:
                to_flash.append(i)
                has_flashed.append(i)
        
        while to_flash:
            store = []
            for flash in to_flash:
                indexes_to_check = []
                
                if flash >= RESOLUTION:
                    if flash % RESOLUTION or not (flash - RESOLUTION - 1):
                        indexes_to_check.append(flash - RESOLUTION - 1)
                    indexes_to_check.append(flash - RESOLUTION)
                    if flash % RESOLUTION != RESOLUTION - 1:
                        indexes_to_check.append(flash - RESOLUTION + 1)
                
                if flash % RESOLUTION:
                    indexes_to_check.append(flash - 1)
                
                if flash % RESOLUTION != RESOLUTION - 1:
                    indexes_to_check.append(flash + 1)
                
                
                if flash < RESOLUTION * (ROWS - 1):
                    if flash % RESOLUTION:
                        indexes_to_check.append(flash + RESOLUTION - 1)
                    indexes_to_check.append(flash + RESOLUTION)
                    if flash % RESOLUTION != RESOLUTION - 1  and (flash + RESOLUTION + 1) < 100:
                        indexes_to_check.append(flash + RESOLUTION + 1)
                for j in indexes_to_check:
                    octopi[j] += 1
                    if octopi[j] > 9 and j not in has_flashed:
                        store.append(j)
                        has_flashed.append(j)
            to_flash = [x for x in store]
        
        for hf in has_flashed:
            flashes += 1
            octopi[hf] = 0
    return flashes


def part_two(inputs):
    octopi = inputs[:]
    c = 0
    while True:
        c += 1
        to_flash = []
        has_flashed = []
        for i, _ in enumerate(octopi):
            octopi[i] += 1
            if octopi[i] > 9:
                to_flash.append(i)
                has_flashed.append(i)
        
        while to_flash:
            store = []
            for flash in to_flash:
                indexes_to_check = []
                
                if flash >= RESOLUTION:
                    if flash % RESOLUTION or not (flash - RESOLUTION - 1):
                        indexes_to_check.append(flash - RESOLUTION - 1)
                    indexes_to_check.append(flash - RESOLUTION)
                    if flash % RESOLUTION != RESOLUTION - 1:
                        indexes_to_check.append(flash - RESOLUTION + 1)
                
                if flash % RESOLUTION:
                    indexes_to_check.append(flash - 1)
                
                if flash % RESOLUTION != RESOLUTION - 1:
                    indexes_to_check.append(flash + 1)
                
                
                if flash < RESOLUTION * (ROWS - 1):
                    if flash % RESOLUTION:
                        indexes_to_check.append(flash + RESOLUTION - 1)
                    indexes_to_check.append(flash + RESOLUTION)
                    if flash % RESOLUTION != RESOLUTION - 1  and (flash + RESOLUTION + 1) < 100:
                        indexes_to_check.append(flash + RESOLUTION + 1)
                for j in indexes_to_check:
                    octopi[j] += 1
                    if octopi[j] > 9 and j not in has_flashed:
                        store.append(j)
                        has_flashed.append(j)
            to_flash = [x for x in store]
        
        for hf in has_flashed:
            octopi[hf] = 0
        if all((o == 0 for o in octopi)):
            return c