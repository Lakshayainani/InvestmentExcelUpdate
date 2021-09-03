from jugaad_data.nse import NSELive
n = NSELive()

def get_ltp(shareSymbol):
    global price
    try:
        price = n.stock_quote(str(shareSymbol).upper())['priceInfo']['lastPrice']
    except Exception as error:
        print("error at: "+shareSymbol+" "+str(error))
    return str(price)

# print("INFY : "+get_ltp('infy'))