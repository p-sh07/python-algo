from sys import stdin

def main():
    text_len = int(input())
    words = stdin.readline().rstrip().split()

    longest_word = ''
    max_length = 0

    for word in words:
        length = len(word)
        if max_length < length:
            max_length = length
            longest_word = word

    print(longest_word)
    print(max_length)


if __name__ == '__main__':
    main()