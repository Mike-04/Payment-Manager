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
