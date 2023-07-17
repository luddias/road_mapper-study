import numpy as np
import cv2

def add_classes_list(list, value, pixel):
    l = []
    if len(list)==0:
        list[value] = [pixel]
        return
    for id in list:
        if id==value:
            l = list[id]
            l.append(pixel)
            list[id] = l
            # list[id] = list[id].append(pixel)
            return
    list[value] = [pixel]
    return
    
def generate_mask(list, img, path_mask):
    n_class = 0
    for item in list:
        n_class+=1
        change_colors(list[item], img, n_class, path_mask)

def change_colors(list_pixel, img, n_class, path_mask):  
    altura,largura = img.shape[:2]    
    for y in range(0, altura):
        for x in range(0, largura):
            img[x,y] = (0,0,0)
    for pixel in list_pixel:
        img[pixel[0], pixel[1]] = (255, 255, 255)
    title = path_mask+str(n_class)+'.png'
    cv2.imwrite(title, img)
    return
        
        
def showImage(img):
    from matplotlib import pyplot as plt
    plt.imshow(img)
    plt.show()
    
def create_masks(path_name, file_name):
    img_name = path_name+'/masks/r'+file_name+'.png'
    path_mask = path_name+'/masks/r'+file_name
    classes = {}
    obj_img = cv2.imread(img_name, 0)
    obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
    # print("Altura (height): %d pixels" % (obj_img.shape[0]))
    # print("Largura (width): %d pixels" % (obj_img.shape[1]))
    # print("Canais (channels): %d"      % (obj_img.shape[2]))
    altura, largura, canais = obj_img.shape
    
    for y in range(0, altura):
        for x in range(0, largura):
            azul = obj_img.item(y,x,0)
            verde = obj_img.item(y,x,1)
            verm = obj_img.item(y,x,2)
            
            # print(azul, verde, verm, x, y)
            add_classes_list(classes, azul, (x,y))
            
    # print(classes, len(classes))
    generate_mask(classes, obj_img, path_mask)
    # showImage(obj_img)
    return len(classes)
    