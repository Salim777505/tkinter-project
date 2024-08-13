# # write a python program that calculat the fibonichy of a numbdr?
# def fib(n):
#     n=int(input("please Enter your number :"))
#     n1=0
#     n2=1
#     count=0
#     if n<=0:
#         print("please Enter a positive number :")
#         fib()
#     elif n==1:
#         print(n1=0)
#     else:
#         n1=n2
#         while count<n:
#             print(n1)
#             ntotal=n1+n2
#             n1=n2
#             n2=ntotal
#             count+=1

# # if __name__=="__msin__"
# fib(())

def fib(n):
    n=int(input("plese enter your number?"))
    n1=0
    n2=1
    count=0
    if n<=0:
        print("please enter a positive number!")
        fib()
    elif n==1:
        print(n1=0)
    else:
        n1=n2
        while count<n:
            print(n1)
            ntotal=n1+n2
            n1=n2
            n2=ntotal
            count+=1

fib(())