'''
Created on 09-May-2017

@author: Rajat Sachdeva
'''
''' Lists
insert i e: Insert integer e at i position .
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''
# declare an empty list
l = []

def main():
    # Take number of operations from User
    N = int(raw_input())
    for i in range(N):
        list_operations()
        
def list_operations():
    request_str = raw_input().split(' ')        
    command = request_str[0]
    
    # check which operations to perform
    if command == 'insert':
        pos = int(request_str[1])
        val = int(request_str[2])
        l.insert(pos, val)
    elif command == 'print':
        print l
    elif command == 'append':
        val = int(request_str[1])
        l.append(val)
    elif command == 'sort':
        l.sort()
    elif command == 'remove':
        val = int(request_str[1])
        l.remove(val)
    elif command == 'pop':
        l.pop()
    elif command == 'reverse':
        l.reverse()
    else:
        print "incorrect operation"
            
if __name__ == '__main__':
    main()