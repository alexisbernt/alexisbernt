# a function
def function(parametera, parameterb):
    #this is a while loop
    while parameterb != 0:
        parameterc = parameterb - 1
        print(parameterc)  # Print the modified value of parameterb (now parameterc)
        parameterb -= 1
        function(parametera, parameterb)  # Recursive call with updated value

def function(parameterb):
    if parameterb == 0:
        return  # Base case to stop recursion
    print(parameterb - 1)
    function(parameterb - 1)  # Reduce parameterb on each call

parameter1 = 5
parameter2 = 13

# function(parameter1, parameter2)
function(parameter2)

# Python built-in functions: https://www.w3schools.com/python/python_ref_functions.asp