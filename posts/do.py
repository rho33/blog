import time

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')
    with open('test.txt', mode='w') as f:
        f.write('testing...')