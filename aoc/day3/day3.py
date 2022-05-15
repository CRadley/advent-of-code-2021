from typing import List
from aoc.utils import file_as_list, display_solutions

def get_counts(bins: List[int]) -> int:
    counts = [[0,0] for _ in range(len(str(bins[0])))]
    for bin_ in bins:
        for (i, bit) in enumerate(str(bin_)):
            counts[i][int(bit)] += 1
    return counts

def part_one(bins: List[int]) -> int:
    counts = [[0,0] for _ in range(len(str(bins[0])))]
    for bin_ in bins:
        for (i, bit) in enumerate(str(bin_)):
            counts[i][int(bit)] += 1
    g = ''
    e = ''
    for count in counts:
        if count[0] < count[1]:
            g += str(1)
            e += str(0)
        else:
            g += str(0)
            e += str(1)
    return int(g, 2) * int(e,2)

def part_two(bins: List[int]) -> int:
    counts = get_counts(bins)
    output_bins_o = bins[:]
    output_bins_c = bins[:]
    for bin_ in bins:
        for (i, bit) in enumerate(str(bin_)):
            counts[i][int(bit)] += 1
    for i, _ in enumerate(counts):
        o_counts = get_counts(output_bins_o)
        c_counts = get_counts(output_bins_c)
        x = '1' if o_counts[i][1] >= o_counts[i][0] else '0'
        y = '1' if c_counts[i][1] < c_counts[i][0] else '0'
        if len(output_bins_o) > 1:
            output_bins_o = [bin_ for bin_ in output_bins_o if bin_[i] == x]

        if len(output_bins_c) > 1:
            output_bins_c = [bin_ for bin_ in output_bins_c if bin_[i] == y]
    return int(output_bins_o[0], 2) * int(output_bins_c[0],2)

def main():
    inputs = file_as_list('./inputs/3.txt')
    solution_one = part_one(inputs)
    solution_two = part_two(inputs)
    display_solutions(solution_one, solution_two)

if __name__ == '__main__':
    main()

#Solution 1: 3320834
#Solution 2: 4481199