
def collatz(number):
    val = 0
    if number % 2 == 0:
        val = number//2
    else:
        val = number * 3 + 1
    print(val)
    return val

def getCollatz(num):
    retval = collatz(num)
    if retval != 1:
        getCollatz(retval)
    return retval

if __name__ == "__main__":
    try:
        num = int(input("Enter a number:"))
        getCollatz(num)
    except ValueError:
        print("Please enter a valid number")