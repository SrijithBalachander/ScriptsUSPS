import numpy as np
import cv2
import os
import pandas as pd

# path = "/data/HTR/Convolve_Attend_Spell_dataset/words/"
# iam_train = "/data/HTR/Convolve_Attend_Spell_dataset/RWTH.iam_word_gt_final.train.thresh"
# iam_test = "/data/HTR/Convolve_Attend_Spell_dataset/RWTH.iam_word_gt_final.test.thresh"
# iam_valid = "/data/HTR/Convolve_Attend_Spell_dataset/RWTH.iam_word_gt_final.valid.thresh"

# new_dir = "/data/HTR/IAM_binarized/"

path = "/data/HTR/Convolve_Attend_Spell_dataset/lines/"
iam_train = "/data/HTR/Convolve_Attend_Spell_dataset/RWTH.iam_line_gt_final.train.thresh"
iam_test = "/data/HTR/Convolve_Attend_Spell_dataset/RWTH.iam_line_gt_final.test.thresh"
iam_valid = "/data/HTR/Convolve_Attend_Spell_dataset/RWTH.iam_line_gt_final.valid.thresh"

new_dir = "/data/HTR/IAM_binarized_lines/"

if not os.path.exists(new_dir):
	os.mkdir(new_dir)

with open(iam_train, 'r', encoding='utf-8') as data:
	datalist = data.readlines()

with open("iam_bin_lines_train.csv",'w') as file:
	nSamples = len(datalist)
	for i in range(nSamples):
		imagePath, label = datalist[i].strip('\n').split(' ',1) # imagePath, label_ = datalist[i].strip('\n').split(',',1)      
		# imagePath = os.path.join(inputPath, imagePath) # + ".png"      ## commented for USPS data
		# label_, label = datalist[i].strip('\n').split(' ',1)          ## commented for USPS data
		imagePath, thresh = imagePath.split(',')
		img = cv2.imread(os.path.join(path,imagePath)+'.png',0)
		th, im_bin = cv2.threshold(img, int(thresh), 255, cv2.THRESH_BINARY)
		cv2.imwrite(os.path.join(new_dir,imagePath)+'.png', im_bin)
		file.write(imagePath+'.png'+'\t'+label+'\n')

print("Writing Train files and images done")


with open(iam_test, 'r', encoding='utf-8') as data:
	datalist = data.readlines()

with open("iam_bin_lines_test.csv",'w') as file:
	nSamples = len(datalist)
	for i in range(nSamples):
		imagePath, label = datalist[i].strip('\n').split(' ',1) # imagePath, label_ = datalist[i].strip('\n').split(',',1)      
		# imagePath = os.path.join(inputPath, imagePath) # + ".png"      ## commented for USPS data
		# label_, label = datalist[i].strip('\n').split(' ',1)          ## commented for USPS data
		imagePath, thresh = imagePath.split(',')
		img = cv2.imread(os.path.join(path,imagePath)+'.png',0)
		th, im_bin = cv2.threshold(img, int(thresh), 255, cv2.THRESH_BINARY)
		cv2.imwrite(os.path.join(new_dir,imagePath)+'.png', im_bin)
		file.write(imagePath+'.png'+'\t'+label+'\n')

print("Writing Test files and images done")

with open(iam_valid, 'r', encoding='utf-8') as data:
	datalist = data.readlines()

with open("iam_bin_lines_valid.csv",'w') as file:
	nSamples = len(datalist)
	for i in range(nSamples):
		imagePath, label = datalist[i].strip('\n').split(' ',1) # imagePath, label_ = datalist[i].strip('\n').split(',',1)      
		# imagePath = os.path.join(inputPath, imagePath) # + ".png"      ## commented for USPS data
		# label_, label = datalist[i].strip('\n').split(' ',1)          ## commented for USPS data
		imagePath, thresh = imagePath.split(',')
		img = cv2.imread(os.path.join(path,imagePath)+'.png',0)
		th, im_bin = cv2.threshold(img, int(thresh), 255, cv2.THRESH_BINARY)
		cv2.imwrite(os.path.join(new_dir,imagePath)+'.png', im_bin)
		file.write(imagePath+'.png'+'\t'+label+'\n')

print("Writing Valid files and images done")

# dfs_train = pd.read_csv()
# for files in os.listdir(path):
# 	img = cv2.imread(os.path.join(path,files),0)
# 	th, im_gray_th_otsu = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
# 	cv2.imwrite('data/dst/opencv_th_otsu.jpg', im_gray_th_otsu)
