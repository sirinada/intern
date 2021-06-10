from fastapi import FastAPI

app = FastAPI()

@app.get('/ticket')
def main(price:int, unit:int, payment_method:str, protect:int):

    amount = price*unit
    tic_prot = amount*0.07
    fee = 20*unit
    credit_fee = (amount+fee)*0.03
    credit_with_tic_prot = (amount+tic_prot+fee)*0.03

    if payment_method == 'credit':
        if protect == 0:
            total = amount+fee+credit_fee
            return {'Total price':total}
        else:
            total = amount+tic_prot+fee+credit_with_tic_prot
            return {'Total price':total}
    else:
        if protect == 0:
            total = amount+fee
            return {'Total price':total}
        else:
            total = amount+tic_prot+fee
            return {'Total price':total}