master_covid_data = { 'usa' : {'+ive': 20, 'test': 200 },
                    'india': {'+ive': 15, 'test': 100 },
                    'af': {'+ive': 2, 'test': 20 },
                    'zim': {'+ive': 10, 'test': 1 }}
today_data = {'usa' : {'+ive': 1, 'test': 1.5 },
         'india': {'+ive': 0.75, 'test': 1 } }
for country in today_data:
    if country in master_covid_data:
        for key in today_data[country]:
            master_covid_data[country][key] += today_data[country][key]
for country, cases in master_covid_data.items():
    print(f"{country} : {cases} ")