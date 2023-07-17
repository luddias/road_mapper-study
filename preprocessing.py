import os
import shutil

DATA_PATH = 'UFES_DATASET'
DATASET_PATH = 'DATASET'
TRAIN_PATH = 'DATASET/treino'
TEST_PATH = 'DATASET/teste'
DATASET_TEST = 'HIGHWAY/guarapari'
TEST_PATH_HW = 'DATASET/teste/highway'
TEST_PATH_UFES = 'DATASET/teste/ufes'


OLD_ADD = '/home/lume/Documents/ludmila-study/Segmentação-Semântica/'
NEW_ADD = '/home/lume/Documents/ludmila-study/Segmentação-Semântica/DATASET/'

path_name = ''
id_data = ''
subpasta = ''
i=0
test_files = 9776
dir=''


# for diretorio, subpastas, arquivos in os.walk(DATASET_TEST):
#     for arquivo in arquivos:
#         path_name = arquivo.replace('.png', '')
#         id_data = list(path_name)[0]
#         path_name = path_name.replace(id_data, '')
#         try:
#             os.mkdir('DATASET/teste/'+ path_name)
#             os.mkdir('DATASET/teste/'+ path_name + '/images')
#             os.mkdir('DATASET/teste/'+ path_name + '/masks')
#         except:
#             print("erro")
#             print(path_name)
# print('concluído')
            
            
            

# for diretorio, subpastas, arquivos in os.walk(DATASET_TEST):
#     for arquivo in arquivos:
#         path_name = arquivo.replace('.png', '')
#         id_data = list(path_name)[0]
#         path_name = path_name.replace(id_data, '')
#         print(path_name, id_data)
#         dir = diretorio[:-9]
#         if id_data == 'i':
#             shutil.move(OLD_ADD+diretorio+'/'+arquivo, NEW_ADD+path_name+"/images/"+arquivo)
#         elif id_data == 'r':
#             shutil.move(OLD_ADD+diretorio+'/'+arquivo, NEW_ADD+path_name+"/masks/"+arquivo)
# print('concluído')

# cont = 0
# list_dir = os.listdir('DATASET2/masks/ufes')
# # print(list_dir)
# quant = len(list_dir)
# print(quant, len(os.listdir('DATASET2/masks')))
# for i in range(quant):
#     arquivo = list_dir[i]
#     path_name = arquivo.replace('.png', '')
#     id_data = list(path_name)[0]
#     path_name = path_name.replace(id_data, '')
#     print(path_name, id_data)
#     # dir = diretorio[:-9]
#     # if id_data == 'i':
#     if os.path.isfile(OLD_ADD+'DATASET2/masks/ufes/'+arquivo) and (os.path.isfile(NEW_ADD+'treino/' +path_name+"/masks/"+arquivo) or os.path.isfile(NEW_ADD+'teste/ufes/' +path_name+"/masks/"+arquivo)):
#         try:
#             shutil.move(OLD_ADD+'DATASET2/masks/ufes/'+arquivo, NEW_ADD+'treino/' +path_name+"/masks/"+arquivo)
#             print('ok')
#         except:
#             shutil.move(OLD_ADD+'DATASET2/masks/ufes/'+arquivo, NEW_ADD+'teste/ufes/' +path_name+"/masks/"+arquivo)
#     else:
#         print(list_dir[i], i)
#         cont+=1
#         print(cont)
    
# # elif id_data == 'r':
# #     shutil.move(OLD_ADD+diretorio+'/'+arquivo, NEW_ADD+path_name+"/masks/"+arquivo)
# print('concluído')

# RESOLVER PROBLEMA NA TRANSFERÊNCIA DOS ARQUIVOS PRAS SUAS RESPECTIVAS PASTAS!

# try:
#     os.mkdir('DATASET/treino')
#     os.mkdir('DATASET/teste')
# except:
#     pass

