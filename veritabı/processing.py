import multiprocessing
import time



def calculate_square(numbers,liste):
    print("sayılar hesaplanıyor...")

    for index,i in enumerate( numbers):
        time.sleep(0.3)
        # print("kare", i*i)
        liste[index]=(i*i)
        
def calculate_cube(numbers,liste):
    print("sayılar hesaplanıyor...")
    for index,i in enumerate(numbers):
        time.sleep(0.3)
        liste[index]=(i*i*i)
        # print("kübü:",i*i*i)
        
        
        
if __name__=="__main__":
    arr = [3,6,9,96,93,93,39,9]
    
    t = time.time()
    liste_square = multiprocessing.Array('i',len(arr))
    liste_cube = multiprocessing.Array('i',len(arr))
    
    p1 = multiprocessing.Process(target=calculate_cube,args=(arr,liste_cube,))
    p2 = multiprocessing.Process(target=calculate_square,args=(arr,liste_square,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
      
    print(time.time()-t)
    
    print(liste_cube[:])
    print(liste_square[:])
