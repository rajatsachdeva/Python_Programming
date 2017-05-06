#!/usr/bin/python3

def main():
    # simple fibonacci series
    # the sum of two elements defines the next set
    a, b = 0, 1
    print(a, end = ' ')
    while b < 50:
        print(b, end=' ')
        a, b = b, a + b

if __name__ == "__main__": main()
