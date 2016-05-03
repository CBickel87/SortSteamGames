import requests
from bs4 import BeautifulSoup
import sqlite3


conn = sqlite3.connect('game_ratingsdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Games;

CREATE TABLE Games (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE,
    metascore  INTEGER,
    userscore  REAL
);
''')

url='http://www.metacritic.com/browse/games/score/metascore/all/pc/filtered?sort=desc&view=condensed&page='

for i in range(33):
    res = requests.get(url+str(i), headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'html.parser')

    htmltitle = soup.select('div.product_item.product_title > a')
    htmlmetascore = soup.select('div.product_item.product_score > div')
    htmluserscore = soup.select('div.product_item.product_userscore_txt > span')

    title = [t.getText().strip() for t in htmltitle]
    metascore = [m.getText() for m in htmlmetascore]
    uscore = [u.getText() for u in htmluserscore]
    userscore = [u for u in uscore if u != 'User:']

    for t, m, u, in zip(title, metascore, userscore):
        print(t, m, u)

        with conn:
            cur.execute('''INSERT OR REPLACE INTO Games (title, metascore, userscore)
                VALUES (?, ?, ?)''', (t, m, u))

conn.commit()
cur.close()
conn.close()
