# 1) Create a list of three countries.
countries = ['USA', 'Canada', 'Australia']
print(countries)
# 2) Add a country at the end of the list.
countries.append('Germany')
print(countries)
# 3) Remove any country using its index.
del countries[2]
print(countries)
# 4) Add a country in the middle of the list.
countries.insert(int(len(countries)/2), 'France')
print(countries)

# 1) Create a set of three countries.
countries = {'USA', 'Canada', 'Australia'}
print(countries)
# 2) Add a country to the set.
countries.add('Germany')
print(countries)
# 3) Remove any country from the set.
countries.remove('Australia')
print(countries)
# 4) Add a country to the set.
countries.add('France')
print(countries)
