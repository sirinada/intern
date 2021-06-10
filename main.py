from fastapi import FastAPI

app = FastAPI()

@app.get('/bmi')
def main(price:int, unit:int, protect:int, payment_method:chr):

    amount = price*unit
    tic_prot = amount*0.07
    fee = 20*unit

    if payment_method == 'credit':
        if protect == 0:
            total = (amount+fee)*0.03
            return {'Total price':total}
        else:
            total = (amount+tic_prot+fee)*0.03
            return {'Total price':total}
    else:
        if protect == 0:
            total = amount+fee
            return {'Total price':total}
        else:
            total = amount+tic_prot+fee
            return {'Total price':total}