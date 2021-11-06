

def some_decorator(f):
  def function_wrapper():
    print('before')
    f()
    print('after')
  return function_wrapper


def some_function():
  print("This is some function")

#wrapper_function = some_decorator(some_function)
#wrapper_function()

@some_decorator
def some_other_function():
  print("This is some other function")

some_other_function()


