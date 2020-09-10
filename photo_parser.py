import requests
import csv

codes = ['ALL_ar',
'ALL_am',
'ALL_au',
'ALL_at',
'ALL_az',
'ALL_bs',
'ALL_bh',
'ALL_bd',
'ALL_by',
'ALL_be',
'ALL_ba',
'ALL_br',
'ALL_vg',
'ALL_bg',
'ALL_kh',
'ALL_ca',
'ky_ALL',
'ALL_cl',
'ALL_co',
'ALL_cy',
'ALL_cz',
'ALL_dk',
'ALL_do',
'ALL_ec',
'ALL_eg',
'ALL_ee',
'ALL_fi',
'ALL_fr',
'ALL_pf',
'ALL_ge',
'ALL_de',
'ALL_gr',
'ALL_hk',
'ALL_in',
'ALL_id',
'ALL_ie',
'ALL_il',
'ALL_it',
'ALL_jp',
'ALL_jo',
'ALL_kz',
'ALL_kg',
'ALL_la',
'ALL_lv',
'ALL_lb',
'ALL_lt',
'ALL_my',
'ALL_mv',
'ALL_mt',
'ALL_mx',
'ALL_md',
'ALL_mn',
'ALL_nz',
'ALL_ph',
'ALL_pl',
'ALL_pt',
'ALL_qa',
'ALL_ro',
'ALL_ru',
'ALL_sa',
'ALL_rs',
'ALL_sg',
'ALL_sk',
'ALL_si',
'ALL_kr',
'ALL_es',
'ALL_lk',
'ALL_se',
'ALL_tw',
'ALL_tj',
'ALL_th',
'ALL_tn',
'ALL_tr',
'ALL_ua',
'ALL_ae',
'ALL_uk',
'ALL_ALL',
'ALL_um',
'ALL_uy',
'ALL_uz',
'ALL_ve',
'ALL_vn',]
coutries = ['Argentina',
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

urls = []

for i in codes:
    url = f'https://maps.google.com/intl/{i}/streetview/feed/photographer/data.json'
    if url not in urls:
        urls.append(url)

def parse():
    x = 0
    for url in urls:
        data = requests.get(url).json()
        i = 0
        with open(f'parsed_{coutries[x]}.csv', 'w', encoding='utf8') as file:
            write = csv.writer(file)
            write.writerow(('Name', 'Agency', 'Website', 'City', 'Phone', 'E-mail'))
            while i < len(data):
                name = data[i]['name']
                try:
                    agency = data[i]['agency']
                except:
                    agency = 'UNKNOWN'
                if(agency == ''):
                    agency = 'FALSE'
                try:
                    website = data[i]['website']
                except:
                    website = 'UNKNOWN'
                if(website == ''):
                    website = 'none'
                city = data[i]['city_english']
                phone = data[i]['phone']
                email = data[i]['email']
                write.writerow((name, agency, website, city, phone, email))
                i += 1
            x += 1

parse()
