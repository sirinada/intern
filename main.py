from fastapi import FastAPI

app = FastAPI()

@app.get('/ticket')
def main(price:int, unit:int, payment_method:str, ticket_protect:str):

    amount = price*unit
    tic_prot = amount*0.07
    fee = 20*unit
    credit_fee = (amount+fee)*0.03
    credit_with_tic_prot = (amount+tic_prot+fee)*0.03

    if payment_method == 'credit':
        if ticket_protect == 'no':
            total = amount+fee+credit_fee
            return {'Total price':total}
        elif ticket_protect == 'yes':
            total = amount+tic_prot+fee+credit_with_tic_prot
            return {'Total price':total}
        else:
            print('error')

    elif payment_method == 'cash' or payment_method == 'atm':
        if ticket_protect == 'no':
            total = amount+fee
            return {'Total price':total}
        elif ticket_protect == 'yes':
            total = amount+tic_prot+fee
            return {'Total price':total}
        else:
            print('error')
    
    else:
        print('error')