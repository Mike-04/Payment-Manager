
import random
import pprint
import datetime

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
                       
'''Getters'''
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
        nr(int):number of apartment to retrive values from\
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

'''Readers'''
def key_selector():
        '''
        The key_selector function prompts the user to select a key (e.g., 'gas', 'water', 'heat', 'sewage', 'misc') and returns the selected key based on the user's input.
        args: none
        returns: selected key as a string based on the user's input.
        '''
        print("select one of the following:")
        print("Gas:1")
        print("Water:2")
        print("Heat:3")
        print("Sewage:4")
        print("Miscellaneous:5")
        val=read_int("Value:")
        match val:
                case 1:
                      return 'gas'
                case 2:
                      return 'water'
                case 3:
                      return 'heat'
                case 4:
                      return 'sewage'
                case 5:
                      return 'misc'

def read_float(msg:str):
        '''
        read_float function prompts the user to input a float value and handles any input errors.
        msg(str): The message to display as a prompt to the user.
        returns:float value entered by the user.
        '''
        while True:
                try :
                        return float(input(msg))
                except ValueError:
                        print("Invalid value")
            
def read_int(msg:str):
        '''
        read_int function prompts the user to input a int value and handles any input errors.
        msg(str): The message to display as a prompt to the user.
        returns:int value entered by the user.
        '''
        while True:
                try :
                        return int(input(msg))
                except ValueError:
                        print("Invalid value")

def read_date():
        '''
        read_date function prompts the user to input a date or autocompletes with todays date and handles any input errors.
        args:none
        returns:date entered by the user.
        '''
        while True:
                str=input("Input date in dd/mm/yyyy or leave blank for todays date:")
                if(str != ""):
                        dt=str.split('/')
                        try:
                                dt=datetime.date(int(dt[2]),int(dt[1]),int(dt[0]))
                                break
                        except:
                               print("Invalid date")
                else:
                        dt=datetime.date.today()
                        break
        return dt

def input_payment(payments:dict,changes:list):
        '''
        input_payment function allows the user to input payment information and updates the 'payments' dictionary.
        payments(dict):dictionary of all payments
        changes(list):list where changes are recorded
        returns nothing
        '''
        nr=read_int("Nr:")
        gas=read_float("Gas:")
        water=read_float("Water:")
        heat=read_float("Heat:")
        sewage=read_float("Sewage:")
        misc=read_float("Misc:")
        date=read_date()
        ADD(payments,nr,{'gas': gas,'water':water,'heat':heat,'sewage':sewage,'misc':misc,'date':date},changes)        

'''Printers'''
def print_ap(payments,nr):
        '''
        print_ap function prints all the payments from an apartment.
        payments(dict):dictionary of all payments
        nr(int):number of apartment to retrive values from
        returns nothing
        '''
        if nr in payments:
                print("Apartment nr",nr,"has the following payments from date",get_date_value_str(nr,payments))
                print("Gas:",get_gas_value(nr,payments))
                print("Water:",get_water_value(nr,payments))
                print("Heat:",get_heat_value(nr,payments))
                print("Sewage:",get_sewage_value(nr,payments))
                print("Misc:",get_misc_value(nr,payments))
        else:
                print("No payments for the apartment nr:",nr)

def print_grt(payments,value):
        '''
        print_grt function prints all the apartments with payments greater than a value.
        payments(dict):dictionary of all payments
        value(float):value for comparison
        returns nothing
        '''
        print("Apartments with payments more than:",value,"are:")
        for nr in payments:
                gas=get_gas_value(nr,payments)
                water=get_water_value(nr,payments)
                heat=get_heat_value(nr,payments)
                sewage=get_sewage_value(nr,payments)
                misc=get_misc_value(nr,payments)
                if gas > value or water > value or heat > value or sewage > value or misc > value:
                       print("Apartment",nr)      

def print_all_key(payments,key):
        '''
        print_all_key function displays payment information for a specific key (e.g., 'gas', 'water', 'heat') from all apartments.
        payments (dict): A dictionary containing payment information for multiple apartments.
        key (str): The payment category to be displayed (e.g., 'gas', 'water', 'heat').
        returns nothing
        '''
        for nr in payments:
                print("Apartment number:",nr,"paid:",payments[nr][key],"for:",key) 

def total_by_key(payments,key):
        '''
        total_by_key function displays total sum for a specific key (e.g., 'gas', 'water', 'heat') for all apartments.
        payments (dict): A dictionary containing payment information for multiple apartments.
        key (str): The payment category to be displayed (e.g., 'gas', 'water', 'heat').
        returns nothing
        '''
        total=0
        for nr in payments:
                total+=payments[nr][key]
        print("The total for the:",key,"is",total)

