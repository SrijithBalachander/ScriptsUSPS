import numpy as np
import os, cv2
import pandas as pd
import matplotlib.pyplot as plt

data_folder = "binarizedFieldImages/"
new_folder = "binarizedFieldImagesCleaned/"
parentDir = "/data/HTR/COA/"

# file = "COA_path_gt_cleaned.txt"
file = "COA_test_cleaned1.csv"

dfs = pd.read_csv(file,sep="\t", header = None)

img_files = [x for x in dfs[0]]

def top_clean():
	if not os.path.exists(os.path.join(parentDir,new_folder)):
		os.mkdir(os.path.join(parentDir,new_folder))

	for imgFile in img_files: 	#os.listdir(os.path.join(parentDir,data_folder)):
		img = cv2.imread(os.path.join(parentDir,data_folder)+imgFile,0)
		for i in range(25):
			if any(img[i])!=255:
				img[i] = 255
			else:
				break
		cv2.imwrite(os.path.join(parentDir,new_folder)+imgFile,img)

	# for i in range(len(df)):
	# 	x = df.at()[i,0]
	# 	y = df.at()[i,1]
	# 	if "fairfax" in y.lower():
	# 		img = cv2.imread(os.path.join(data,x),0)
	# 		cv2.imshow(x,img)
	# 		cv2.waitKey(0)
	# 		cv2.destroyAllWindows()

def clean_gt(start=0):
	for i,x in enumerate(dfs[0]):
		if i < start:
			continue;

		img = cv2.imread(os.path.join(parentDir,data_folder)+x,0)
		print(i)
		cv2.imshow(str(x),img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

if __name__ == '__main__':
	clean_gt()