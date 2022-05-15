from typing import List
from aoc.utils import file_as_list, display_solutions

def get_counts(bins: List[int]) -> int:
    counts = [[0,0] for _ in range(len(str(bins[0])))]
    for bin_ in bins:
        for (i, bit) in enumerate(str(bin_)):
            counts[i][int(bit)] += 1
    return counts

def part_one(bins: List[int]) -> int:
    counts = get_counts(bins)
    g = "".join(map(str, [int(count[0] < count[1]) for count in counts]))
    e = "".join(map(str, [int(count[0] > count[1]) for count in counts]))
    return int(g, 2) * int(e,2)

def part_two(bins: List[int]) -> int:
    counts = get_counts(bins)
    output_bins_o = [x for x in bins]
    output_bins_c = [x for x in bins]
    for i, _ in enumerate(counts):
        o_counts = get_counts(output_bins_o)
        c_counts = get_counts(output_bins_c)
        most_common = str(int(o_counts[i][1] >= o_counts[i][0]))
        least_common = str(int(c_counts[i][1] < c_counts[i][0]))
        if len(output_bins_o) > 1:
            output_bins_o = [bin_ for bin_ in output_bins_o if bin_[i] == most_common]
        if len(output_bins_c) > 1:
            output_bins_c = [bin_ for bin_ in output_bins_c if bin_[i] == least_common]
    return int(output_bins_o[0], 2) * int(output_bins_c[0],2)