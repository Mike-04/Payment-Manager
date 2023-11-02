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

def print_date_value(payments,date,value):
        print("Apartments with payments before",date)
        for nr in payments:
                total=get_total_value(nr,payments)
                if total>value and payments[nr]['date']<date:
                        print("Apartment nr:",nr)

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
        entry=payment_creator(gas,water,heat,sewage,misc,date)
        try:
                validate_entry(entry)
                ADD(payments,nr,entry,changes)
        except ValueError as ve:
                print(ve)
        
