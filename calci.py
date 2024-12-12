# SP=Selling Price
# cgst=central govt gst
# sgst=state govt gst
import os
import csv
import sys
import math
import numpy as np
import datetime

dt=[datetime.datetime.now()]

print(dt)
print("\t GST BILLING SOFTWARE")
print("\t CREATED BY - BHARAT MANGAL")

busn=input("Enter Your Business Name ")
item=input("Enter Item Name ")
SP=[float(input("Enter selling price of item "+item+": "))]
gstRate=[float(input("Enter GST Rate (%): "))]
cgst1=np.divide(gstRate,2)
cgst2=np.divide(cgst1,100)
cgstf=np.multiply(cgst2,SP)
sgst=cgstf
amt=SP+cgstf+sgst # Consumer will buy at this price

print("\t\t\t",busn)
print("\t\t\t INVOICE")
print("\t\t\t Item:",item)
print("\t\t\t Price:",SP)
print("\t\t\t CGST(@",(np.divide(gstRate,2)),"%):",cgstf)
print("\t\t\t SGST(@",(np.divide(gstRate,2)),"%):",sgst)
print("\t\t\t Amount payable:",amt)

import csv
with open('bill.jpg', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(busn)
    writer.writerow("INVOICE")
    writer.writerow(dt)
    writer.writerow(item)
    writer.writerow("Price")
    writer.writerow(SP)
    writer.writerow("cgst : gstrate @")
    writer.writerow(cgstf)
    writer.writerow("sgst : gstrate @")
    writer.writerow(sgst)
    writer.writerow("Amount Payable:")
    writer.writerow(amt)
    
    
os.startfile("bill.jpg", "print")

#For Converting It To Exe,,, We Use Command TO Run On Command Prompt,,,Command :- auto-py-to-exe
