import time
import os

frameList = [
''' 
	  
     
    (0_0)   
     /|\  
     / \  
          ''' , '''
      
    (-O-) 
     /|\   
	 / \ 
            '''	
		
]


while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(.3)