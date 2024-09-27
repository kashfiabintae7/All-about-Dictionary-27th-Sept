country_code = {
    'India' : '0091',
    'Australia' : '0025',
    'Bangladesh' : '00880',
    'Nepal': '00977',

}


print("Country Code for India -")
print(country_code.get('India', 'Not Found'))

print("Country Code for Bangladesh -")
print(country_code.get('Bangladesh', 'Not Found'))

print("Country Code for Japan -")
print(country_code.get('Japan', 'Not Found'))


