penny = int(input("How many pennies do you have "))
hundred = penny//10000
lefthundred = penny%10000
fifty = lefthundred//5000
leftfifty = lefthundred%5000
twenty = leftfifty//2000
lefttwenty = leftfifty%2000
ten = lefttwenty//1000
leftten = lefttwenty%1000
five = leftten//500
leftfive = leftten%500
one = leftfive//100
leftone = leftfive%100
quarters = leftone//25
leftquarters = leftone%25
dimes = leftquarters//10
leftdimes = leftquarters%25
nickels = leftdimes//5
leftnickels = leftdimes%5
pennies = leftnickels//1
print("You will have", str(hundred), "one hundred dollar bills,", str(fifty), "fifty dollar bills,", str(twenty), "twenty dollar bills,", str(ten), "ten dollar bills,", str(five), "five dollar bills,", str(one), "one dollar bills,", str(quarters), "quarters,", str(dimes), "dimes,", str(nickels), "nickels, and", str(pennies), "pennies.")

