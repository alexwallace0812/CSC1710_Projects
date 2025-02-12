# Alex Wallace
# Lab3C 
# 9/5/23
# This program takes a 6 digit code and calculates a checksum
# Each part of the lab prior were helping to understand how to create a working program that calculates the smallest number of currency
code = int(input("Enter a six digit number: "))
d6 = code%10
leftd6 = code//10
d5 = leftd6%10
leftd5 = leftd6//10
d4 = leftd5%10
leftd4 = leftd5//10
d3 = leftd4%10
leftd3 = leftd4//10
d2 = leftd3%10
leftd2 = leftd3//10
d1 = leftd2%10
leftd1 = leftd2//10
print(d1, d2, d3, d4, d5, d6)
checkleft = d1 + d2
checkleftleft = checkleft%10
checkmiddle = d3 + d4
checkmiddlemiddle = checkmiddle%10
checkright = d5 + d6
checkrightright = checkright%10
checksummaybe = checkleftleft + checkrightright + checkmiddlemiddle
checksum = checksummaybe%10
print(checksum)