def run():
        changes=[]
        payments={}
        while(True):
                #pprint.pprint(changes)
                print("Choices:")
                print("1: Add/Modify")
                print("2: Delete")
                print("3: Search")
                print("4: Raports")
                print("5: Filters")
                print("6: Undo")
                print("7: Exit")
                req=read_int("Make selection:")
                match req:
                        case 1:
                                input_payment(payments,changes)
                        case 2:
                                while(True):
                                        print("Choices:")
                                        print("1: Delete entries for an apartment")
                                        print("2: Delete entries in range")
                                        print("3: Delete all payments for a certain utility")
                                        print("4: Exit")
                                        sub_req=read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        nr=read_int("Enter apartment number:")
                                                        DEL(payments,nr,changes)
                                                case 2:
                                                        start=read_int("Start:")
                                                        end=read_int("End:")
                                                        mass_DEL(payments,start,end,changes)
                                                case 3:
                                                        key=key_selector()
                                                        start=min(payments)
                                                        end=max(payments)
                                                        mass_MOD(payments,start,end,key,0.0,changes)
                                                case 4:
                                                        break
                                                case _:
                                                        print("Invalid input!")
                        case 3:
                                while(True):
                                        print("Choices:")
                                        print("1: Shows all apartments with utilities over a inputed value")
                                        print("2: Shows a certain uitilty for all apartaments")
                                        print("3: Shows all utilies paid before a inputed date and over a inputed value")
                                        print("4: Exit")
                                        sub_req=read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        val=read_float("Enter the value:")
                                                        print_grt(payments,val)
                                                case 2:
                                                        key=key_selector()
                                                        print_all_key(payments,key)
                                                case 3:
                                                        pass
                                                case 4:
                                                        break
                                                case _:
                                                        print("Invalid input!")
                        case 4:
                                while(True):
                                        print("Choices:")
                                        print("1: Shows all apartments with utilities over a inputed value")
                                        print("2: Shows a certain uitilty for all apartaments")
                                        print("3: Calculates total payments for an apartment")
                                        print("4: Exit")
                                        sub_req=read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        val=read_float("Enter the value:")
                                                        print_grt(payments,val)
                                                case 2:
                                                        key=key_selector()
                                                        print_all_key(payments,val)
                                                case 3:
                                                        nr=read_int("Enter apartment number:")
                                                        print("Total for apartment:",nr,"is",get_total_value(nr,payments))
                                                case 4:
                                                        break
                                                case _:
                                                        print("Invalid input!")
                        case 5:
                                while(True):
                                        print("Choices:")
                                        print("1: Delete all payments for a certain utility")
                                        print("2: Delete all payments under a certain value")
                                        print("3: Exit")
                                        sub_req=read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        key=key_selector()
                                                        start=min(payments)
                                                        end=max(payments)
                                                        mass_MOD(payments,start,end,key,0.0,changes)
                                                case 2:
                                                        pass
                                                case 3:
                                                        break
                                                case _:
                                                        print("Invalid input!")
                        case 6:
                                UNDO(payments,changes)
                        case 7:
                                break
                        case 86:
                                while(True):
                                        print("DEV MODE-Activated :)")
                                        print("Choices:")
                                        print("1: Add a random apartment to the list")
                                        print("2: Delete an apartment")
                                        print("3: Delete all apartments")
                                        print("4: Undo")
                                        print("5: PPrint all apartments")
                                        print("6: PPrint all changes")
                                        print("7: Exit")
                                        sub_req=read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        nr=random.randint(1,20)
                                                        ADD(payments,nr,{'gas': float(random.randint(1,20)),'water':float(random.randint(1,20)),'heat':float(random.randint(1,20)),'sewage':float(random.randint(1,20)),'misc':float(random.randint(1,20)),'date':datetime.date.today()},changes)
                                                        pprint.pprint(payments[nr])
                                                case 2:
                                                        nr=read_int("Apartment number:")
                                                        DEL(payments,nr,changes)
                                                case 3:
                                                        start=min(payments)
                                                        end=max(payments)
                                                        mass_DEL(payments,start,end,changes)
                                                case 4:
                                                        UNDO(payments,changes)
                                                case 5:
                                                        pprint.pprint(payments)
                                                case 6:
                                                        pprint.pprint(changes)
                                                case 7:
                                                        print("DEV MODE-Deactivated :)")
                                                        break
                                                case _:
                                                        print("R U rlly a DEV?")
                        case _:
                                print("Invalid input!")

run()
