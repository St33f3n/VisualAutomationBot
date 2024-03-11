import os
import json
from PIL import Image

startup = {"config": {}, "ressource": {}, "playset": [], "actionset" : {}, "pictures": {}}
# functions = ["keyPress", "compareRessources((1,1,1))",  "clickIfPicture(img, img)", "locateRessources(img)", "wait()", "conditionalAction(n, 2)"] # dragMouse 
functions = {
    "keyPress": "Add key with text box",
    "compareRessources": "ressource, (0 = >, 1 = <, 2 = ==)",
    "clickIfPicture": "picture to find, picture to click on",
    "locateRessources": "picture to locate resources",
    "wait": "stop, long, key, click",
    "conditionalAction": " condition, action, confidence",
    "dragPictureToPicture": "Add two pictures",
    "dragFromPicture": "picture, pixel to move, direction (0 = N, 180 = S, all are available)",
}
class JsonHandler():
    """
    A class to handle JSON data.

    Attributes:
        name (str): The name of the JSON file.
        jsonData (dict): The JSON data.
    """
    def __init__(self, name) -> None:
        self.name = name
        self.jsonData = {}
        self.loadData()


    def __str__(self):
        """
        Returns a string representation of the JSON data.

        Returns:
            str: String representation of the JSON data.
        """
        return self.jsonData


    def loadData(self):
        """
        Loads JSON data from file.
        """
        config_file = f'{self.name}/config.json'
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.jsonData = json.load(f)
        else:
            with open(config_file, "w") as f:
                json.dump(startup, f, indent=4)
                self.jsonData = startup


    def saveData(self): 
        """
        Saves JSON data to file.
        """
        with open(f'{self.name}/config.json', 'w') as f:
            json.dump(self.jsonData, f, indent=4)


    # from lib.JsonHandler import JsonHandler 
    # than JsonHandler.create_...
    # no object need to be created
    def create_ressourceData(name, value, x, y):
            """
        Creates resource data.

        Args:
            name (str): The name of the resource.
            value (int): The value of the resource.
            x (int): The x-coordinate of the resource.
            y (int): The y-coordinate of the resource.

        Returns:
            dict: The resource data.
        """
            return {name : {'value' : value, 'position' : {'x' : x,'y' : y}}}


    def saveNewPicture(self, name, img : Image, path, windowSize, screenSize):
        """
        Saves a new picture.

        Args:
            name (str): The name of the picture.
            img (Image): The image object.
            path (str): The path of the image.
            windowSize (tuple): The size of the window.
            screenSize (tuple): The size of the screen.
        """
        w, h = img.size
        window_width, window_height = windowSize
        screen_width, screen_height = screenSize
        data = {
            name: {
                "width": w,
                "height": h,
                "path": path,
                "windowSize": {
                    "width": window_width,
                    "height": window_height
                },
                "screenSize": {
                    "width": screen_width,
                    "height": screen_height
                }
            }
        }
        self.add(data, "pictures",)
        self.saveData()


    def add(self, option, data : tuple):
        """
        Adds data to JSON.

        Args:
            option (str): The option to update.
            data (name, directory): The data to update.
        """
        if option not in self.jsonData:
            raise ValueError(f'No {option} in jsonData')
        self.jsonData[option][data[0]] = data[1]


    def add(self,  data : dict, option = None):
        """
        Updates JSON data.

        Args:
            data (dict): The data to add.
            option (str, optional): The option to add data to. Defaults to None.
        """
        if option == None:
            self.jsonData.update(data)
            return

        if option not in self.jsonData:
            raise ValueError(f'No {option} in jsonData')
        self.jsonData[option].update(data)


    def valueUpdate(self, option, data : tuple):   
        key, value = data
        
        if key not in self.jsonData[option]:
            raise ValueError(f'No {key} in {option}')
        
        self.jsonData[option][key]["value"] = value
        
        self.saveData()


    def remove(self):
        """
        Removes JSON data.
        """
        pass
  

    def getData(self, option : str, key=None):
        """
        Gets JSON data.

        Args:
            option (str): The option to get data from.
            key (str, optional): The key to get. Defaults to None.

        Returns:
            dict: The requested data.
        """
        # return the complete playset
        if key == None:
            if option in self.jsonData:
                return self.jsonData[option]

        # if option == 'playset':
        #     return self.jsonData[option]
        
        # if option == 'actionset':
        #     return self.jsonData[option]
        
        # if option == 'pictures' and key == 0:
        #     return self.jsonData[option]

        # Checks if a key is valid
        if key not in self.jsonData[option]:
            raise ValueError(f'No {key} in jsonData[{option}]')
        
        data = self.jsonData[option][key]

        return data

    def getPictureData(self, key):
        """
        Gets picture data.

        Args:
            key (str): The key of the picture.

        Returns:
            tuple: The picture data.
        """
        data = self.getData('pictures', key=key)
        w = data['width']
        h = data['height']
        p = data['path']
        wS = data['windowSize']
        sS = data['screenSize']

        img = Image.open(p+".png")

        return (w, h, img)
    
    def getRessourceData(self, key):
        """
        Gets resource data.

        Args:
            key (str): The key of the resource.

        Returns:
            tuple: The resource data.
        """
        data = self.getData('ressource', key=key)
        v = data['value']
        sx = data['position']['x']
        sy = data['position']['y']
        return (v, sx, sy) 
