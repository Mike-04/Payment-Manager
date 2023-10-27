'''Operations'''
def ADD(payments:dict,nr:int,val:dict,changes:list):
        '''
        The `ADD` function updates a payment dictionary and records the type of operation ('MOD' or 'ADD').
        args:
        payments(dict):dictionary of all payments
        nr(int):number of apartment that has to be modified
        val(dict):value to be intorduced or modified
        changes(list):list where changes are recorded
        returns nothing
        '''
        op='MOD'
        if nr not in payments:
                payments[nr]=val
                op='ADD'
                changes.append({'op':op,'nr':nr,'init':{'gas':0,'water':0,'heat':0,'sewage':0,'misc':0,'date':'NaN'},'fin':val})
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

def mass_DEL(payments,start,end,changes):
        '''
        The `mass_DEL` function deletes payments between the indexes start and end records the type of operation.
        args:
        payments(dict):dictionary of all payments
        start,end(int):indexes where apartments are to be deleted
        changes(list):list where changes are recorded
        returns nothing
        '''
        for nr in range (start, end+1):
              DEL(payments,nr,changes)
        changes.append({'op':'mDEL','nr':end-start+1,'init':'NaN','fin':'NaN'}) 

def mass_UNDO(payments,changes,rec):
        '''
        The mass_UNDO function iteratively undoes changes in a payment dictionary based on a specified number of records (rec).
        payments(dict):dictionary of all payments
        rec(int):number of undos to be made
        changes(list):list where changes are recorded
        returns nothing
        '''
        for i in range(0,rec):
              UNDO(payments,changes)

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
        val(dict):value to be intorduced or modified
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
                                mass_UNDO(payments,changes,nr)
                        case 'mMOD':
                                mass_UNDO(payments,changes,nr)
                
        else:
               print("Nothing to undo")

def mass_MOD(payments,start,end,key,value,changes):
        '''
        The mass_MOD function iteratively modifies payment information within a specified range and records a 'mMOD' operation in the changes list to indicate the mass modification.
        args:
        payments(dict):dictionary of all payments
        start,end(int):indexes where apartments are to be modiffied
        key:key to be modified 
        value:new value of the key to be modified 
        changes(list):list where changes are recorded
        returns nothing
        '''
        for nr in range(start,end+1):
                if nr in payments:
                        ADD(payments,nr,{key:value},changes)
        changes.append({'op':'mMOD','nr':end-start+1,'init':'NaN','fin':'NaN'})

def del_under_value(payments,value,changes):
        '''
        The del_under_value function iteratively modifies payment information under a certain value and records a 'mMOD' operation in the changes list to indicate the mass modification.
        args:
        payments(dict):dictionary of all payments
        value: value for comparison
        changes(list):list where changes are recorded
        returns nothing
        '''
        nrc=0
        for nr in payments:
                gas=get_gas_value(nr,payments)
                water=get_water_value(nr,payments)
                heat=get_heat_value(nr,payments)
                sewage=get_sewage_value(nr,payments)
                misc=get_misc_value(nr,payments)
                if(gas<value):
                        ADD(payments,nr,{'gas':0.0},changes)
                        nrc+=1
                if(water<value):
                        ADD(payments,nr,{'water':0.0},changes)
                        nrc+=1
                if(heat<value):
                        ADD(payments,nr,{'heat':0.0},changes)
                        nrc+=1
                if(sewage<value):
                        ADD(payments,nr,{'sewage':0.0},changes)
                        nrc+=1
                if(misc<value):
                        ADD(payments,nr,{'misc':0.0},changes)
                        nrc+=1    
        changes.append({'op':'mMOD','nr':nrc,'init':'NaN','fin':'NaN'})    
