payments={
0: {'gas': 10,'water':10,'heat':10,'sewer':10,'misc':10},
1: {'gas': 10,'water':10,'heat':10,'sewer':10,'misc':10}, 
2: {'gas': 10,'water':10,'heat':10,'sewer':10,'misc':10}, 
}


def ADD(nr:int,type:str,sum:float):
        payments[nr][type]=sum


ADD(3,'gas',11)
print(payments)



