import os
import json
from PIL import Image

all = list(filter(os.path.isdir, os.listdir()))

rm = ['.', 'lib']

directorys = [x for x in all if not any(substring in x for substring in rm)]


for directory in directorys:


    data_section = {
        "money" : {
            'value' : 0, 
            'position' : {
                'x' : 0,
                'y' : 0
            }
        },
        
    }

    pictures_section = {}

    for imge in os.listdir(directory):
        if any(el in imge for el in ["png", "PNG"]):

            img = Image.open(f"{directory}/{imge}")
            w, h = img.size
            pictures_section[os.path.splitext(imge)[0]] = {'width' : w, 'height' : h, 'path': f'{directory}/{imge}'}
 

    full_data = {'data' : data_section, 'pictures' : pictures_section}

    file_path = os.path.join(directory, "info.json")


    with open(file_path, 'w') as f:
        json.dump(full_data, f, indent=2)

