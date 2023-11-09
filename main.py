import datetime
import random
import pprint

import service
import UI
import testing


def run():
        while(True):
                print("Choices:")
                print("1: Add/Modify")
                print("2: Delete")
                print("3: Search")
                print("4: Reports")
                print("5: Filters")
                print("6: Undo")
                print("7: Exit")
                req=UI.read_int("Make selection:")
                match req:
                        case 1:
                                UI.input_payment()
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
                                                        UI.del_app()
                                                case 2:
                                                        
                                                        start=UI.read_int("Start:")
                                                        end=UI.read_int("End:")
                                                        service.mass_del(start,end)
                                                case 3:
                                                        payments=service.retrieve_payments()
                                                        key=UI.key_selector()
                                                        start=min(payments)
                                                        end=max(payments)
                                                        service.mass_mod(start,end,key,0.0)
                                                case 4:
                                                        break
                                                case _:
                                                        print("Invalid input!")
                        case 3:
                                while(True):
                                        print("Choices:")
                                        print("1: Shows all apartments with utilities over a inputted value")
                                        print("2: Shows a certain utility for all apartments")
                                        print("3: Shows all utilities paid before a inputted date and over a imputed value")
                                        print("4: Exit")
                                        sub_req=UI.read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        val=UI.read_float("Enter the value:")
                                                        UI.print_grt(val)
                                                case 2:
                                                        key=UI.key_selector()
                                                        UI.print_all_key(key)
                                                case 3:
                                                        dt=UI.read_date()
                                                        val=UI.read_float("Input value:")
                                                        UI.print_date_value(dt,val)
                                                case 4:
                                                        break
                                                case _:
                                                        print("Invalid input!")
                        case 4:
                                while(True):
                                        print("Choices:")
                                        print("1: Shows all apartments with utilities over a inputted value")
                                        print("2: Shows a certain utility for all apartments")
                                        print("3: Calculates total payments for an apartment")
                                        print("4: Exit")
                                        sub_req=UI.read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        val=UI.read_float("Enter the value:")
                                                        UI.print_grt(val)
                                                case 2:
                                                        key=UI.key_selector()
                                                        UI.print_all_key(val)
                                                case 3:
                                                        UI.total_app()
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
                                                        UI.print_without_key(key)
                                                case 2:

                                                        val=UI.read_float("Input value:")
                                                        UI.print_under_value(val)
                                                case 3:
                                                        break
                                                case _:
                                                        print("Invalid input!")
                        case 6:
                                service.undo_service()
                        case 7:
                                break
                        case 86:
                                while(True):
                                        payments=service.retrieve_payments()
                                        changes=service.retrieve_changes()
                                        print("DEV MODE-Activated :)")
                                        print("Choices:")
                                        print("1: Add a random apartment to the list")
                                        print("2: Delete an apartment")
                                        print("3: Delete all apartments")
                                        print("4: Undo")
                                        print("5: PPrint all apartments")
                                        print("6: PPrint all changes")
                                        print("7: Clear all")
                                        print("8: Exit")
                                        sub_req=UI.read_int("Make selection:")
                                        match sub_req:
                                                case 1:
                                                        nr=random.randint(1,20)
                                                        entry=service.payment_creator(float(random.randint(1,20)),float(random.randint(1,20)),float(random.randint(1,20)),float(random.randint(1,20)),float(random.randint(1,20)),datetime.date.today())
                                                        service.add_payment(nr,entry)
                                                        payments=service.retrieve_payments()
                                                        pprint.pprint(payments[nr])
                                                case 2:
                                                        nr=UI.read_int("Apartment number:")
                                                        service.del_payment(nr)
                                                case 3:
                                                        start=min(payments)
                                                        end=max(payments)
                                                        service.mass_del(start,end)
                                                case 4:
                                                        service.undo_service()
                                                case 5:
                                                        pprint.pprint(payments)
                                                case 6:
                                                        pprint.pprint(changes)
                                                case 7:
                                                        service.clear(testing.KEY)
                                                case 8:
                                                        print("DEV MODE-Deactivated :)")
                                                        break
                                                case _:
                                                        print("R U rlly a DEV?")
                        case _:
                                print("Invalid input!")

testing.auto_testing()
run()
