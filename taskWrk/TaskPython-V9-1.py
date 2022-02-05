# *** Import

#  Import, from, as

#  Простой вариант


#import factory.pipe
#from factory import pipe
from factory.pipe import pipe as fun_pipe

if __name__ == '__main__':
    for _, towel in zip(range(4), fun_pipe()):
        print(towel)


# End