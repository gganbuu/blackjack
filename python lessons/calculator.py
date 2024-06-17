def check_q(number):
    if number == 'q':
        print('Exiting Program')
        return True

number_1 = 0
number_2 = 0
symbol = ''
while True:
    number_1 = input("number 1: ")
    if check_q(number_1):
        break
    number_2 = input("number 2: ")
    if check_q(number_2):
        break
    symbol = input("What mathematical equation would you like? (*,/,+,-)")
    if check_q(symbol):
        break

    if symbol == '*':
        answer = float(number_1) * float(number_2)
    elif symbol == '+':
        answer = float(number_1) + float(number_2)
    elif symbol == '-':
        answer = float(number_2) - float(number_2)
    elif symbol == '/':
        answer = float(number_1) / float(number_2)
    
    try:
        print(f"{number_1} {symbol} {number_2} = {answer}")
    except:
        print("Error")

