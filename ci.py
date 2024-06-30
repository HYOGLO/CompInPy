# Compound Interest in Python

type = input("Type balance OR interest: ")

if type == "balance":
    p = float(input("Give principle (starting amount): "))
    r1 = float(input("Give interest rate without % sign: "))
    t = float(input("Give time in years: "))
    r = r1/100
    total = (p*(1+r)**t)
    
elif type == "interest":
    p = float(input("Give principle (starting amount): "))
    r1 = float(input("Give interest rate without % sign: "))
    t = float(input("Give time in years: "))
    r = r1/100
    total = (p*(1+r)**t)
print(total)
