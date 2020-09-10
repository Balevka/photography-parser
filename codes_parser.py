import requests
from bs4 import BeautifulSoup as bs

countries = ['Argentina',
'Armenia',
'Australia',
'Austria',
'Azerbaijan',
'Bahamas',
'Bahrain',
'Bangladesh',
'Belarus',
'Belgium',
'Bosnia and Herzegovina',
'Brasil',
'British Virgin Islands',
'Bulgaria',
'Cambodia',
'Canada',
'Cayman Islands',
'Chile',
'Colombia',
'Cyprus',
'Czech Republic',
'Denmark',
'Dominican Republic',
'Ecuador',
'Egypt',
'Estonia',
'Finland',
'France',
'French Polynesia',
'Georgia',
'Germany',
'Greece',
'Hong Kong',
'India',
'Indonesia',
'Ireland',
'Israel',
'Italy',
'Japan',
'Jordan',
'Kazakhstan',
'Kyrgyzstan',
'Laos',
'Latvia',
'Lebanon',
'Lithuania',
'Malaysia',
'Maldives',
'Malta',
'México',
'Moldova',
'Mongolia',
'New Zealand',
'Philippines',
'Poland',
'Portugal',
'Qatar',
'Romania',
'Russia',
'Saudi Arabia',
'Serbia',
'Singapore',
'Slovakia',
'Slovenia',
'South Korea',
'Spain',
'Sri Lanka',
'Sweden',
'Taiwan',
'Tajikistan',
'Thailand',
'Tunisia',
'Turkey',
'Ukraine',
'United Arab Emirates',
'United Kingdom',
'United States',
'United States Minor Outlying Islands',
'Uruguay',
'Uzbekistan',
'Venezuela',
'Vietnam']

base_url = "https://maps.google.com/streetview/hire/"
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.94'}
def codes(base_url, headers):
    x = 0
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        select = soup.find_all('option', attrs={})
        for all in select:
            xd = all['data-name']
            if (countries[x] == xd):
                print(all['value'])
                x += 1
        print(select)

codes(base_url,headers)