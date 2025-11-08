# same test.py 
# run austin: austin-tui  python3 try.py  if in terminal  or austin-web  python3 try.py if web and austin  python3 try.py normal
import cProfile
import pstats
import time

def add(x,y):
    result=0
    result+=x
    result+=y
    return result

def fact(n):
    result=1
    for i in range(1,n+1):
        result *=i
    return result

def do_stuf():
    result=[]
    for x in range(1000):
        result.append(x**2)
    return result

def waste_time():
    time.sleep(5)
    print("Hello")
    
if __name__=="__main__":
    with cProfile.Profile() as profile:
        r1=add(100,500)
        print(r1)
        r2=fact(700)
        print(r2)
        r3=do_stuf()
        print(r3)
        waste_time()
    
    result=pstats.Stats(profile)
    result.sort_stats(pstats.SortKey.TIME)
    result.print_stats()
    result.dump_stats("result.prof") # This is for the tuna