"""
File: webcrawler.py
Name: Daniel Wu (1.5hr)
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
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

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})
        male_num = 0
        female_num = 0

        for tag in tags:
            split_list = tag.tbody.text.split()  # a list stores strings split by spacing
            # The index of the number of male will be at 2, 7, 12 and so on. The female will be 4, 9, 14 and so on
            # There are 22 strings that is not related to the table, so need to be excluded.
            for i in range(2, len(split_list)-22, 5):
                male_num += int(''.join(split_list[i].split(',')))
            for i in range(4, len(split_list)-22, 5):
                female_num += int(''.join(split_list[i].split(',')))
        print(f'Male Number: {male_num}')
        print(f'Female Number: {female_num}')


if __name__ == '__main__':
    main()
