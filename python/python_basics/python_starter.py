# a function
def function(parametera, parameterb):
    #this is a while loop
    while parameterb != 0:
        parameterc = parameterb - 1
        print(parameterc)  # Print the modified value of parameterb
        parametera -= 1  # Correctly decrement parametera
        parameterb -= 1
        function(parametera, parameterb)  # Recursive call with updated value

parameter = 5
parameter2 = 13

function(parameter, parameter2)