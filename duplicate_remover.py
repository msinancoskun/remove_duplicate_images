import os
from PIL import Image
from PIL import ImageStat


# Where are the files?
which_path = 'Desktop'   # input("Where are the images that you want to remove duplicates???\n")
path = 'C:/Users/Sinan/{}'.format(which_path.title())


files = []
accepted_extension = ('jpeg', 'png', 'jpg')


# if image_file is a .jpg or .png append it to files.
for image_file in os.listdir(path):
    if image_file.endswith(accepted_extension):
        files.append(image_file)
        

# find means of images in files list.
means = []


try:
    for image in files:
        image_path = 'C:/Users/Sinan/' + which_path + '/' + image
        image_org = Image.open(image_path)
        pix_mean = ImageStat.Stat(image_org).mean
        means.append(pix_mean)
        for i in range(len(means) - 1):
            if means[i] == means[i + 1]:
                print('{} equals to {}'.format(means[i], means[i + 1]))
                means.remove(means[i + 1])
                files.remove(image)
                os.remove(image_path)

except FileNotFoundError:
    pass
