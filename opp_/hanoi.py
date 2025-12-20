class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)
print(a)



# Recursive function for Tower of Hanoi
# def hanoi(disks, source, helper, destination):
#     # Base Condition
#     if (disks == 1):
#         print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
#         return

#     # Recursive calls in which function calls itself.
#     hanoi(disks - 1, source, destination, helper)
#     print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
#     hanoi(disks - 1, helper, source, destination)

# # Driver code: Initializing and calling the function
# disks = int(input('Number of disks to be displaced: '))
# '''
# Tower names passed as arguments:
# Source: A
# Helper: B
# Destination: C
# '''
# # Actual function call
# hanoi(disks, 'A', 'B', 'C')

# numbers = [15, 30, 47, 82, 95]
# def lesser(numbers):
#    return numbers < 50

# small = list(map(lesser, numbers))
# print(small)

# some = ["aaa", "bbb"]

# 1
# def aa( some):
#    return

# print(aa(some))

# def aa():
#    return "aaa"

# print(aa())

