import time
import threading

def calculate_square(numbers):
    print("sayılar hesaplanıyor...")
    
    for i in numbers:
        time.sleep(0.3)
        print("kare", i*i)
        
def calculate_cube(numbers):
    print("sayılar hesaplanıyor...")
    for i in numbers:
        time.sleep(0.3)
        
        print("kübü:",i*i*i)
        
        
sayilar = [3,6,9,96,93,63,33]
sayilar2 = [3,6,9,96,93,93,33333333]

t=time.time()


# calculate_cube(sayilar)
# calculate_square(sayilar)

t1 = threading.Thread(target=calculate_cube,args=(sayilar2,))
t2 = threading.Thread(target=calculate_square,args=(sayilar2,))
t1.start()
t2.start()
t1.join()
t2.join()

print(f"zaman: {(time.time()-t)}")