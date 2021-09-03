from getLTP import get_ltp
from MyShares import shares

for share in shares:
    print(share +": "+get_ltp(share))

print("Total number of shares: "+str(len(shares)))