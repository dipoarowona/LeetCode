def reverse(x):
    
    y = str(abs(x))
    if x<0:
        z = "-"+y[::-1]
    else:
        z = y[::-1]
    
    if abs(int(z)).bit_length()>31:
        return 0

    return(int(z))

print(reverse(123))