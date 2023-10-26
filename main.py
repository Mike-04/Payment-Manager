
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
              return payments[nr]['gas']
                     
def get_water_value(nr,payments):
        if nr in payments:
              return payments[nr]['water']
             
def get_heat_value(nr,payments):
        if nr in payments:
              return payments[nr]['heat']
                
def get_sewage_value(nr,payments):
        if nr in payments:
              return payments[nr]['sewage']
                
def get_misc_value(nr,payments):
        if nr in payments:
              return payments[nr]['misc']

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

def run():
        changes=[]
        payments={}
        while(True):
                #pprint.pprint(changes)
                print("Choices:")
                print("1: Adds or modifies an entry")
                print("2: Deletes an entry")
                print("3: Undo")
                print("4: Prints list")
                print("5: Exits the program")
                req=int(input("Make a selection: "))
                match req:
                        case 1:
                                input_payment(payments,changes)
                        case 2:
                                start=int(input("Start:"))
                                end=int(input("End:"))
                                key=input("Key:")
                                value=read_float("Value")
                                mass_MOD(payments,start,end,key,value,changes)
                        case 3:
                                UNDO(payments,changes)
                        case 4:
                                pprint.pprint(changes)
                                print("----------------------------------")
                                pprint.pprint(payments)
                                print("----------------------------------")
                        case 5:
                                break
                        case _:
                                print("Invalid input!")

run()
