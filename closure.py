def outer_fun():
    message = "Hi"

    def inner_fun():
        print(message)

    return(inner_fun)

my_func = outer_fun()        

print(my_func())   