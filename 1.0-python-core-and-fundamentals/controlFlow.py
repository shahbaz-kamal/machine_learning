for i in range(10,50):
    if i == 0:
        label = "Zero"
    elif i % 2 == 0:
        label = "even"
    else:
        label = "odd"
    print(i, " is ", label)
