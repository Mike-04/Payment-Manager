import random
import datetime
import service
import bussines
def auto_testing():
        keys=['gas','water','heat','sewage','misc']
        sb_changes=[]
        sb_payments={}
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
                        bussines.ADD(sb_payments,nr,test,sb_changes)
                        assert(sb_payments[nr]==test)
                sb_payments_c=sb_payments
                service.mass_mod(sb_payments,min(sb_payments),max(sb_payments), random.choice(keys), float(random.randint(0,100)), sb_changes)
                bussines.UNDO(sb_payments,sb_changes)
                assert(sb_payments==sb_payments_c)
                service.mass_del(sb_payments,min(sb_payments),max(sb_payments),sb_changes)
                assert(sb_payments=={})
                bussines.UNDO(sb_payments,sb_changes)
                assert(sb_payments==sb_payments_c)

