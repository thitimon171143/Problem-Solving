def read() :
    global principal
    global interest
    global years
    global time
    print('-----Input-----')
    principal = int(input('Principal : '))
    interest = float(input('Interest : '))
    years = int(input('Number of Years : '))
    time = int(input('Compound Interval : '))
    print('---------------')

def calc() :
    global amount
    amount = principal*(1+(interest/time))**(years*time)

def printt() :
    print('-----Result-----')
    print('Principal :',principal)
    print('Interest :',interest)
    print('Number of Years :',years)
    print('Compound Interval :',time)
    print('Amount :',amount)
    print('----------------')

read()
calc()
printt()