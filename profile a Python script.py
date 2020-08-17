import cProfile

def sum():
    print(1,100)

cProfile.run('sum()')