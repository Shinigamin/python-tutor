import time

def decor(func):

    def wrapper(n):
        start = time.time()

        result = func(n)

        end = time.time()
 
        print(end - start)
        return result

    return wrapper

@decor
def fat():
    print('foo')
    time.sleep(5)
    print('bar')



f = decor(fat)
