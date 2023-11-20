from ast import List, Tuple
import os
import json
from PIL import Image

def create_ressourceData( name, value, x, y):
        return (name , {'value' : value, 'position' : {'x' : x,'y' : y}})

def create_playsetData( name, arg1, arg2, argN):
    return {'name': name, 'arg1': arg1, 'arg2' : arg2, 'argN' : argN}

# TODO reag img path
def create_imageData(name, img : Image, path):
    w, h = img.size
    # p = img.filename
    return (name, {'width': w, 'height' : h, 'path': path})

class Json_Handler():

    def create_ressourceData(self, name, value, x, y):
        return (name , {'value' : value, 'position' : {'x' : x,'y' : y}})

    def create_playsetData(self, name, arg1, arg2, argN):
        return {'name': name, 'arg1': arg1, 'arg2' : arg2, 'argN' : argN}

    # TODO reag img path
    def create_imageData(self, name, img : Image, path):
        w, h = img.size
        # p = img.filename
        return (name, {'width': w, 'height' : h, 'path': path})

    def __init__(self, name) -> None:
        self.name = name
        self.jsonData = {}
        self.loadData()

    def __str__(self):
        return self.jsonData

    def loadData(self):
        with open(f'{self.name}/config.json', 'r') as f:
            self.jsonData = json.load(f)

    def saveData(self): 
        with open(f'{self.name}/config.json', 'w') as f:
            json.dump(self.jsonData, f, indent=2)

    # data is Tuple (name, directory)
    def add(self, option, data : Tuple):
        if option not in self.jsonData:
            raise ValueError(f'No {option} in jsonData')
        self.jsonData[option][data[0]] = data[1]

    def add(self, option, data : dict):
        if option not in self.jsonData:
            raise ValueError(f'No {option} in jsonData')
        self.jsonData[option] # TODO need finish the playset dict add

    def update(self, option, data : Tuple):
        if option not in self.jsonData:
            print(0)
            if data[0] in self.jsonData[option]:
                raise ValueError(f'No {option} in jsonData')
            
        print(data)
        self.jsonData[option][data[0]] = data[1]
        self.saveData()

    
    # TODO playset update if needed
    # def update(self, option, data : Tuple):
    #     None

    def remove(self):
        None
  

    def getData(self, option : str, key=None):
        print(option, key)
        # return the complete playset
        if option == 'playset':
            return self.jsonData[option]

        # Checks if a key is valid
        if key not in self.jsonData[option]:
            raise ValueError(f'No {key} in jsonData[{option}]')
        
        data = self.jsonData[option][key]

        return data

    def getPictureData(self, key):
        data = self.getData('pictures', key=key)
        w = data['width']
        h = data['height']
        p = data['path']

        img = Image.open(p)

        return (w, h, img)
    
    def getRessourceData(self, key):
        data = self.getData('ressource', key=key)
        v = data['value']
        sx = data['position']['x']
        sy = data['position']['y']
        return (v, sx, sy) 







def start():

    all = list(filter(os.path.isdir, os.listdir()))

    rm = ['.', 'lib']

    directorys = [x for x in all if not any(substring in x for substring in rm)]


    for directory in directorys:


        ressource_section = {
            "money" : {
                'value' : 0, 
                'position' : {
                    'x' : 0,
                    'y' : 0
                }
            },
            
        }
        config = {}
        playset = [{'name' : "",
                    'arg1' : "",
                    'arg2' : "",
                    'argN' : "",
                    }]

        pictures_section = {}

        for imge in os.listdir(directory):
            if any(el in imge for el in ["png", "PNG"]):

                img = Image.open(f"{directory}/{imge}")
                img_dat = create_imageData(os.path.splitext(imge)[0], img, f"{directory}/{imge}")
                # pictures_section[os.path.splitext(imge)[0]] = {'width' : w, 'height' : h, 'path': f'{directory}/{imge}'}
                pictures_section[img_dat[0]] = img_dat[1]

        full_data = {'config': config, 'ressource' : ressource_section, 'playset' : playset, 'pictures' : pictures_section}

        file_path = os.path.join(directory, "config.json")


        with open(file_path, 'w') as f:
            json.dump(full_data, f, indent=2)