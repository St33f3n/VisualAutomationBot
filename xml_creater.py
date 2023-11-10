import os
import json
from PIL import Image

all = list(filter(os.path.isdir, os.listdir()))

rm = ['.', 'lib']

directorys = [x for x in all if not any(substring in x for substring in rm)]


for directory in directorys:


    data_section = {
        "money" : 0,
    }

    pictures_section = []

    for imge in os.listdir(directory):
        if any(el in imge for el in ["png"]):

            w, h = Image.open(f"{directory}/{imge}").size
            pictures_section.append({'name' : imge, 'width' : w, 'height' : h})
 

    full_data = {'data' : data_section, 'pictures' : pictures_section}

    file_path = os.path.join(directory, "info.json")


    with open(file_path, 'w') as f:
        json.dump(full_data, f, indent=2)

