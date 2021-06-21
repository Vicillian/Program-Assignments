##python Dictionary_Practice.py
dict_food = {"chicken": "1.64", "beef": "1.99", "milk": "2.50", "ham": "2.00", "Sausig": "3.00"}

chicken_price = dict_food["chicken"]
##print("Price of chicken:" + chicken_price)

dict_food["beef"] = "2"
beef_price =  dict_food["beef"]
##print("Price of beef:" + beef_price)

print("Shoes stocked in Shoes R Us™")
dict_shoes = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
##del dict_shoes["SB Dunk"]
Jordans = dict_shoes["Jordan 13"]
Jordans = Jordans + 4
Jordans = str(Jordans)
print("Amt of  Jordans left: " + Jordans)
Yeezy = dict_shoes["Yeezy"]
Yeezy = Yeezy + 5
Yeezy = str(Yeezy)
print("Amt of Yeezy's left: " + Yeezy)
Foamposite = dict_shoes["Foamposite"]
Foamposite = Foamposite + 4
Foamposite = str(Foamposite)
print("Amt of Foamposite left: " + Foamposite)
AirMax = dict_shoes["Air Max"]
AirMax = AirMax + 4
AirMax = str(AirMax)
print("Amt of Air Max's left: " + AirMax)
SBDunk = dict_shoes["SB Dunk"]
SBDunk = SBDunk + 2
SBDunk = str(SBDunk)
print("Amt of SB Dunks left: " + SBDunk)