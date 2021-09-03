from openpyxl import Workbook
from MyShares import shares
from getLTP import get_ltp

# Get the price of the list of shares in a excel file
workbook = Workbook()
sheet = workbook.active
sheet["A1"] = "Ticker"
sheet["B1"] = "Price"
for i in range(len(shares)):
    nameCell = "A" + str(i + 2)
    priceCell = "B" + str(i + 2)
    sheet[nameCell] = shares[i]
    sheet[priceCell] = float(get_ltp(shares[i]))
    print(shares[i] + " : " + get_ltp(shares[i]))

workbook.save(filename="hello_world.xlsx")
