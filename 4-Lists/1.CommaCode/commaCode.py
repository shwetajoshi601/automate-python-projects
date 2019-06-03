def addComma(items):
    val=''
    for i in range(len(items)):
        # if it is not the last element
        if i != len(items) -1:
            val = val + items[i] + ', '
        # last element
        else:
            val = val + 'and ' + items[i]
    return val

# Alternative solution
def addComma2(items):
    items = ["bat", "ball", "wickets", "pads", "helmet"]
    # use ', ' as a separator and join items upto the second last element
    val = ", ".join(items[:len(items)-1])
    # add the last element with 'and'
    val = val + ", and " + items[-1]
    return val

if __name__ == "__main__":
    myList = ["bat", "ball", "wickets", "pads", "helmet"]
    print(addComma(myList))
    print(addComma2(myList))
