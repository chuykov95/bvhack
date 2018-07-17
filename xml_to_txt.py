import os
from xml.etree import ElementTree

xml_path = 'C:/Users/user/PycharmProjects/ssd300_bvh/test/Annotations/'  #путь к xml файлам
txt_path = 'C:/Users/user/PycharmProjects/ssd300_bvh/txt_rez/'

test_xml = []  # массив с именами всех xml в папке
test_xml = os.listdir(xml_path)
txt_list = []
file_boxes = []
# считываем файл разметки
filename = []
for g in test_xml:
    bounding_boxes = []  # массив координат
    tree = ElementTree.parse(xml_path + g)
    root = tree.getroot()
    for object_tree in root.findall('object'):
        for bounding_box in object_tree.iter('bndbox'):
            xmin_o = int(bounding_box.find('xmin').text)
            ymin_o = int(bounding_box.find('ymin').text)
            xmax_o = int(bounding_box.find('xmax').text)
            ymax_o = int(bounding_box.find('ymax').text)
        class_name = object_tree.find('name').text
        bounding_box = [class_name,'1.0', xmin_o, ymin_o, xmax_o-xmin_o, ymax_o-ymin_o] #если сохраняем файлы детектированных объектов
        #bounding_box = [class_name, xmin_o, ymin_o, xmax_o-xmin_o, ymax_o-ymin_o]      #если сохраняем файлы эталонных объектов
        image_name2 = root.find('filename').text
        bounding_boxes.append(bounding_box)
    image_name = root.find('filename').text
    text_name = g[:(len(g) - 4)]+'.txt'
    f = open(txt_path+text_name, 'w')
    for item in bounding_boxes:
        f.write("%s\n" % item)
    f.close()
    with open(txt_path+text_name) as file_in:
        text = file_in.read()

    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("'", "")
    text = text.replace(",", "")
    #сохраняем текстовые файлы для использования в скрипте pascalvoc.py
    with open(txt_path+text_name, "w") as file_out:  
        file_out.write(text)
