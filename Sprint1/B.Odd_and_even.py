import sys

def even(num):
    return int(num) % 2 == 0

def main():
    line = sys.stdin.readline().rstrip()
    nums = line.split()

    if even(nums[0]) == even(nums[1]) == even(nums[2]):
        print("WIN")
    else:
        print("FAIL")


if __name__ == '__main__':
    main()