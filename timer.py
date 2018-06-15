import time
def timeit(f):
    def new_f(*args):
        start = time.time()
        f(*args)
        print("Function "+f.__name__ + " took "+str(round((time.time()-start)*1000, 2)) + " milliseconds")
    return new_f
