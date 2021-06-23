##python Dictionary_Practice.py
dict_food = {"chicken": "1.64", "beef": "1.99", "milk": "2.50", "ham": "2.00", "Sausig": "3.00"}

chicken_price = dict_food["chicken"]
##print("Price of chicken:" + chicken_price)

dict_food["beef"] = "2"
beef_price =  dict_food["beef"]
##print("Price of beef:" + beef_price)

#print("Shoes stocked in Shoes R Us™")
dict_shoes = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
##del dict_shoes["SB Dunk"]
Jordans = dict_shoes["Jordan 13"]
Jordans = Jordans + 4
Jordans = str(Jordans)
##print("Amt of  Jordans left: " + Jordans)
Yeezy = dict_shoes["Yeezy"]
Yeezy = Yeezy + 5
Yeezy = str(Yeezy)
##print("Amt of Yeezy's left: " + Yeezy)
Foamposite = dict_shoes["Foamposite"]
Foamposite = Foamposite + 4
Foamposite = str(Foamposite)
##print("Amt of Foamposite left: " + Foamposite)
AirMax = dict_shoes["Air Max"]
AirMax = AirMax + 4
AirMax = str(AirMax)
##print("Amt of Air Max's left: " + AirMax)
SBDunk = dict_shoes["SB Dunk"]
SBDunk = SBDunk + 2
SBDunk = str(SBDunk)
##print("Amt of SB Dunks left: " + SBDunk)

def restock (shoe, amt):
    shoe = shoe * amt

restock(Yeezy, 5)
#print(dict_shoes["Yeezy"])

def triangleArea(base, height):
        area = base*height/2
        return area

n = 5
m = 5
areaList = []
for b in range (0,n):
    for h in range (0,n):
        areaList.append(triangleArea(b,h))

Menu = {"Burgers": 12.99, "Fries": 3.00, "Shakes": 1.50}
def foodSum (item1, item2):
    sum = item1 + item2
    print("The total price of your order of " + str(item1) + " and " + str(item2) + " is " + str(sum))

foodSum(Menu["Burgers"], Menu["Fries"])

def price_difference (item1, item2):
    difference = item1 - item2
    print("The difference between the price of " + str(item1) + " and " + str(item2) + " is " + str(difference))

price_difference(Menu["Burgers"], Menu["Fries"])