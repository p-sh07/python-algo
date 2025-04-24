from sys import stdin

def compute_chaotic_days(num_days, temp_data):
    if num_days != len(temp_data):
        return -1 #input error

    if num_days == 1:
        return 1 #only one day data -> chaotic

    num_chaotic = 0
    for i, t in enumerate(temp_data):
        #check that neither of next temps is less or equal to today
        if (i != 0 and t <= temp_data[i - 1]) or (i != num_days - 1 and t <= temp_data[i + 1]):
            continue
        else:
        #count day only if both next temps, if present, are higher
            num_chaotic += 1

    return num_chaotic


def main():
    num_days = int(input())
    temp_data = [int(t) for t in stdin.readline().rstrip().split()]

    print( compute_chaotic_days(num_days, temp_data) )


if __name__ == '__main__':
    main()