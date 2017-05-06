#!/usr/bin/python3

# Break, Continue and else

def main():
    s = 'this is a string'
    for c in s:
        print(c, end='')
    print()
    
    for c in s:
        # skip 's'
        if c == 's': continue
        print(c, end='')
    print()
    
    for c in s:
        # stop at first 's'
        if c == 's': break
        print(c, end='')
    print()
    
    # else in for
    for c in s:
        print(c, end='')
    else:
        print('\nelse')
        
    i = 0
    while(i < len(s)):
        print(s[i], end = '')
        i += 1
    else:
        print (' else')
if __name__ == "__main__": main()
