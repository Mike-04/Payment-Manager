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
