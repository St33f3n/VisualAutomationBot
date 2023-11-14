import os
import json
from PIL import Image

class Json_Handler():

    def __init__(self, name) -> None:
        self.name = name
        self.jsonData = {}
        self.loadData()


    def loadData(self):
        with open(f'{self.name}/info.json', 'r') as f:
            self.jsonData = json.load(f)

    def __str__(self):
        return self.jsonData

    def start():

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
            config = {}
            playset = [{'name' : ...,
                        'arg1' : ...,
                        'arg2' : ...,
                        'argN' : ...,
                        }]

            pictures_section = {}

            for imge in os.listdir(directory):
                if any(el in imge for el in ["png", "PNG"]):

                    img = Image.open(f"{directory}/{imge}")
                    w, h = img.size
                    pictures_section[os.path.splitext(imge)[0]] = {'width' : w, 'height' : h, 'path': f'{directory}/{imge}'}
        

            full_data = {'config': config, 'data' : data_section, 'playset' : playset, 'pictures' : pictures_section}

            file_path = os.path.join(directory, "info.json")


            with open(file_path, 'w') as f:
                json.dump(full_data, f, indent=2)

    def update(self):
        None

    def getData(self, option : str, key=None):

        # return the complete playset
        if option == 'playset':
            return self.jsonData[option]

        # Checks if a key is valid
        if key not in self.jsonData[option]:
            return None
        
        data = self.jsonData[option][key]

        return data

    def getPicture(self, key):
        data = self.getData('pictures', key=key)
        w = data['width']
        h = data['height']
        p = data['path']

        img = Image.open(p)

        return (w, h, img)
