import os
import shutil
import img_segmentation


TRAIN_PATH = 'DATASET/treino'
TEST_PATH_HW = 'DATASET/teste/highway'
TEST_PATH_UFES = 'DATASET/teste/ufes'

def main():
    total_classes = 0
    for diretorio, subpastas, arquivos in os.walk(TRAIN_PATH):
        for subpasta in subpastas:
            print(subpasta, " está sendo analisada...")
            print(subpasta+'/masks/i'+subpasta+'.png')
            if subpasta != 'images' and subpasta!= 'masks':
                n_classes = img_segmentation.create_masks(TRAIN_PATH+'/'+subpasta, subpasta)
                if(n_classes>total_classes):
                    total_classes = n_classes

            
                
    print('concluído! total de classes: ', n_classes)
    
main()