
import random
import pprint
import datetime

import service
import UI
import testing
#importing bussines only for dev options
import bussines

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
                req=UI.read_int("Make selection:")
                match req:
                        case 1:
                                UI.input_payment(payments,changes)
                        case 2:
                                while(True):
                                        print("Choices:")
                                        print("1: Delete entries for an apartment")
                                        print("2: Delete entries in range")
                                        print("3: Delete all payments for a certain utility")
                                        print("4: Exit")
                                        sub_req=UI.read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        UI.del_app(payments,changes)
                                                case 2:
                                                        start=UI.read_int("Start:")
                                                        end=UI.read_int("End:")
                                                        service.mass_del(payments,start,end,changes)
                                                case 3:
                                                        key=UI.key_selector()
                                                        start=min(payments)
                                                        end=max(payments)
                                                        service.mass_mod(payments,start,end,key,0.0,changes)
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
                                        sub_req=UI.read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        val=UI.read_float("Enter the value:")
                                                        UI.print_grt(payments,val)
                                                case 2:
                                                        key=UI.key_selector()
                                                        UI.print_all_key(payments,key)
                                                case 3:
                                                        dt=UI.read_date()
                                                        val=UI.read_float("Input value:")
                                                        UI.print_date_value(payments,dt,val)
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
                                        sub_req=UI.read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        val=UI.read_float("Enter the value:")
                                                        UI.print_grt(payments,val)
                                                case 2:
                                                        key=UI.key_selector()
                                                        UI.print_all_key(payments,val)
                                                case 3:
                                                        UI.total_app(payments)
                                                case 4:
                                                        break
                                                case _:
                                                        print("Invalid input!")
                        case 5:
                                while(True):
                                        print("Choices:")
                                        print("1: Eliminates all payments for a certain utility")
                                        print("2: Eliminates all payments under a certain value")
                                        print("3: Exit")
                                        sub_req=UI.read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        key=UI.key_selector()
                                                        UI.print_without_key(payments,key)
                                                case 2:

                                                        val=UI.read_float("Input value:")
                                                        UI.print_under_value(payments,val)
                                                case 3:
                                                        break
                                                case _:
                                                        print("Invalid input!")
                        case 6:
                                service.undo_service(payments,changes)
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
                                        sub_req=UI.read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        nr=random.randint(1,20)
                                                        entry=service.payment_creator(float(random.randint(1,20)),float(random.randint(1,20)),float(random.randint(1,20)),float(random.randint(1,20)),float(random.randint(1,20)),datetime.date.today())
                                                        bussines.ADD(payments,nr,entry,changes)
                                                        pprint.pprint(payments[nr])
                                                case 2:
                                                        nr=UI.read_int("Apartment number:")
                                                        bussines.DEL(payments,nr,changes)
                                                case 3:
                                                        start=min(payments)
                                                        end=max(payments)
                                                        service.mass_del(payments,start,end,changes)
                                                case 4:
                                                        service.undo_service(payments,changes)
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

testing.auto_testing()
run()
