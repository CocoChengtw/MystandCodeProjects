"""
File: webcrawler.py
Name: Coco
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        tags = soup.find_all('td')

        # find the top 200 data
        lst = []
        for tag in tags[1:1000]:
            tag = str(tag)
            tag = tag[tag.find('>')+1:tag.find('</')]
            lst.append(tag)

        # find male & female number, and add together
        male = 0
        female = 0
        comma = ','
        for num in range(len(lst)):
            if (num + 1) % 5 == 3:
                ans = ''.join(x for x in lst[num] if x not in comma)
                male += int(ans)
            if (num + 1) % 5 == 0:
                ans = ''.join(x for x in lst[num] if x not in comma)
                female += int(ans)

        print('Male number:', male)
        print('Female number:', female)


if __name__ == '__main__':
    main()
