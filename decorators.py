import time

def decor(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__+" took "+str((end-start)*1000)+ "mil sec")
        print("HIIIIIII")
        return result
    return wrapper



@decor
def calc_square(numbers):
    sq = []
    for i in numbers:
        sq.append(i*i)
    
    return sq

@decor
def calc_cube(numbers):
    cu = []
    for i in numbers:
        cu.append(i*i*i)

    return cu

calc_cube([1,2,3,4,5])
calc_square([1,2,3,4,5])


