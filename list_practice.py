##python list_practice.py
empty_list = []
city_list = ["Oakland", "Atlanta", "New York City", "Seattle", "Mempish", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
##print(city_list)
print(city_list[9])
city_list[0] = "San Francisco"
city_list[2] = "Brooklyn"
city_list[7] = "Hollywood"
city_list[5] = "Tampa"
city_list.append("New Jersey")
city_list.extend(["Oakland", "New York City", "Los Angeles"])
city_list.insert(0, "Miami")

del city_list[1]
city_list.pop(8)
city_list.remove("Oakland")
city_list.remove("Los Angeles")

print(city_list)

three_cities = city_list[0:3]
print(three_cities)

bean_list = ["Pinto Bean", "String Bean", "Green bean", "Refried Bean", "Raw Bean", "Mr.Bean", "Beany", "Cranberry Bean", "Flat Bean", "Common Bean"]
##print(bean_list)

new_list= ["new 1", "new 2 "]
type(new_list)