# for diretorio, subpastas, arquivos in os.walk(DATASET_PATH):
#     for subpasta in subpastas:
#         if subpasta != 'treino' and subpasta!= 'teste':
#             if i<test_files:
#                 shutil.move( NEW_ADD+subpasta, NEW_ADD+'teste/'+subpasta)
#             else:
#                 shutil.move( NEW_ADD+subpasta, NEW_ADD+'treino/'+subpasta)

#             i+=1
#         if subpasta != 'treino' and subpasta!= 'teste':
#             shutil.move( NEW_ADD+subpasta, NEW_ADD+'treino/'+subpasta)       


print( 'carregando...')
for diretorio, subpastas, arquivos in os.walk(TEST_PATH_UFES):
    for subpasta in subpastas:
        
        if subpasta != 'treino' and subpasta!= 'teste' and subpasta!= 'images' and subpasta!= 'masks':
            try:
                os.rename( OLD_ADD+'DATASET/teste/ufes/'+subpasta+'/'+'r'+subpasta+'.png',  OLD_ADD+'DATASET/teste/ufes/'+subpasta+'/masks/'+'r'+subpasta+'.png')
            except:
                continue
        # if subpasta != 'treino' and subpasta!= 'teste' and subpasta!= 'images' and subpasta!= 'masks':
        #     dir = os.listdir(TRAIN_PATH+'/'+subpasta)
        #     quant = len(dir)
        #     for i in range(quant):
        #         if dir[i]!='r'+subpasta+'.png':  
                    # if subpasta != 'treino' and subpasta!= 'teste' and subpasta!= 'images' and subpasta!= 'masks':
print( 'conc')                       


# os.mkdir('DATASET2/masks/ufes')


# for diretorio, subpastas, arquivos in os.walk('DATASET2/masks/ufes'):
#     for arquivo in arquivos:
#         # if subpasta != 'images' and subpasta!= 'masks':
#         # quant = len(os.listdir('DATASET2/masks/ufes'))
#         # for i in range(quant-1):
#         # if os.listdir(TRAIN_PATH+'/'+subpasta + "/masks")[i]=='r'+subpasta+'.png':
#         end = os.listdir(TRAIN_PATH+'/'+subpasta + "/masks")[i]
#         shutil.move(OLD_ADD+'DATASET2/masks/ufes/'+end, OLD_ADD+TRAIN_PATH+'/'+subpasta + "/masks/"+ end)  
# print('concluído')              

# for diretorio, subpastas, arquivos in os.walk(TRAIN_PATH):
#     print('carregando...')
#     for subpasta in subpastas:
#         if len(os.listdir(TRAIN_PATH)) > 15000:
#             shutil.move(NEW_ADD+"treino/"+subpasta, '/home/lume/Documents/ludmila-study/Segmentação-Semântica/DATASET2/'+subpasta)
            
# print('concluido!')


# try:
#     os.mkdir('DATASET/teste/highway')
#     os.mkdir('DATASET/teste/ufes')
# except:
#     pass

# for diretorio, subpastas, arquivos in os.walk(DATASET_PATH+"/teste"):
#     for subpasta in subpastas:
#         if subpasta != 'images' and subpasta!= 'masks' and subpasta!= 'ufes' and subpasta!= 'highway':
#             path_name = subpasta[:4]
#             if(int(path_name)>7740):
#                 shutil.move( NEW_ADD+subpasta, NEW_ADD+'ufes/'+subpasta)
#             elif(int(path_name)<7740):
#                 shutil.move( NEW_ADD+subpasta,NEW_ADD+'highway/'+subpasta)
#         if subpasta != 'treino' and subpasta!= 'teste':
#             if i<test_files:
#                 shutil.move( NEW_ADD+subpasta, NEW_ADD+'teste/'+subpasta)
#             else:
#                 shutil.move( NEW_ADD+subpasta, NEW_ADD+'treino/'+subpasta)

#             i+=1
#         if subpasta != 'treino' and subpasta!= 'teste':
#             shutil.move( NEW_ADD+subpasta, NEW_ADD+'treino/'+subpasta)       
