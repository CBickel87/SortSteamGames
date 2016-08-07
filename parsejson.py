import json
import csv

with open('AppList.json', encoding='UTF8') as data1, open ('steamlist.json', encoding='UTF8') as data2:
    data1 = json.load(data1)
    data2 = json.load(data2)

d1 = (data1['applist']['apps']['app'])
d2 = (data2['response']['games'])

for index1 in d2:
    for index2 in d1:
        appid1 = index1['appid']
        appid2 = index2['appid']
        names = index2['name']

        if appid1 == appid2:
            with open('metacritic.csv', newline='') as fr:
                csv_reader = csv.reader(fr)
                csv_writer = csv.writer(fr)
                for row in csv_reader:
                    if names == row[0]:
                        results = [appid1, names, row[1], row[2]]

                        with open('currentgames.csv', 'a', newline='') as fw:
                            csv_writer = csv.writer(fw)
                            csv_writer.writerow(results)
