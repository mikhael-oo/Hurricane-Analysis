# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico',
         'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita',
         'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita',
         'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September',
          'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July',
          'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September',
          'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971,
         1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016,
         2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165,
                       180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'],
                  ['Mexico'], ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'],
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'],
                  ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'],
                  ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'],
                  ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded',
           '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B',
           '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B',
           '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65,
          19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:

def updated_damage(_damages):
    update_d = []
    for val in _damages:
        if val == 'Damages not recorded':
            update_d.append(val)
        elif val[-1] == 'M':
            update_d.append(float(val[:-1]) * 1000000)
        else:
            update_d.append(float(val[:-1]) * 1000000000)
    return update_d


# write your construct hurricane dictionary function here:
def construction(name, month, years_, max_sustained_wind, area_affected, damage_, death):
    main_dict = {}
    for i in range(len(name)):
        temp_dict = {'Name': name[i], 'Month': month[i], "Year": years_[i], 'Max Sustained Wind': max_sustained_wind[i],
                     'Areas Affected': area_affected[i], 'Damage': damage_[i], 'Deaths': death[i]}
        main_dict[name[i]] = temp_dict
    return main_dict


hurricane = construction(names, months, years, max_sustained_winds, areas_affected, updated_damage(damages), deaths)
print("The hurricane data is below:")
print(hurricane)
print("\n")


# write your construct hurricane by year dictionary function here:
def convert_to_year(construction_):
    main_dict = {}
    for val in construction_.values():
        main_dict[val["Year"]] = val
    return main_dict


year_dict = convert_to_year(hurricane)


# write your count affected areas function here:
def count_affected_areas(hurr):
    affected__areas = {}
    for name in hurr:
        for area in hurr[name]['Areas Affected']:
            if area in affected__areas:
                affected__areas[area] += 1
            else:
                affected__areas[area] = 1
    return affected__areas


affected_areas = count_affected_areas(hurricane)

print("The affected areas by count is below:")
print(affected_areas)
print('\n')


# write your find most affected area function here:
def max_affected(hurr):
    max_area = ""
    max_area_count = 0
    for key, val in hurr.items():
        if val > max_area_count:
            max_area = key
            max_area_count = val
    return "The most affected area is " + max_area + " and it was hit " + str(max_area_count) + " times."


max_hit = max_affected(affected_areas)

print(max_hit)
print('\n')


# write your greatest number of deaths function here:
def max_death(hurr):
    max_deaths = 0
    hur = ''
    for key, val in hurr.items():
        if val["Deaths"] > max_deaths:
            max_deaths = val["Deaths"]
            hur = val["Name"]
    return "Hurricane " + hur + " caused the maximum number of deaths by killing " + str(max_deaths) + " people."


maximum_death = max_death(hurricane)
print(maximum_death)
print('\n')


# write your categorization by mortality function here:

def mortality_rating(hurr):
    mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    for name in hurr:
        if hurr[name]['Deaths'] == mortality_scale[0]:
            mortality[0] = name
        elif mortality_scale[0] < hurr[name]['Deaths'] <= mortality_scale[1]:
            mortality[1].append(name)
        elif mortality_scale[1] < hurr[name]['Deaths'] <= mortality_scale[2]:
            mortality[2].append(name)
        elif mortality_scale[2] < hurr[name]['Deaths'] <= mortality_scale[3]:
            mortality[3].append(name)
        elif mortality_scale[3] < hurr[name]['Deaths'] <= mortality_scale[4]:
            mortality[4].append(name)
        else:
            mortality[5].append(name)
    return mortality


print("The scale of deaths of the hurricanes is below, ranking from 1 to 5, 5 as greatest:")
print(mortality_rating(hurricane))
print("\n")


# write your greatest damage function here:
def greatest_damage(hurr):
    max_damage = 0
    hur = ""
    for val in hurr.values():
        if val["Damage"] != "Damages not recorded" and val["Damage"] > max_damage:
            max_damage = val["Damage"]
            hur = val['Name']
    return "Hurricane " + hur + " caused the greatest costing about " + str(max_damage) + " US dollars."


maximum_damage = greatest_damage(hurricane)
print(maximum_damage)
print("\n")


# write your categorize by damage function here:

def damage_rating(hurr):
    damagess = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], "No record": []}
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    for val in hurr.values():
        if val["Damage"] == "Damages not recorded":
            damagess["No record"].append(val["Name"])
            continue
        elif val["Damage"] == 0:
            damagess[0].append(val["Name"])
        elif damage_scale[0] <= val["Damage"] < damage_scale[1]:
            damagess[1].append(val["Name"])
            continue
        elif damage_scale[1] <= val["Damage"] < damage_scale[2]:
            damagess[2].append(val["Name"])
            continue
        elif damage_scale[2] <= val["Damage"] < damage_scale[3]:
            damagess[3].append(val["Name"])
            continue
        elif damage_scale[3] <= val["Damage"] < damage_scale[4]:
            damagess[4].append(val["Name"])
            continue
        else:
            damagess[5].append(val["Name"])
    return damagess


damage_ratings = damage_rating(hurricane)
print(damage_ratings)
