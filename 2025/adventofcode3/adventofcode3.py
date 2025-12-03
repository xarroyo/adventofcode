from infrastructue.files import read_file_to_list


def joltage(data):
    return sum(int(maxbateryjoltage(list(str(v)))) for v in data)

def maxbateryjoltage(digits, nbateries=12):
    offset= len(digits) - nbateries + 1
    maxvalue = max(digits[:offset])
    index = digits.index(maxvalue, 0, offset)

    if len(digits) == nbateries:
        return "".join(digits)

    if nbateries == 1:
        return str(maxvalue)

    return str(maxvalue) + maxbateryjoltage(digits[index+1:], nbateries-1)

if __name__ == "__main__":
    data = read_file_to_list("2025/adventofcode3/input.txt")
    print(joltage(data))