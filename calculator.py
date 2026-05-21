def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

op ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    should_accumulate = True
    num1 = int(input("what is your first number? "))

    while should_accumulate:
        for symbol in op:
            print(symbol)
        operation = input("what is your operation? ")
        num2 = int(input("what is your second number? "))
        answer = op[operation](num1, num2)
        print(f"{num1} + {num2} = {answer}")

        choice = input(f"Type y to continue cal with {answer} or n to start new \n")

        if choice == "y":
            num1=answer
        else:
            should_accumulate = False
            print("\n"*200)
            calculator()



calculator()
