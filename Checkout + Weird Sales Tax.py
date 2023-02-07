def checkout():
    total = 0
    count = 0
    moreItems = True
    
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        
        if price != 0:
            tax = float(input('Enter tax on that item:'))
        
        
        if price != 0:
            count = count + 1
            total = total + price + price*(tax/100)
            print('Subtotal: $', total)
        else:
            moreItems = False
   
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()