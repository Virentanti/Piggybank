import pickle


def add(money):
        money=int(money)
        balance_sheet=open('balance_sheet.dat','rb+')
        bal_ob=pickle.load(balance_sheet)
        bal_ob.append(money)
        balance_sheet.seek(0)
        pickle.dump(bal_ob,balance_sheet)
        return True



def savings():
    try:
        balance_sheet=open('balance_sheet.dat','rb')
        balance_sheet.seek(0)
        bal_ob=pickle.load(balance_sheet)
        try:
            sum=0
            for i in bal_ob:
                sum+=int(i)
            return str(sum)
        except:
            return str(0)
    except EOFError:
        return str(0)

def clear():
    balance_sheet=open('balance_sheet.dat','wb')
    pickle.dump([],balance_sheet)
    return True
