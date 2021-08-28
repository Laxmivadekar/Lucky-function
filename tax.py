GS=int(input('enter the gross salary'))
TS=int(input('enter the total salary'))  
def taxcalculator():
    remaining_savings=GS-TS
    if remaining_savings<100000:
        print(0,'zero tax')
    if remaining_savings<200000:
        print(remaining_savings*0.1,'this tax for 100000 to 20000')
    if remaining_savings<500000:
        print(remaining_savings*0.1+remaining_savings*0.2)
    if remaining_savings>500000:
        print(remaining_savings*0.1+remaining_savings*0.2+remaining_savings*0.5)
taxcalculator()