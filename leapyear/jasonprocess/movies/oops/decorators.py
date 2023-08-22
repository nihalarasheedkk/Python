
# rule1=> decorator always take a function as a parameter(the fn we wanna decorate)
#rule2=> there'll be a an inner f/n()=> (eth functna dec chyynde ayinta parameter)


# def dec_fun(fn): #fn=sub(10,20)
#     def inner_fun(n1,n2): #inner_fun(10,20)   def function is calling the inner f/n
#         if n1<n2:
#             (n1,n2)=(n2,n1) #n1=20 n2=10
#         return fn(n1,n2) #sub(20,10)
#     return inner_fun

# @dec_fun
# def sub(n1,n2):
#     return n1-n2
# @dec_fun
# def div(n1,n2):
#     return n1/n2

# print(sub(10,20)) 
   


def dec_square(fn):
    def wrapper(n1,n2):
        return fn(n1**2,n2**2)
    return wrapper

@dec_square
def add(n1,n2):
    return n1+n2

@dec_square
def product(n1,n2):
    return n1*n2

print(add(2,3))

print(product(2,3))        #db

# class Parent:
#     def property(self):
#         print("2car 5kg gold 10lakh rs")


#     def proposal(self):
#         print("mrg with gopal")

# class Child(Parent):
#     def proposal(self):
#         print("amal")

# ch=Child()

# ch.property()
# ch.proposal()