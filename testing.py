import random
import datetime
import service
import business
KEY=random.randint(1000,9999)

def check_key(sKEY):
        if sKEY!=KEY:
                return 0
        return 1

def auto_testing():
        keys=['gas','water','heat','sewage','misc']
        for tests in range(1,100):
                for it in range(1,100):
                        nr=random.randint(0,100)
                        gas=float(random.randint(0,100))
                        water=float(random.randint(0,100))
                        heat=float(random.randint(0,100))
                        sewage=float(random.randint(0,100))
                        misc=float(random.randint(0,100))
                        date=datetime.date.today()
                        test={'gas': gas,'water':water,'heat':heat,'sewage':sewage,'misc':misc,'date':date}
                        service.add_payment(nr,test)
                        sb_payments=service.retrieve_payments()
                        assert(sb_payments[nr]==test)
                sb_payments_c=sb_payments
                service.mass_mod(min(sb_payments),max(sb_payments), random.choice(keys), float(random.randint(0,100)))
                service.undo_service()
                sb_payments=service.retrieve_payments()
                assert(sb_payments==sb_payments_c)
                service.mass_del(min(sb_payments),max(sb_payments))
                sb_payments=service.retrieve_payments()
                assert(sb_payments=={})
                service.undo_service()
                sb_payments=service.retrieve_payments()
                assert(sb_payments==sb_payments_c)
                gas=float(random.randint(-100,100))
                water=float(random.randint(-100,100))
                heat=float(random.randint(-100,100))
                sewage=float(random.randint(-100,100))
                misc=float(random.randint(-100,100))
                date=datetime.date.today()
                entry=service.payment_creator(gas,water,heat,sewage,misc,date)
                try:
                        service.validate_entry(entry)
                        if(gas<0 or water<0 or heat<0 or sewage<0 or misc<0):
                                assert(False)
                except:
                        assert(True)
        service.clear(KEY)

