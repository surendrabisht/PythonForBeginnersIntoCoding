def EvaluateProfitOrLoss(B, A):
    profit= A-B
    loss = B-A
    if profit>0:
        print(" profit  is ",profit)
    elif loss>0:
        print(" loss is ",loss)
    else:
        print(" No profit no loss.")

def EvaluateProfitOrLossPercent(B, A):
    profit= A-B
    loss = B-A
    profitPercent= profit *100 /B
    lossPercent= loss *100 /B
    if profit>0:
        print(" profit % is ",profitPercent)
    elif loss>0:
        print(" loss % is ",lossPercent)
    else:
        print(" No profit no loss.")


sp=int(input("enter your Selling price "))
cp=int(input("enter your COST Price"))
EvaluateProfitOrLoss(cp,sp)
EvaluateProfitOrLossPercent(cp,sp)









