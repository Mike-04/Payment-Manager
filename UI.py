import service
import datetime 
import msvcrt

def pak():
        '''
        pak function asks the user to press a key in order to proceed
        args: none
        returns nothing
        '''
        print("Press any key to continue...")
        msvcrt.getch()

def print_ap(nr):
        '''
        print_ap function prints all the payments from an apartment.
        nr(int):number of apartment to retrieve values from
        returns nothing
        '''
        payments=service.retrieve_payments()
        if nr in payments:
                print("Apartment nr",nr,"has the following payments from date",service.get_date_value_str(payments[nr]))
                print("Gas:",service.get_gas_value(payments[nr]))
                print("Water:",service.get_water_value(payments[nr]))
                print("Heat:",service.get_heat_value(payments[nr]))
                print("Sewage:",service.get_sewage_value(payments[nr]))
                print("Misc:",service.get_misc_value(payments[nr]))
        else:
                print("No payments for the apartment nr:",nr)

def print_grt(value):
        '''
        print_grt function prints all the apartments with payments greater than a value.
        value(float):value for comparison
        returns nothing
        '''
        print("Apartments with payments more than:",value,"are:")
        payments=service.retrieve_payments()
        for nr in payments:
                gas=service.get_gas_value(payments[nr])
                water=service.get_water_value(payments[nr])
                heat=service.get_heat_value(payments[nr])
                sewage=service.get_sewage_value(payments[nr])
                misc=service.get_misc_value(payments[nr])
                if gas > value or water > value or heat > value or sewage > value or misc > value:
                       print("Apartment",nr)      

def print_date_value(date,value):
        '''
        print_date_value function prints all the apartments with payments before a certain date and with total over a certain value.
        value(float):value for comparison
        date(date):date for comparison
        returns nothing
        '''
        payments=service.retrieve_payments()
        print("Apartments with payments before",date)
        for nr in payments:
                total=service.get_total_value(payments[nr])
                if total>value and payments[nr]['date']<date:
                        print("Apartment nr:",nr)

def print_all_key(key):
        '''
        print_all_key function displays payment information for a specific key (e.g., 'gas', 'water', 'heat') from all apartments.
        key (str): The payment category to be displayed (e.g., 'gas', 'water', 'heat').
        returns nothing
        '''
        payments=service.retrieve_payments()
        for nr in payments:
                print("Apartment number:",nr,"paid:",payments[nr][key],"for:",key) 

def total_by_key(key):
        '''
        total_by_key function displays total sum for a specific key (e.g., 'gas', 'water', 'heat') for all apartments.
        key (str): The payment category to be displayed (e.g., 'gas', 'water', 'heat').
        returns nothing
        '''
        total=0
        payments=service.retrieve_payments()
        for nr in payments:
                total+=payments[nr][key]
        print("The total for the:",key,"is",total)

def key_selector():
        '''
        The key_selector function prompts the user to select a key (e.g., 'gas', 'water', 'heat', 'sewage', 'misc') and returns the selected key based on the user's input.
        args: none
        returns: selected key as a string based on the user's input.
        '''
        print("Select one of the following:")
        print("Gas:1")
        print("Water:2")
        print("Heat:3")
        print("Sewage:4")
        print("Miscellaneous:5")
        val=read_int("\nValue:")
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
        pak()

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
        read_date function prompts the user to input a date or autocomplete with todays date and handles any input errors.
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

def input_payment():
        '''
        input_payment function allows the user to input payment information and updates the 'payments' dictionary.
        returns nothing
        '''
        nr=read_int("Nr:")
        gas=read_float("Gas:")
        water=read_float("Water:")
        heat=read_float("Heat:")
        sewage=read_float("Sewage:")
        misc=read_float("Misc:")
        date=read_date()
        entry=service.payment_creator(gas,water,heat,sewage,misc,date)
        try:
                service.validate_entry(entry)
                service.add_payment(nr,entry)
        except ValueError as ve:
                print(ve)

def del_app():
        '''
        del_app function passes the command to delete a certain apartment to services
        args:none
        returns nothing
        '''
        nr=read_int("Enter apartment number:")
        service.del_payment(nr)      

def del_app_sf():
        '''
        del_app_sf function passes the command to delete a apartments in range to services
        args:none
        returns nothing
        '''
        start=read_int("Start:")
        end=read_int("End:")
        service.mass_del(start,end)

def del_key_sf():
        '''
        del_key_sf function passes the command to delete a payment type from all apartments to services
        args:none
        returns nothing
        '''
        payments=service.retrieve_payments()
        key=key_selector()
        start=min(payments)
        end=max(payments)
        service.mass_mod(start,end,key,0.0)

def total_app():
        '''
        total_app function prints the total for a certain apartment
        args:none
        returns nothing
        '''
        payments=service.retrieve_payments()
        nr=read_int("Enter apartment number:")
        print("Total for apartment:",nr,"is",service.get_total_value(payments[nr]))

def print_without_key(key):
        '''
        print_without_key function prints all the apartments without one payment type
        key:payment type to be removed 
        returns nothing
        '''
        keys=['gas','water','heat','sewage','misc']
        payments=service.retrieve_payments()
        for nr in payments:
                gas=service.get_gas_value(payments[nr])
                water=service.get_water_value(payments[nr])
                heat=service.get_heat_value(payments[nr])
                sewage=service.get_sewage_value(payments[nr])
                misc=service.get_misc_value(payments[nr])
                rez="Apartment number "+str(nr)
                if(key!=keys[0]):
                        rez+=" gas:"+str(gas)
                if(key!=keys[1]):
                        rez+=" water:"+str(water)
                if(key!=keys[2]):
                        rez+=" heat:"+str(heat)
                if(key!=keys[3]):
                        rez+=" sewage:"+str(sewage)
                if(key!=keys[4]):
                        rez+=" misc:"+str(misc)
                print(rez)

def print_over_value(value):
        '''
        print_over_value function prints all the payment types from all the apartments over a certain value 
        value: value for comparison 
        returns nothing
        '''
        payments=service.retrieve_payments()
        for nr in payments:
                gas=service.get_gas_value(payments[nr])
                water=service.get_water_value(payments[nr])
                heat=service.get_heat_value(payments[nr])
                sewage=service.get_sewage_value(payments[nr])
                misc=service.get_misc_value(payments[nr])
                rez="Apartment number "+str(nr)
                if(value<gas):
                        rez+=" gas:"+str(gas)
                if(value<water):
                        rez+=" water:"+str(water)
                if(value<heat):
                        rez+=" heat:"+str(heat)
                if(value<sewage):
                        rez+=" sewage:"+str(sewage)
                if(value<misc):
                        rez+=" misc:"+str(misc)
                if rez!="Apartment number "+str(nr):
                        print(rez)