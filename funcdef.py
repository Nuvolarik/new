def print_params(a, b, c):
    print(a, b, c)

print_params('Girl', True, 5)

print('---------')

def func_with_params(a, b=3):
    print(a + b)

func_with_params(4)
func_with_params(4)
func_with_params(4)
func_with_params(4)

print('---------')

def func_with_params2(a, b=3, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)

func_with_params2(4)
func_with_params2(7)
func_with_params2(15)
func_with_params2(2)