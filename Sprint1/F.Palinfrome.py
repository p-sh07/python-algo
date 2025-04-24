from sys import stdin

def is_palindrome(line):
    if len(line) == 0:
        return True

    i, j = 0, -1

    while i < len(line) + j:
        while not line[i].isalnum():
            i += 1
        while not line[j].isalnum():
            j -= 1
        if line[i].lower() != line[j].lower():
            return False
        i, j = i + 1, j - 1

    return True


def main():
    print(is_palindrome(stdin.readline().rstrip()))


if __name__ == '__main__':
    main()