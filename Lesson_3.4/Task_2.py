#######################################Task 2#######################################
#
# 
def square(func):
    def inner(n):
        result = func(n)
        return result ** 2
    return inner 

@square
def function(n):
    return n

print(function(1))
print(function(6))
print(function(4))
print(function(7)) 
print(function(12))
# 
# 
1
36
16
49
144
# 
# 