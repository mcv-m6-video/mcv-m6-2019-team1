
# Folder fnames
import utils as ut
import os
DIR= '../annotation_pascal'
xml_fname = '../datasets/AICity_data/train/S03/c010/Anotation_test.xml'
xml_fname2 = '../Anotation_testN.xml'
ut.folderPascal2xml(xml_fname,xml_fname2,DIR)
#file_list = []
#i = 0
#for file_name in os.listdir(DIR):
#    if file_name.endswith(".xml"):
#        file_list.append(os.path.join(DIR,file_name))
#        i +=1

#print file_list
#bboxes,pd_bboxes = ut.get_bboxes_from_pascal(file_list, 2)
#print('BBOX- DICT?')
#print(bboxes)
#print('BBOX- PD')
#print(pd_bboxes)
#xml_fname = '/home/noamor/Documents/repo/m6/datasets/AICity_data/train/S03/c010/Anotation_test.xml'
#xml_fname2 = '/home/noamor/Documents/repo/m6/datasets/AICity_data/train/S03/c010/Anotation_test3.xml'
#ut.add_track2xml(xml_fname,xml_fname2,pd_bboxes)

#ut.create_aicity_xml_file('trial_name.xml', pd_bboxes)
#boxes,pd.DataFrame(bboxes)get_bboxes_from_aicity(fnames)
