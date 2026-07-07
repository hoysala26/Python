simple_list = ('a', 'b', 'c')

print(*simple_list)

def func(*args):
    print(args)

func(1,2,3,4,4,56)


def func(**kwargs):
    print(kwargs)

func(item_1="box",item_2="ball")    