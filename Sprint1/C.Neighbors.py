import sys

# mat -> [row][col] -> [y][x]
# returns answer as string
def get_neighbors(mat, row, col):
    if not mat:
        return []

    neighbors = []

    #case when there are neibs left/up
    if col > 0:
        neighbors.append(mat[row][col - 1])
    if row > 0:
        neighbors.append(mat[row - 1][col])

    max_row = len(mat) - 1 # max index is 1 less than len
    max_col = len(mat[0]) - 1

    # case when there is a neib to the right/down
    if row < max_row:
        neighbors.append(mat[row + 1][col])
    if col < max_col:
        neighbors.append(mat[row][col + 1])

    neighbors.sort(key = int)
    return " ".join(neighbors)

def main():
    rows = int(input())
    cols = int(input())

    mat = []
    for i in range(rows):
        line = sys.stdin.readline().rstrip()
        mat.append(line.split()) # NB: this stores values as strings,
                                 # so need to use key=int when sorting
    row = int(input())
    col = int(input())

    print( get_neighbors(mat, row, col) )

if __name__ == '__main__':
    main()