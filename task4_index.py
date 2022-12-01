import zip_util
from geopy.distance import geodesic

zip_codes = zip_util.read_zip_all()


def loc_f():
    flag = True
    location = []
    while flag:
        zip_code = input('Enter a ZIP Code to lookup or enter "end" for exit=>').casefold()
        if zip_code == 'end':
            break
        else:
            for itm in range(0, len(zip_codes)):
                line = zip_codes[itm]
                if line[0] == zip_code:
                    location = line
                    lat = '{:010.9}'.format(abs(location[1]))
                    long = '{:010.9}'.format(abs(location[2]))
                    print(f'ZIP Code {location[0]} is in {location[3]}, {location[4]}, {location[5]} county, '
                          f'coordinates: ({lat[0:3]}\xb0{lat[4:6]}\'{lat[6:8]}.{lat[8:10]}\"N, '
                          f'{long[0:3]}\xb0{long[4:6]}\'{long[6:8]}.{long[8:10]}\""W)')
                    flag = False
            if flag:
                print("Invalid or unknown ZIP Code")
    return location


def zip_f():
    flag = True
    location = []
    while flag:
        city_name = input('Enter a city name to lookup or enter "end" for exit)=>').casefold()
        if city_name == 'end':
            print('Choose command:')
            break
        state_name = input('Enter the state name to lookup or enter "end" for exit)=>').casefold()
        if state_name == 'end':
            print('Choose command:')
            break
        zip_code_list = []
        location = []
        for itm in range(0, len(zip_codes)):
            line = zip_codes[itm]
            if line[3].casefold() == city_name and line[4].casefold() == state_name:
                zip_code_list.append(line[0])
                location = line
                flag = False
        if not flag:
            print(f'The following ZIP Code(s) found for {location[3]}, {location[4]}:', ', '.join(zip_code_list))
        if flag:
            print(f"No ZIP Code found for {location[3]}, {location[4]}")
    return location


def dist_f():
    flag = True
    point1 = []
    point2 = []
    distance = 0
    while flag:
        count = 0
        zip_code1 = input('Enter the first ZIP Code or enter "end" for exit=>').casefold()
        if zip_code1 == 'end':
            break
        zip_code2 = input('Enter the second ZIP Code or enter "end" for exit=>').casefold()
        if zip_code2 == 'end':
            break
        for itm in range(0, len(zip_codes)):
            line = zip_codes[itm]
            if line[0] == zip_code1:
                point1.append(line[1])
                point1.append(line[2])
                count += 1
        for itm in range(0, len(zip_codes)):
            line = zip_codes[itm]
            if line[0] == zip_code2:
                point2.append(line[1])
                point2.append(line[2])
                count += 1
        if count == 2:
            flag = False
            distance = geodesic(point1, point2).miles
            print(f'The distance between {zip_code1} and {zip_code2} is {distance:.2f} miles')
        if flag:
            print(f"The distance between {zip_code1} and {zip_code2} cannot be determined")
    return distance


def command():
    flag = True
    while flag:
        var = input("Command ('loc', 'zip', 'dist', 'end') =>").casefold()
        if var == 'end':
            print('Bye!')
            break
        elif var == 'loc':
            loc_f()
        elif var == 'zip':
            zip_f()
        elif var == 'dist':
            dist_f()
        else:
            print("Invalid command, ignoring")


command()
