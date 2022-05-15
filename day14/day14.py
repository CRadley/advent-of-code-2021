from collections import defaultdict


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()
        instructions = {}
        for line in lines[2:]:
            y, z = line.strip().split(" -> ")
            instructions[y] = f"{y[0]}{z}{y[1]}"

    return lines[0].strip(), instructions



def extract_pairs(s):
    return [f"{v}{s[i+1]}" for i, v in enumerate(s[:-1])]

def char_freq(s):
    return [(c, s.count(c)) for c in set(s)]
        


def determine_polymer(polymer, rules, steps):
    for _ in range(steps):
        pairs = extract_pairs(polymer)
        polymer = "".join(rules[p] if not i else rules[p][1:] for i, p in enumerate(pairs))
    freq = char_freq(polymer)
    return max(freq, key=lambda x: x[1])[1] - min(freq, key=lambda x: x[1])[1]


def optimised_determine_polymer(polymer, rules, steps):
    counts = defaultdict(int)
    for c in set(polymer):
        counts[c] = polymer.count(c)
    pairs = extract_pairs(polymer)
    cache = {p: pairs.count(p) for p in set(pairs)}
    for _ in range(steps):
        temp_cache = defaultdict(int)
        for pair in cache:
            rule = rules[pair]
            temp_cache[rule[:-1]] += cache[pair]
            temp_cache[rule[1:]] += cache[pair]
            counts[rule[1]] += cache[pair]
        cache = temp_cache.copy()
    return max(counts.values()) - min(counts.values())

def test_determine_polymer_10_steps() -> None:
    polymer_template, insertertion_rules = read_file("day14.txt")
    assert 2435 == determine_polymer(polymer_template, insertertion_rules, 10)

def test_optimised_determine_polymer_10_steps() -> None:
    polymer_template, insertertion_rules = read_file("day14.txt")
    assert 2435 == optimised_determine_polymer(polymer_template, insertertion_rules, 10)

def test_optimised_determine_polymer_40_steps() -> None:
    polymer_template, insertertion_rules = read_file("day14.txt")
    assert 2587447599164 == optimised_determine_polymer(polymer_template, insertertion_rules, 40)