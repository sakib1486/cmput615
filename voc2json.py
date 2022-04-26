import os
import glob
import xml.etree.ElementTree as ET
import xmltodict
import json
from xml.dom import minidom
from collections import OrderedDict

def XML2JSON(xmlFiles):
    attrDict = dict()
    attrDict["categories"]=[{"supercategory":"none","id":"1","name":"pneumonia"},
                    {"supercategory":"none","id":"2","name":"backbone"}
                  ]
                  
    images = list()
    image_id = 0
    
    for file in xmlFiles:
        annotations = list()
        image = dict()


        image_id = image_id + 1      
        annotation_path=file
        doc = xmltodict.parse(open(annotation_path).read(), force_list=('object'))

        image["image_id"] = image_id
        image['file_name'] = str(doc['annotation']['filename'])
        image['height'] = int(doc['annotation']['size']['height'])
        image['width'] = int(doc['annotation']['size']['width'])
        print ("File Name: {} and image_id {}".format(file, image_id))
        id1 = 1
        if 'object' in doc['annotation']:
            for obj in doc['annotation']['object']:
                for value in attrDict["categories"]:
                    annotation = dict()          
                    if str(obj['name']) == value["name"]:
                        x1 = int(obj["bndbox"]["xmin"])  - 1
                        y1 = int(obj["bndbox"]["ymin"]) - 1
                        x2 = int(obj["bndbox"]["xmax"]) - x1
                        y2 = int(obj["bndbox"]["ymax"]) - y1                         
                        annotation["bbox"] = [x1, y1, x2, y2]
                        annotation["bbox_mode"] = 1
                        annotation["category_id"] = value["id"]
                        annotations.append(annotation)

                    else:
                        print("File: {} doesn't have any object".format(file))

        else:
            print("File: {} not found".format(file))
        image["annotations"] = annotations

        images.append(image)
            

    attrDict["images"] = images    
    #attrDict["annotations"] = annotations
    #attrDict["type"] = "instances"

    jsonString = json.dumps(attrDict["images"])
    with open("test.json", "w") as f:
        f.write(jsonString)


#path="/home/sakib-hasan/Desktop/Win22/cmput615/Project/ROI Detection/train_annotations/"
path="/home/sakib-hasan/Desktop/Win22/cmput615/Project/ROI Detection/test_annotations/"

trainXMLFiles=glob.glob(os.path.join(path, '*.xml'))
XML2JSON(trainXMLFiles)
