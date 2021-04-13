import Augmentor
import os
import glob

currdir = os.path.abspath(os.curdir)

try:  # Create dirs if not exist
    if not os.path.exists('augmentated_images'):
        os.makedirs('augmentated_images')
    if not os.path.exists('augmentated_images\\images'):
        os.makedirs('augmentated_images\\images')
    if not os.path.exists('augmentated_images\\masks'):
        os.makedirs('augmentated_images\\masks')
except OSError:
    print('Error: Creating directory failed')

p = Augmentor.Pipeline(currdir + "\\images",
                       output_directory=currdir + "\\augmentated_images")
p.ground_truth(currdir + "\\masks")

# Augmentation options
p.zoom_random(probability=0.5, percentage_area=0.8)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)

p.process()  # apply pipeline for every picture

for filepath in glob.iglob(currdir + "\\augmentated_images\\*.png"):  # Sort masks and images from each other
    filename = filepath.split('\\')[-1]
    filename = filename.split(".png")[0] + ".png"  # Change filename
    try:
        if "images_original" in filename:
            filename = filename.replace("images_original_", "")   # Change filename
            os.replace(filepath, currdir + "\\augmentated_images\\images\\" + filename)  # Change file dir
        elif "_groundtruth_" in filename:
            filename = filename.replace("_groundtruth_(1)_images_", "")   # Change filename
            os.replace(filepath, currdir + "\\augmentated_images\\masks\\" + filename)  # Change file dir
    except:
        print("something went wrong...")


