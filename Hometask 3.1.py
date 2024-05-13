#Програма має виконувати прості математичні дії (+, -, *, /). Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії, обчислює та друкує результат.
#Зробити перевірку на те, що при діленні дільник не дорівнює 0!
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
operation=(input("Enter operation (+, -, *, /):  "))
if operation=="+":
    print(number1+number2)
elif operation=="-":
    print(number1-number2)
elif operation=="*":
    print(number1*number2)
elif operation=="/":
    if number2 !=0:
        print(number1/number2)
    else:
        print ("Mistake, division by zero")
else:
    print("Invalid operation")
