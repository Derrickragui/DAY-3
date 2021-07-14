'''
Given the exclusive price of milk and VAT Calculate the inclusive price of milk in supermarket
'''
#The function calculates the inclusive price of items from the developers point of view.
def calculateInclusiveprice (exclusiveprice,vatTax ):
     inclusiveprice = exclusiveprice + exclusiveprice * vatTax#This calculates the inclusive price using the parameters above.
     return inclusiveprice#This gives back the inclusive price calculated above.
#The fuction creates a user interface where the user is required to key in the required details to calculate the inclusive price
def userinputexcltaxrate():
    exclusiveprice = float(input("Enter exclusive price"))#This prompts the user to key in the exclusive price.
    vatTax = float(input("Enter vatTax"))#This prompts the user to key in vat tax

    return calculateInclusiveprice(exclusiveprice,vatTax)

print (userinputexcltaxrate())


