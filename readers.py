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
