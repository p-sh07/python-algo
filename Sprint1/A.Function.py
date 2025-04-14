import sys

#Read 4 numbers and compute result of quadratic equation
def main():
    line = sys.stdin.readline().rstrip()
    a, x, b, c = (int(num) for num in line.split())
    print(a * x * x + b * x + c)


if __name__ == '__main__':
    main()