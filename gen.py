import json
from requests import get

REQ_URL = 'http://aod.parliament.act.gov.au/api/search/speeches/_/date/_/phrase/0'
M3U8_URL = ['http://video.parliament.act.gov.au/vod/amlst:', '/playlist.m3u8?DVR']

def get_json(url):
    return(json.loads(get(url).text))

json_data = get_json(REQ_URL)
urls_list = []

for speech in json_data:
    if(M3U8_URL[0] + speech['name'].replace(' #', '_').replace(' ', '_') + M3U8_URL[1] not in urls_list):
        urls_list.append(M3U8_URL[0] + speech['name'].replace(' #', '_').replace(' ', '_') + M3U8_URL[1])

with open('assembly_url_list.txt', 'w') as file:
    for url in urls_list:
        file.write(url + '\n')