child_price = float ( input ("enter the price of a child's meal: ") )
adult_price = float (input ("enter the price of adult's meal:") )
number_children = int (input ("enter the number of children:") )
number_adults = int  (input ("enter the number adults:") )
tax_rate = float (input("enter the sales tax(in decimal form):"))

#calculate price
child_price_total = child_price * number_children
adult_price_total = adult_price * number_adults

#adding prices
Subtotal= child_price_total + adult_price_total

# salestax
sales_tax = Subtotal * tax_rate/100

#totalprice
total_price = Subtotal + sales_tax


print()


print (f'Subtotal: ${Subtotal:.2f}')
print (f'Tax : ${sales_tax:.2f}')
print (f'Total: ${total_price:.2f}')