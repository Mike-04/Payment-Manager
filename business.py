import service

def inDEL(payments:dict,nr:int):
        '''
        The `inDEL` function deletes a payment dictionary.
        args:
        payments(dict):dictionary of all payments
        nr(int):number of apartment that has to be modified
        returns nothing
        '''
        if nr in payments:
                del(payments[nr])

def inADD(payments:dict,nr:int,val:dict):
        '''
        The `inADD` function updates a payment dictionary.
        args:
        payments(dict):dictionary of all payments
        nr(int):number of apartment that has to be modified
        val(dict):value to be introduced or modified
        returns nothing
        '''
        if nr not in payments:
                payments[nr]=val
        else:
                payments[nr].update(val)

def UNDO(payments:dict,changes:list):
        '''
        The UNDO function reverses the most recent payment operation recorded in the changes list and updates the payments dictionary accordingly
        args:
        payments(dict):dictionary of all payments
        changes(list):list where changes are recorded
        returns nothing
        '''
        if len(changes):
                op=changes[len(changes)-1]['op']
                nr=changes[len(changes)-1]['nr']
                init=changes[len(changes)-1]['init']
                fin=changes[len(changes)-1]['fin']
                del changes[-1]
                match op:
                        case 'DEL':
                                inADD(payments,nr,init)
                        case 'MOD':
                                inADD(payments,nr,init)
                        case 'ADD':
                                inDEL(payments,nr)
                        case 'mDEL':
                                service.mass_undo(nr)
                        case 'mMOD':
                                service.mass_undo(nr)
                
        else:
               print("Nothing to undo")

def ADD(payments:dict,nr:int,val:dict,changes:list):
        '''
        The `ADD` function updates a payment dictionary and records the type of operation ('MOD' or 'ADD').
        args:
        payments(dict):dictionary of all payments
        nr(int):number of apartment that has to be modified
        val(dict):value to be introduced or modified
        changes(list):list where changes are recorded
        returns nothing
        '''
        template={'gas':0,'water':0,'heat':0,'sewage':0,'misc':0,'date':'NaN'}
        op='MOD'
        if nr not in payments:
                payments[nr]=val
                op='ADD'
                changes.append({'op':op,'nr':nr,'init':template,'fin':val})
        else:
                init=payments[nr].copy()
                changes.append({'op':op,'nr':nr,'init':init,'fin':val}) 
                payments[nr].update(val)

def DEL(payments:dict,nr:int,changes:list):
        '''
        The `DEL` function deletes a payment dictionary and records the type of operation.
        args:
        payments(dict):dictionary of all payments
        nr(int):number of apartment that has to be modified
        changes(list):list where changes are recorded
        returns nothing
        '''
        if nr in payments:
                op='DEL'
                init=payments[nr].copy()
                changes.append({'op':op,'nr':nr,'init':init,'fin':'NaN'}) 
                del(payments[nr])
        else:
                raise IndexError("Index not in payments")
