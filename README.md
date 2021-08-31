# ScriptsUSPS
Some short scripts I used to handle USPS image data.

binarizer.py -- takes a text file with image locations and labels as input and extracts the image locations using pandas. Loads the images sequentially and binarizes them using OpenCV. Then saves the image and writes to new file.

cleaning_images.py -- loads the images from the locations given in the text file and streams them one after another to the user so the user can manually check the image and labels for correctness.

data_split.py -- splits the data into train,valid,test

make_data.py -- creates the data text file with image locations and labels from the excel sheet with various redundant columns and inputs.

split_labels.py -- splits the image (containing various words) into separate words using a threshold of blank space.
