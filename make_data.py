import string
import pandas as pd
import os, re


def init_data_creation():
	file_name = "COA Full Truth.xlsx"

	dfs = pd.read_excel(file_name, sheet_name = "merged")

	dfs = dfs.apply(lambda s: s.fillna({i: "" for i in dfs.index}))			## removing NaNs



	print(dfs)
	print("Dataframe keys: ---> " + dfs.keys())

	x = list(string.ascii_lowercase)
	y = ['a', 'b']

	xy = [y1 + x1 for y1 in y for x1 in x]
	xy = x + xy

	ind = xy.index("bh")
	xy = xy[:ind]
	print("Columns letters: " + str(xy))

	dfs_cols = [x for x in dfs.keys()]
	xls_cols = dict(zip(xy, dfs_cols))

	print("Dictionary of column names : \n" + str(dfs_cols))

	dfs.columns = xy

	dict_req = {'o' : '7a_old_mailing_address', 'p' : '7b_old_apt', 'q' : '7c_old_city', 'r' : '7d_old_state', 's': '7e_old_zip', 'ag': '8a_new_mailing', 'ah' : '8b_new_apt', 'ai' : '8c_new_city', 'aj' : '8d_new_state', 'ak': '8e_new_zip', 'al' : '5a_lastname', 'am' : '5b_firstname'}

	# img_filenames = dfs['a']

	img_filenames = [st[5:]+'.tif' for st in dfs['a']]

	# xy = [y1 + x1 for y1 in y for x1 in x]

	data_file = open("COA_path_gt_cleaned.txt", "w")


	with open("COA_path_gt_cleaned.txt", "w") as file:
		for i in range(len(dfs)):
			for j in dict_req.keys():
				path = img_filenames[i]+'.'+dict_req[j]+'.png'
				if os.path.exists("/data/HTR/COA/binarizedFieldImages/"+path) and dfs.at[i,j]!="": #and not bool(re.search(r'\d',str(dfs.at[i,j]))):		#bool(re.search(r'\d', gt))
					if re.search(r'.0', str(dfs.at[i,j])):
						dfs.at[i,j] = str(dfs.at[i,j]).split('.')[0]
					# if type(dfs.at[i,j]) == float:
						# dfs.at[i,j] - int(dfs.at[i,j])
					row = path + '\t' + str(dfs.at[i,j])
					data_file.write(row+'\n')

	# for i in range(len(dfs)):
	# 	for j in dict_req.keys():
	# 		row = img_filenames[i]+'.'+dict_req[j]+'.png' + ' ' + str(dfs.at[i,j])
	# 		data_file.write(row)

	data_file.close()

def data_without_labels():
	file_name = "COA_test_cleaned1.csv"
	dfs = pd.read_csv(file_name,sep = '\t', header=None)
	new_file = "COA_test_paths_only.csv"
	with open(new_file,"w") as file:
		for x in dfs[0]:
			file.write(x+'\n')


if __name__ == "__main__":
	# data_without_labels()

	init_data_creation()

# for i in range(11):
# 	index = random.randrange(0, len(files))
# 	img = cv2.imread(os.path.join(path,files[index]),0)
# 	th, im_gray_th_otsu = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)
# 	print(files[index], th)
# 	cv2.imshow(files[index],im_gray_th_otsu)
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()


# for i in range(nSamples):
# 	imagePath, label = datalist[i].strip('\n').split(' ',1)
# 	imagePath, thresh = imagePath.split(',')
# 	print(imagePath, label, thresh)
# 	input("enter")
# 	img = cv2.imread(os.path.join(path,imagePath)+'.png',0)
# 	print(img)
# 	th, im_bin = cv2.threshold(img, int(thresh), 255, cv2.THRESH_BINARY)
# 	cv2.imshow("a",im_bin)
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()
# 	input("exit")