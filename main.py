import datetime
import random
import pprint

import service
import UI
import testing
import os

def read_com():
        while(True):
                input_string=input(">>>")
                commands=input_string.split(";") 
                for comms in commands:
                        comms=comms.strip()
                        elem=comms.split()
                        comm=elem[0]
                        args=elem[1:]
                        args.append("")
                        #print(args)
                        match comm:
                                case "add":
                                        try:
                                                UI.input_payment(args[0],args[1],args[2],args[3],args[4],args[5],args[6])
                                        except:
                                                print("Invalid command!")
                                case "del":
                                        match len(args):
                                                case 2:
                                                        try:
                                                                service.del_payment(int(args[0]))
                                                        except:
                                                                print("Invalid command!")
                                                case 3:
                                                        try:
                                                                service.mass_del(int(args[0]),int(args[1]))
                                                        except:
                                                                print("Invalid command!")
                                case "undo":
                                        service.undo_service()
                                case "pprint":
                                        match args[0]:
                                                case "p":
                                                        cpayments=service.retrieve_payments()
                                                        pprint.pprint(cpayments)
                                                case "h":
                                                        chistory=service.retrieve_changes()
                                                        pprint.pprint(chistory)
                                case "delk":
                                        payments=service.retrieve_payments()
                                        if payments:
                                                start=min(payments)
                                                end=max(payments)
                                        if args[0] in {"gas","water","heat","sewage","misc"}:
                                                try:
                                                        service.mass_mod(start,end,args[0],0.0)
                                                except:
                                                        print("Invalid command!")
                                        else:
                                                print("Invalid key")
                                case "addr":
                                        try:
                                                nr=random.randint(1,20)
                                                entry=service.payment_creator(float(random.randint(1,20)),float(random.randint(1,20)),float(random.randint(1,20)),float(random.randint(1,20)),float(random.randint(1,20)),datetime.date.today())
                                                service.add_payment(nr,entry)
                                        except:
                                                print("Invalid command!")
                                case "src":
                                        match args[0]:
                                                case "v":
                                                        try:
                                                                UI.print_grt(float(args[0]))
                                                        except:
                                                                print("Invalid command!")
                                                case "k":
                                                        if args[1] in {"gas","water","heat","sewage","misc"}:
                                                                try:
                                                                        UI.print_all_key(args[1])
                                                                except:
                                                                        print("Invalid command!")
                                                        else:
                                                                print("Invalid key")
                                                case "dv":
                                                        try:
                                                                dt=UI.get_date_fs(args[0])
                                                                UI.print_date_value(dt,float(args[1]))
                                                        except:
                                                                print("Invalid command!")
                                                case _:
                                                        print("Invalid descriptor!")
                                case "flt":
                                        match args[0]:
                                                case "k":
                                                        if args[1] in {"gas","water","heat","sewage","misc"}:
                                                                try:
                                                                        UI.print_without_key(args[1])
                                                                except:
                                                                        print("Invalid command!")
                                                        else:
                                                                print("Invalid key")
                                                case "v":
                                                        UI.print_over_value(float(args[1]))
                                                case _:
                                                        print("Invalid descriptor!")

                                case "exit":
                                        break
                                case "clearc":
                                        os.system("cls")
                                case _:
                                        print("Function error")
                                        print("Command:",comm,"\nArgs:",args)
        

def run():
        os.system("cls")
        read_com()

testing.auto_testing()
run()
