TRANSLATION = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

def hex_to_binary(hex_string: str) -> str:
    return "".join([TRANSLATION[char] for char in hex_string])


def determine_input_binary(filepath) -> str:
    with open(filepath, "r") as input_hex_file:
        return hex_to_binary(input_hex_file.read().strip())


def calculate_version_sum(binary: str) -> int:
    return 0