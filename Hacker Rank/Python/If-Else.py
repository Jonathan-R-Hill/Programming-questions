if __name__ == '__main__':
    n = int(raw_input().strip())

if n % 2 == 1:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
elif 2 <= n <= 5:
    print('Not Weird')
elif 6 <= n <= 20:
    print('Weird')
else:
    pass