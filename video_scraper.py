from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('datasets/ovp_all_all_video.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Id","MPEG-1","MPEG-2","MPEG-4","QuickTime","RealMedia","Year","Genre","Keywords","Duration","Color","Sound","Amount of Motion","Language","Sponsor","Contributing Organization","Transcript Available","Digitization Date","Digitizing Organization"])

csv_path = 'datasets/ovp_all_all.csv'
with open(csv_path, newline='') as csv_read:
    video_list = csv.reader(csv_read, delimiter=',')
    next(video_list)
    for row in video_list:
        video_id = row[0]

        source = requests.get('https://open-video.org/details.php?videoid='+video_id).text

        soup = BeautifulSoup(source, 'lxml')

        all_details = []
        all_details.append(video_id)

        downloads = soup.find('td', class_='downloadLinks')

        video_urls = [None, None, None, None, None]
        video_types = ["MPEG-1","MPEG-2","MPEG-4","QuickTime","RealMedia"]

        for link in downloads.find_all('a', href=True):
            url = link['href']
            type = link.text.replace(' ', '')

            i = video_types.index(type)
            video_urls[i]=url

        # print("Video URLs:", video_urls)

        all_details.extend(video_urls)

        video_metadata = []

        for metadata in soup.find_all('table', class_='metadataTable'):
            rows = metadata.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 2:
                    label = cells[0].text.strip()
                    value = cells[1].text.strip()
                    # print(f"{label} {value}")

                    video_metadata.append(value)


        # print("Video Metadata:", video_metadata)

        all_details.extend(video_metadata)
        # print(all_details)
        # print(len(all_details))
        if len(all_details) == 19:
            csv_writer.writerow(all_details)

csv_file.close()