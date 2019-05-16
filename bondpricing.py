""" Get bond price from YTM """
#freq is number of
#periods is number of counting dates
import numpy as np
def bond_price(par, T, ytm, coup, freq=2):
    #freq = float(freq)
    periods = T*freq
    coupon = coup/100.*par/freq
    dt = [(i+1)/freq for i in range(int(periods))]
    print([t*freq for t in dt])
    price = sum([coupon/(1+ytm/freq)**(freq*t) for t in dt]) + \
            par/(1+ytm/freq)**(freq*T)
    return price

"""
def bond_price(par, T, ytm, coup, freq=2):
    freq=float(freq)
    periods=T*freq
    coupon=coup/100.*par/freq
    dt=[(i+1)/freq for i in range(int(periods))]
    rate=ytm/freq
    price = sum([coupon/(1+rate)**(freq*t) for t in dt])+par/(1+rate)**(freq*T)
"""
def bond(par,T,ytm,coup,freq=2):
    numSettlement=T*freq
    coupon=coup/100.*par/freq
    tn=np.arange(1/freq,T+1/freq,1/freq)
    print(tn*freq)
    rate=ytm/freq
    price=sum([coupon/(1+rate)**(t*freq) for t in tn])+par/(1+rate)**(T*freq)
    return price


ytm=0.03
print(bond_price(100, 1.5, ytm, 5.75, 2))
print(bond(100, 1.5, ytm, 5.75, 2))




"""
m = Number of payments per period (e.g., m=2 for semiannually payments)
t = Number of years to maturity
ytm = Yield to maturity (in decimals terms)
fv = The Bond’s Face Value
c = Coupon rate (in decimals terms)

m = 2
t = 9
ytm = 0.08
fv = 1000
c = 0.06


bondPrice = ((fv*c/m*(1-(1+ytm/m)**(-m*t)))/(ytm/m)) + fv*(1+(ytm/m))**(-m*t)

print (bondPrice)
"""
