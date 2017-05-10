'''
Created on 09-May-2017

@author: Rajat Sachdeva

'''
'''
Use of _ in loops
It's just a variable name, and it's conventional in python to use _ for throwaway variables. 
It just indicates that the loop variable isn't actually used.
'''
marksheet = []
def main():
    for _ in range(int(raw_input())):
        _name = raw_input()
        _score = float(raw_input())
        temp = [_name, _score]
        marksheet.append(temp)
       # second_highest = sorted(list(set(marks for name)))
    print students
    
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
    
if __name__ == '__main__':
    main()