
import random
import pprint
payments={}
'''
changes=[
{'op':'ADD','nr':nr,'init':{},'fin':{}}
]
'''
def ADD(nr:int,val:dict,changes:list):
        op='MOD'
        if nr not in payments:
                payments[nr]=val
                op='ADD'
                changes.append({'op':op,'nr':nr,'init':{'gas':0,'water':0,'heat':0,'sewage':0,'misc':0},'fin':val})
        else:
                init=payments[nr].copy()
                changes.append({'op':op,'nr':nr,'init':init,'fin':val}) 
                payments[nr].update(val)


def DEL(nr:int,changes:list):
        if nr in payments:
                op='DEL'
                init=payments[nr].copy()
                changes.append({'op':op,'nr':nr,'init':init,'fin':'NAN'}) 
                del(payments[nr])

def inDEL(nr:int,changes:list):
        if nr in payments:
                del(payments[nr])

def inADD(nr:int,val:dict,changes:list):
        if nr not in payments:
                payments[nr]=val
        else:
                payments[nr].update(val)

def UNDO(payments:dict,changes:list):
        if len(changes):
                op=changes[len(changes)-1]['op']
                nr=changes[len(changes)-1]['nr']
                init=changes[len(changes)-1]['init']
                fin=changes[len(changes)-1]['fin']
                #print(op,nr,init,fin)
                match op:
                        case 'DEL':
                                inADD(nr,init,changes)
                        case 'MOD':
                                inADD(nr,init,changes)
                        case 'ADD':
                                inDEL(nr,changes)
                del changes[-1]  

def main():

        changes=[]

        while(True):
                print("Choices:")
                print("1: Adds or modifies an entry")
                print("2: Deletes an entry")
                print("3: Undo")
                print("4: Prints list")
                print("5: Exits the program")
                req=int(input("Make a selection: "))
                match req:
                        case 1:
                                nr=int(input("Nr:"))
                                gas=int(input("Gas:"))
                                water=int(input("Water:"))
                                heat=int(input("Heat:"))
                                sewage=int(input("Sewage:"))
                                misc=int(input("Misc:"))
                                ADD(nr,{'gas': gas,'water':water,'heat':heat,'sewage':sewage,'misc':misc},changes)
                        case 2:
                                nr=int(input("Nr:"))
                                DEL(nr,changes)
                        case 3:
                                UNDO(payments,changes)
                        case 4:
                                pprint.pprint(payments)
                        case 5:
                                break
                        case _:
                                print("Invalid input!")

main()
