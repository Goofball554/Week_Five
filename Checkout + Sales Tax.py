def checkout():
    total = 0
    count = 0
    moreItems = True
    
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
       
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    
    average = total / count
    totalTax = total*1.02
    print('Total items:', count)
    print('Total $', total)
    print('Total WITH tax $', totalTax)
    print('Average price per item: $', average)

checkout()