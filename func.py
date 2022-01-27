import datetime
import pickle


def add(money):
    try:
        balance_sheet=open('balance_sheet.dat','ab')
        bal_ob=pickle.load(balance_sheet)
        bal_ob[datetime.datetime.now()]=money
        balance_sheet.seek(0)
        pickle.dump(bal_ob,balance_sheet)
        return True
    except:
        return False


def savings():
    try:
        balance_sheet=open('balance_sheet.dat','rb')
        balance_sheet.seek(0)
        bal_ob=pickle.load(balance_sheet)
        try:
            sum=0
            for i in bal_ob:
                sum+=bal_ob[i]
            return str(sum)
        except:
            return str(0)
    except EOFError:
        return str(0)