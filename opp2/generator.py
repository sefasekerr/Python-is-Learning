import sys
# def fib(max):
#     fib_list=[]
#     a,b =0,1
#     while(len(fib_list)<max):
#         fib_list.append(b)
#         a,b = b,b+a
#         yield b
# def gen_fib(max):
#     a,b =0,1
#     countv =0
#     while(countv<=max):
        
#         yield b
#         a,b=b,b+a
#         countv+=1
# print(fib(100))
# print(sys.getsizeof(fib(100)))


# generator = fib(100)
# gen_fibo = gen_fib(100)
# print(next(gen_fibo))
# print(next(gen_fibo))
# print(next(gen_fibo))
# print(next(gen_fibo))
# print(next(gen_fibo))
# print(next(gen_fibo))
# print(next(gen_fibo))
# print(next(gen_fibo))



def sayac(start,stop):
    if(start<stop):
        while(start<stop):
            yield start
            start+=1
            
def counter(start,stop):
    liste = []
    if(start<stop):
        while(start<stop):
            liste.append(start)
            start+=1
        return liste 
            
# generator = sayac(1,10)
# print(next(generator))

# generator = counter(1,10)
# generator =iter(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# sayilar = sayac(1,50)
# while(True):
#     try:
#         print(next(sayilar))
        
#     except StopIteration:
#         break
print(
f"________________________\n"
f"|      *base word      |\n"
f"|                      |\n"
f"|      >helper word    |\n"
f"|      >helper word    |\n"
f"|      >helper word    |\n"
f"|      >helper word    |\n"
f"|                      |\n"
f"|                      |\n"
f"|                      |\n"
f"‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
)
