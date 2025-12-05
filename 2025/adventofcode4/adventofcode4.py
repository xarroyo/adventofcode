import copy
from hmac import new

from infrastructue.files import read_file_to_list


def forkliftrolls(matrix):
    removable = 0
    new_matrix = copy.deepcopy(matrix)
    while True:
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                if matrix[x][y] == '@' and has_less_than_4(matrix, x, y):
                    new_matrix[x][y] = 'x' if matrix[x][y] == '@' else matrix[x][y]
                    removable+=1
        if new_matrix == matrix:
            break
        matrix = copy.deepcopy(new_matrix)
    return removable, new_matrix


def has_less_than_4(matrix, x: int, y: int, size: int = 1):
    return count_adjacent_rolls(matrix, x, y) < 4


def count_adjacent_rolls(matrix, x: int, y: int, size: int = 1):
    counter = 0
    for r in range(1, size+1):
        for i in range(-r, r+1):
            for j in range(-r, r+1):
                if i == 0 and j == 0:
                    continue
                if x+i < 0 or y+j < 0 or x+i >= len(matrix) or y+j >= len(matrix):
                    continue
                # print(f"{x+i=} {y+j=} - {r=} - {matrix[x+i][y+j]=}")
                if matrix[x+i][y+j] == '@':
                    counter+=1
    return counter


if __name__ == "__main__":
    data = read_file_to_list("2025/adventofcode4/input.txt")
    rolls, new_state = forkliftrolls([list(l) for l in data])
    print(rolls)