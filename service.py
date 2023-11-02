def get_gas_value(nr,payments):
        '''
        The get_gas_value function retrieves the gas value for a specific payment record number from the payments dictionary.
        payments(dict):dictionary of all payments
        nr(int):number of apartment to retrive values from
        returns:value requested
        '''
        if nr in payments:
              return float(payments[nr]['gas'])
                     
def get_water_value(nr,payments):
        '''
        The get_gas_value function retrieves the water value for a specific payment record number from the payments dictionary.
        payments(dict):dictionary of all payments
        nr(int):number of apartment to retrive values from
        returns:value requested
        '''
        if nr in payments:
              return float(payments[nr]['water'])
             
def get_heat_value(nr,payments):
        '''
        The get_gas_value function retrieves the heat value for a specific payment record number from the payments dictionary.
        payments(dict):dictionary of all payments
        nr(int):number of apartment to retrive values from
        returns:value requested
        '''
        if nr in payments:
              return float(payments[nr]['heat'])
                
def get_sewage_value(nr,payments):
        '''
        The get_gas_value function retrieves the sewage value for a specific payment record number from the payments dictionary.
        payments(dict):dictionary of all payments
        nr(int):number of apartment to retrive values from
        returns:value requested
        '''
        if nr in payments:
              return float(payments[nr]['sewage'])
                
def get_misc_value(nr,payments):
        '''
        The get_gas_value function retrieves the misc value for a specific payment record number from the payments dictionary.
        payments(dict):dictionary of all payments
        nr(int):number of apartment to retrive values from
        returns:value requested
        '''
        if nr in payments:
              return float(payments[nr]['misc'])

def get_date_value_str(nr,payments):
        '''
        The get_gas_value function retrieves the date value as string for a specific payment record number from the payments dictionary.
        payments(dict):dictionary of all payments
        nr(int):number of apartment to retrive values from
        returns:value requested
        '''
        if nr in payments:
                return payments[nr]['date'].strftime("%x")
                
def get_total_value(nr,payments):
        '''
        The get_gas_value function calculates the total for a specific payment record number from the payments dictionary.
        payments(dict):dictionary of all payments
        nr(int):number of apartment to retrive values from
        returns: total
        '''
        total=0
        total+=get_gas_value(nr,payments)
        total+=get_water_value(nr,payments)
        total+=get_heat_value(nr,payments)
        total+=get_sewage_value(nr,payments)
        total+=get_misc_value(nr,payments)
        return total

def validate_entry(entry):
        if entry['gas']<0 or entry['water']<0 or entry['heat']<0 or entry['sewage']<0 or entry['misc']<0:
                raise ValueError("Value can't be smaller than 0")



def payment_creator(gas,water,heat,sewage,misc,date):
        entry={'gas': gas,'water':water,'heat':heat,'sewage':sewage,'misc':misc,'date':date}
        return entry


def mass_mod(payments,start,end,key,value,changes):
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

def mass_del(payments,start,end,changes):
        '''
        The `mass_DEL` function deletes payments between the indexes start and end records the type of operation.
        args:
        payments(dict):dictionary of all payments
        start,end(int):indexes where apartments are to be deleted
        changes(list):list where changes are recorded
        returns nothing
        '''
        chg=0
        for nr in range (start, end+1):
                try:
                        DEL(payments,nr,changes)
                        chg+=1
                except:
                        pass
        changes.append({'op':'mDEL','nr':chg,'init':'NaN','fin':'NaN'}) 

def mass_undo(payments,changes,rec):
        '''
        The mass_UNDO function iteratively undoes changes in a payment dictionary based on a specified number of records (rec).
        payments(dict):dictionary of all payments
        rec(int):number of undos to be made
        changes(list):list where changes are recorded
        returns nothing
        '''
        for i in range(0,rec):
              UNDO(payments,changes)
  
