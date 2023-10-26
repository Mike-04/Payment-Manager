
import random
import pprint
import datetime

'''Operations'''
def ADD(payments:dict,nr:int,val:dict,changes:list):
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
        if nr in payments:
                op='DEL'
                init=payments[nr].copy()
                changes.append({'op':op,'nr':nr,'init':init,'fin':'NaN'}) 
                del(payments[nr])

def mass_DEL(payments,start,end,changes):
        for nr in range (start, end+1):
              DEL(payments,nr,changes)
        changes.append({'op':'mDEL','nr':end-start+1,'init':'NaN','fin':'NaN'}) 

def mass_UNDO(payments,changes,rec):
       for i in range(0,rec):
              UNDO(payments,changes)

def inDEL(payments:dict,nr:int):
        if nr in payments:
                del(payments[nr])

def inADD(payments:dict,nr:int,val:dict):
        if nr not in payments:
                payments[nr]=val
        else:
                payments[nr].update(val)

def UNDO(payments:dict,changes:list):
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
        for nr in range(start,end+1):
                if nr in payments:
                        ADD(payments,nr,{key:value},changes)
        changes.append({'op':'mMOD','nr':end-start+1,'init':'NaN','fin':'NaN'})
                       
'''Getters'''
def get_gas_value(nr,payments):
        if nr in payments:
              return float(payments[nr]['gas'])
                     
def get_water_value(nr,payments):
        if nr in payments:
              return float(payments[nr]['water'])
             
def get_heat_value(nr,payments):
        if nr in payments:
              return float(payments[nr]['heat'])
                
def get_sewage_value(nr,payments):
        if nr in payments:
              return float(payments[nr]['sewage'])
                
def get_misc_value(nr,payments):
        if nr in payments:
              return float(payments[nr]['misc'])

def get_date_value_str(nr,payments):
        if nr in payments:
                return payments[nr]['date'].strftime("%x")
                
def get_total_value(nr,payments):
        total=0
        total+=get_gas_value(nr,payments)
        total+=get_water_value(nr,payments)
        total+=get_heat_value(nr,payments)
        total+=get_sewage_value(nr,payments)
        total+=get_misc_value(nr,payments)
        return total

'''Readers'''
def key_selector():
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
    while True:
        try :
            return float(input(msg))
        except ValueError:
            print("Invalid value")
            
def read_int(msg:str):
    while True:
        try :
            return int(input(msg))
        except ValueError:
            print("Invalid value")

def read_date():
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
        for nr in payments:
                print("Apartment number:",nr,"paid:",payments[nr][key],"for:",key) 

def total_by_key(payments,key):
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
                                        print("DEV MODE!")
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
                                                        break
                                                case _:
                                                        print("R U rlly a DEV?")
                        case _:
                                print("Invalid input!")

run()
