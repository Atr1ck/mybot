from bs4 import BeautifulSoup
import re
import json

with open("musicdata.txt", "r") as f:
    html = f.read()
    soup = BeautifulSoup(html, "lxml")
    music_info = []
    for item in soup.find_all("div", class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-3 css-1etv89n"):
        try:
            music_id_path = item.find("a")["href"]
            match = re.search(r'\d+', music_id_path)
            music_id = match.group()

            music_name = item.find("div", class_="MuiCardMedia-root css-bc9mfn")["title"].split("|")[0].strip()
            
            music_cover_raw=  item.find("div", class_="MuiCardMedia-root css-bc9mfn")["style"]
            music_cover_webp_re = re.search(r'url\("(.*?)"\)', music_cover_raw)
            music_cover_webp = music_cover_webp_re.group(1)
            music_cover_png = music_cover_webp.replace('.webp', '.png')

            music_info.append({
                "music_id":music_id,
                "music_name":music_name,
                "music_cover_png":music_cover_png
            })
        except:
            break
    with open("src/others/pjsk_music.json", "w",encoding="UTF-8") as json_file:
        json.dump(music_info, json_file, ensure_ascii=False, indent=4)