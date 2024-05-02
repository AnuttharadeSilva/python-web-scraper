from bs4 import BeautifulSoup
import requests
import re
import csv

csv_file = open('ovp_all_all.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'description','genre','keywords','duration','popularity','video_url','image_path' ])

with open('ovp_all_all.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

results = soup.find('table', class_='resultsTable')

for result in results.find_all('tr'):
    td = result.find('td', class_='smalltext')
    td_img = result.find('td', class_='imageTd')
    if td != None and td_img!= None:
        td_text = td.text.replace('\n', '').replace('\t', '')
        # print(td.a.text)
        title = td.a.text
        video_url = td.find('a', href=True)['href']
        img_file = td_img.find('img', src=True)['src']

        # td_text = "Lucky Strike Cigarette Commercial: Square Dance (1948) Lucky Strike cigarette commercial with stop-motion animation of square-dancing cigarettes. Genre: EphemeralKeywords: Advertising: Television commercials;Substance abuse: Tobacco;Animation: Stop-motion;Duration: 00:00:58Popularity (downloads): 5126"

        parts = re.split(r'(?:Genre:\s)|(?:Keywords:\s)|(?:Duration:\s)|(?:Popularity\s\(downloads\):\s)', td_text)
        parts = [x for x in parts if x is not None]
        # print(parts)

        try:
            # title = parts[0].strip()
            # year = parts[1].strip('()')
            description = parts[0].strip()
            genre = parts[1].strip()
            keywords = parts[2].strip()
            duration = parts[3].strip()
            popularity = parts[4]
        except:
            # title = None
            # year = None
            description = None
            genre = None
            keywords = None
            duration = None
            popularity = None

        print("Title:", title)
        # print("Year:", year)
        print("Description:", description)
        print("Genre:", genre)
        print("Keywords:", keywords)
        print("Duration:", duration)
        print("Popularity:", popularity)
        print("Video URL:", video_url)
        print("Image Path:",img_file)
        print("\n")

        csv_writer.writerow([title, description, genre, keywords, duration, popularity, video_url, img_file])

csv_file.close()