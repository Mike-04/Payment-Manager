payments={}
import random
changes=[]

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
ADD(0,{'gas': 10,'water':10,'heat':10,'sewer':10,'misc':10},changes)
ADD(1,{'gas': 10,'water':10,'heat':10,'sewer':10,'misc':10},changes)
ADD(2,{'gas': 10,'water':10,'heat':10,'sewer':10,'misc':10},changes)
DEL(2,changes)
print(payments)
print('----------------------------------------')
print(changes)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('start undo')
UNDO(payments,changes)
print(payments)
print('----------------------------------------')
print(changes)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
UNDO(payments,changes)
print(payments)
print('----------------------------------------')
print(changes)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
UNDO(payments,changes)
print(payments)
print('----------------------------------------')
print(changes)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
ADD(2,{'gas': 10,'water':10,'heat':10,'sewer':10,'misc':10},changes)
print(payments)
print('----------------------------------------')
print(changes)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
ADD(2,{'gas': 11,'water':11,'heat':11,'sewer':11,'misc':11},changes)
print(payments)
print('----------------------------------------')
print(changes)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
UNDO(payments,changes)
print(payments)
print('----------------------------------------')
print(changes)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

