'''
Created on 09-May-2017

@author: Rajat Sachdeva

'''
'''
The year can be evenly divided by 4, unless;
The year cannot be evenly divided by 100, unless;
The year is also evenly divisible by 400. Then it is a leap year.
'''
import calendar

def is_leap(year):
    leap = False
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0 ):
        leap = True 
    return leap

def main():
    year = int(raw_input())
    print is_leap(year)

def test():
    p, fail , total = 0, 0 , 0
    for year in range(2017):
        total += 1
        result = is_leap(year)
        if result == calendar.isleap(year):
            print 'Test Case {} PASS'.format(year + 1)
            p += 1
        else:
            print 'Test Case {} FAILED'.format(year + 1)
            fail += 1
            
    print "Total Cases: {} Pass: {} Fail: {}".format(total, p, fail)
if __name__ == '__main__': test()