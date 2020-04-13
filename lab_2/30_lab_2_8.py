def is_power_of_two(n):
    # checks if it's a power of 2 by making sure that all bits after that bitwise & operation are 0.
    # The bitwise operation is designed to be only True for powers of 2 — with one exception:
    # if n (and thus all of its bits) were 0 to begin with.
    return (n != 0) and (n & (n - 1) == 0)

        

  
if __name__ == '__main__':
    n = input('Enter a number: ')
    while type(n) != int:    
        try:
            n = int(n)
            result = is_power_of_two(n)
            print("Yes") if result else print("No")
        except (TypeError, ValueError):
            print('This is not a number.')
            n = input('Enter a number: ')
        
        
        