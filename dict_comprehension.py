'''
cities_in_f={"New York":22,"Boston":75,"Los Angles":100,"Chicago":50}
cities_in_c={key:(round(value-32)+(5/9)) for (key, value) in cities_in_f.items()}
print(cities_in_c)
'''

'''
weather={"New York":"Snowing","Boston":"Sunny","Los Angles":"Sunny","Chicago":"Snowing"}
sunny_weather={key:value for (key, value) in weather.items() if value=="Sunny"}
print(sunny_weather)

cities={"New York":32,"Boston":44,"Los Angles":42,"Chicago":36}
desc_cities={key:{"warm" if value >= 40 else "cold"} for (key, value) in cities.items()}
print(desc_cities)
'''
def check_value(value):
    if value >= 70:
        return "HOT"
    elif 69>=value>=40:
        return 'WARM'
    else:
        return "COLD"

cities={"New York":32,"Boston":44,"Los Angles":42,"Chicago":36}
desc_cities={key:check_value(value) for (key, value) in cities.items()}
print(desc_cities)