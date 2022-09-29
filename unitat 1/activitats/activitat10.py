lis1 = [1,2,3,4,5] 
  
parells = lambda x: x % 2 == 0
imparrells=lambda x: x % 2 != 0
  
lis2 = list(filter(parells, lis1)) 
lis3=list(filter(imparrells,lis1))
print(lis2)
print(lis3) 