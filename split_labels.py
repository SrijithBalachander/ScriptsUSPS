import cv2
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
import math, os

file_name = "COA_test_cleaned1.csv"

new_file_name = "COA_test_cleaned1_split.csv"

dfs = pd.read_csv(file_name, delimiter = "\t", header = None)

datapath = "/data/HTR/COA/binarizedFieldImages/"

folder = "split_images_test"
if not os.path.exists(folder):
    os.mkdir(folder)

def split_image(img, label, path):
    labels = label.split(" ")
    if len(labels) <= 1:
        return
    # print(len(labels), labels)
    width = 30
    thresh = 1.0
    flg = 0
    cnt = 0
    img = img/255
    imgT = img.T
    cut_pos = []
    for i in range(int(imgT.shape[0]/width)):
        x, y = i*width, (i+1)*width

        # print("x | y", x, y)
        
        mean_val = np.mean(imgT[:imgT.shape[0]][x:y])
        
        # print("i | mean: ", i, mean_val)
        
        # if mean_val > thresh:
        if math.isclose(mean_val, thresh, rel_tol=0.00001):
            if flg == 1:
                continue
            flg = 1
            x1, y1 = x, y
            
            # print("yep")
        
        elif flg==1:
            cnt += 1
            cut_pos.append((x1,y1))
            flg = 0

    if cnt == len(labels)-1:
        img2 = imgT[:imgT.shape[0]][0:cut_pos[0][0]].T * 255
        # print(img2)
        # input()
        # cv2.imshow("a",img2)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # input()
        # num_split += 1
        cv2.imwrite(os.path.join(folder, path) + "_0" + ".png",img2)
        row = path + "_0.png" + '\t' + labels[0]
        file.write(row+'\n')
        # cv2.imshow(labels[0],img2)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        for i in range(1,len(labels)-1):
            img2 = imgT[:imgT.shape[0]][cut_pos[i-1][1]:cut_pos[i][0]].T * 255
            # cv2.imshow("a",img2)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # input()
            cv2.imwrite(os.path.join(folder, path) + "_" + str(i)+".png",img2)
            row = path + "_" + str(i)+".png" + '\t' + labels[i]
            file.write(row+'\n')

        img2 = imgT[:imgT.shape[0]][cut_pos[len(labels)-2][1]:].T * 255
        # cv2.imshow("a",img2)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # input("Input")
        cv2.imwrite(os.path.join(folder, path) + "_" + str(len(labels)-1)+".png",img2)
        row = path + "_" + str(len(labels)-1)+".png" + '\t' + labels[-1]
        file.write(row+'\n')
        # return 1
    # file.close()
    # return 0

    # print("cnt : ", cnt)
    # return cnt


if __name__ == '__main__':
    # num_split = 0
    with open(new_file_name, "w") as file:
        for path,label in zip(dfs[0],dfs[1]):
            if(os.path.exists(datapath+path)):
                img = cv2.imread(datapath+path,0)
                # print(img)
                split_image(img, label, path)
    # print("Number of files split = ", num_split)

    file.close()