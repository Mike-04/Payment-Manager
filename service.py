import business
import testing

payments={}
changes=[]

def clear(KEY):
        '''
        clear function removes every apartment and every changes in history
        KEY: generated verification key for safety purposes
        returns:nothing
        '''
        if testing.check_key(KEY):
                payments.clear()
                changes.clear()
        else:
                print("Invalid key!")

def retrieve_payments():
        '''
        retrieve_payments function returns a copy of all the payments
        args: none
        returns: c_payments:dict (a copy of the payment dictionary)
        '''
        c_payments=payments.copy()
        return c_payments

def retrieve_changes():
        '''
        retrieve_payments function returns a copy history
        args: none
        returns: c_payments:list (a copy of the history list)
        '''
        c_changes=changes.copy()
        return c_changes      

def get_date_value(entry):
        '''
        The get_gas_value function retrieves the gas value for a specific payment record number from the payments dictionary.
        entry:dict an apartment entity
        returns:value requested
        '''
        if entry:
              return entry['date']

def get_gas_value(entry):
        '''
        The get_gas_value function retrieves the gas value for a specific payment record number from the payments dictionary.
        entry:dict an apartment entity
        returns:value requested
        '''
        if entry:
              return float(entry['gas'])
                     
def get_water_value(entry):
        '''
        The get_gas_value function retrieves the water value for a specific payment record number from the payments dictionary.
        entry:dict an apartment entity
        returns:value requested
        '''
        if entry:
              return float(entry['water'])
             
def get_heat_value(entry):
        '''
        The get_gas_value function retrieves the heat value for a specific payment record number from the payments dictionary.
        entry:dict an apartment entity
        returns:value requested
        '''
        if entry:
              return float(entry['heat'])
                
def get_sewage_value(entry):
        '''
        The get_gas_value function retrieves the sewage value for a specific payment record number from the payments dictionary.
        entry:dict an apartment entity
        returns:value requested
        '''
        if entry:
              return float(entry['sewage'])
                
def get_misc_value(entry):
        '''
        The get_gas_value function retrieves the misc value for a specific payment record number from the payments dictionary.
        entry:dict an apartment entity
        returns:value requested
        '''
        if entry:
              return float(entry['misc'])

def get_date_value_str(entry):
        '''
        The get_gas_value function retrieves the date value as string for a specific payment record number from the payments dictionary.
        entry:dict an apartment entity
        returns:value requested
        '''
        if entry:
                return entry['date'].strftime("%x")
                
def get_total_value(entry):
        '''
        The get_gas_value function calculates the total for a specific payment record number from the payments dictionary.
        entry:dict an apartment entity
        returns: total
        '''
        total=0
        total+=get_gas_value(entry)
        total+=get_water_value(entry)
        total+=get_heat_value(entry)
        total+=get_sewage_value(entry)
        total+=get_misc_value(entry)
        return total

def validate_entry(entry):
        '''
        validate_entry function checks for unacceptable value inputted by the user
        entry:dict an apartment entity
        returns: nothing
        raises error if wrong input
        '''
        if entry['gas']<0 or entry['water']<0 or entry['heat']<0 or entry['sewage']<0 or entry['misc']<0:
                raise ValueError("Value can't be smaller than 0")



def payment_creator(gas,water,heat,sewage,misc,date):
        '''
        payment_creator function generates an apartment entity
        gas:gas value
        water:water value
        heat:heat value
        sewage:sewage value
        misc:misc value
        date:date value
        returns: apartment entity
        '''
        entry={'gas': gas,'water':water,'heat':heat,'sewage':sewage,'misc':misc,'date':date}
        return entry


def mass_mod(start,end,key,value):
        '''
        The mass_MOD function iteratively modifies payment information within a specified range and records a 'mMOD' operation in the changes list to indicate the mass modification.
        args:
        start,end(int):indexes where apartments are to be modified
        key:key to be modified 
        value:new value of the key to be modified 
        returns nothing
        '''
        nrc=0
        ok=0
        for nr in range(start,end+1):
                if nr in payments:
                        gas=get_gas_value(payments[nr])
                        water=get_water_value(payments[nr])
                        heat=get_heat_value(payments[nr])
                        sewage=get_sewage_value(payments[nr])
                        misc=get_misc_value(payments[nr])
                        date=get_date_value(payments[nr])
                        if(key=='gas'):
                                ok=1
                                gas=value
                        if(key=='water'):
                                ok=1
                                water=value
                        if(key=='heat'):
                                ok=1
                                heat=value
                        if(key=='sewage'):
                                ok=1
                                sewage=value
                        if(key=='misc'):
                                ok=1
                                misc=value
                        if ok==1:
                                entry=payment_creator(gas,water,heat,sewage,misc,date)
                                business.ADD(payments,nr,entry,changes)
                                nrc+=1
        changes.append({'op':'mMOD','nr':nrc,'init':'NaN','fin':'NaN'})

def del_under_value(value):
        '''
        The del_under_value function iteratively modifies payment information under a certain value and records a 'mMOD' operation in the changes list to indicate the mass modification.
        args:
        value: value for comparison
        returns nothing
        '''
        ok=0
        nrc=0
        for nr in payments:
                gas=get_gas_value(payments[nr])
                water=get_water_value(payments[nr])
                heat=get_heat_value(payments[nr])
                sewage=get_sewage_value(payments[nr])
                misc=get_misc_value(payments[nr])
                date=get_date_value(payments[nr])
                if(gas<value):
                        ok=1
                        gas=0.0
                if(water<value):
                        ok=1
                        water=0.0
                if(heat<value):
                        ok=1
                        heat=0.0
                if(sewage<value):
                        ok=1
                        sewage=0.0
                if(misc<value):
                        ok=1
                        misc=0.0
                if ok==1:
                        entry=payment_creator(gas,water,heat,sewage,misc,date)
                        business.ADD(payments,nr,entry,changes)
                        nrc+=1    
        changes.append({'op':'mMOD','nr':nrc,'init':'NaN','fin':'NaN'})  

def mass_del(start,end):
        '''
        The `mass_DEL` function deletes payments between the indexes start and end records the type of operation.
        args:
        start,end(int):indexes where apartments are to be deleted
        returns nothing
        '''
        chg=0
        for nr in range (start, end+1):
                try:
                        business.DEL(payments,nr,changes)
                        chg+=1
                except:
                        pass
        changes.append({'op':'mDEL','nr':chg,'init':'NaN','fin':'NaN'}) 

def mass_undo(rec):
        '''
        The mass_UNDO function iteratively undoes changes in a payment dictionary based on a specified number of records (rec).
        rec(int):number of undo operations to be made
        returns nothing
        '''
        for i in range(0,rec):
              business.UNDO(payments,changes)

def add_payment(nr,entry):
        '''
        add_payment function send an apartment entity and a number to be added into the payments or modified
        nr: number where the apartment should be added or modifies
        entry: apartment entity
        returns nothing
        '''
        business.ADD(payments,nr,entry,changes)

def del_payment(nr):
        '''
        del_payment function send an apartment number to be deleted from payments or excepts index error if number is not existent
        nr: number of the apartment that should be deleted
        returns nothing
        '''
        try:
                business.DEL(payments,nr,changes)
        except IndexError as error:
                print(error)
                

  
def undo_service():
        '''
        undo_service function requires an undo of the last operation made
        args: none
        returns nothing
        '''
        business.UNDO(payments,changes)

