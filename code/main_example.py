'''Module 3: count black and white pixels and compute the percentage of white pixels in a .jpg image and extrapolate points'''

from termcolor import colored
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import pandas as pd

# Load the images you want to analyze

filenames = [
    r"/Users/gracelee/Documents/computational BME/horn_lee_Module-3-Fibrosis/6 images/MASK_SK658 Slobe ch010089.jpg",
    r"/Users/gracelee/Documents/computational BME/horn_lee_Module-3-Fibrosis/6 images/MASK_SK658 Slobe ch010092.jpg",
    r"/Users/gracelee/Documents/computational BME/horn_lee_Module-3-Fibrosis/6 images/MASK_SK658 Slobe ch010098.jpg",
    r"/Users/gracelee/Documents/computational BME/horn_lee_Module-3-Fibrosis/6 images/MASK_SK658 Slobe ch010105.jpg",
    r"/Users/gracelee/Documents/computational BME/horn_lee_Module-3-Fibrosis/6 images/MASK_SK658 Slobe ch010114.jpg",
    r"/Users/gracelee/Documents/computational BME/horn_lee_Module-3-Fibrosis/6 images/MASK_SK658 Slobe ch010118.jpg",
]

# Enter the depth of each image (in the same order that the images are listed above; you can find these in the .csv file provided to you which is tilted: "Filenames and Depths for Students")

depths = [
    10000,
    10000,
    10000,
    8100,
    9900,
    9900
]

# Make the lists that will be used

white_counts = []
black_counts = []
white_percents = []

print(colored("Counts of pixel by color in each image", "yellow"))

# Build the list of all the images you are analyzing

for i, (filename, depth) in enumerate(zip(filenames, depths)):
    img = cv2.imread(filename, 0)

    #Make the image greyscale
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


    total = binary.size
    white = int(np.sum(binary == 255))
    black = total - white

    white_pct = 100 * white/total

    white_counts.append(white)
    black_counts.append(black)
    white_percents.append(white_pct)

    print(colored(f"White pixels in image {i}: {white}", "white"))
    print(colored(f"Black pixels in image {i}: {black}", "black"))
    print()

print(colored("Percent white px:", "yellow"))

for i, (filename, depth) in enumerate(zip(filenames, depths)):
    
    print(colored(f'{filenames[i]}:', "red"))
    print(f'{white_percents[i]}% White | Depth: {depths[i]} microns')
    print()

'''Write your data to a .csv file'''

# Create a DataFrame that includes the filenames, depths, and percentage of white pixels
df = pd.DataFrame({
    'Filenames': filenames,
    'Depths': depths,
    'White percents': white_percents
})

# Write that DataFrame to a .csv file

df.to_csv('Percent_White_Pixels.csv', index=False)

print("The .csv file 'Percent_White_Pixels.csv' has been created.")

'''the .csv writing subroutine ends here'''


##############
# LECTURE 2: UNCOMMENT BELOW

# # Interpolate a point: given a depth, find the corresponding white pixel percentage

# interpolate_depth = float(input(colored(
#     "Enter the depth at which you want to interpolate a point (in microns): ", "yellow")))

# x = depths
# y = white_percents

# # You can also use 'quadratic', 'cubic', etc.
# i = interp1d(x, y, kind='linear')
# interpolate_point = i(interpolate_depth)
# print(colored(
#     f'The interpolated point is at the x-coordinate {interpolate_depth} and y-coordinate {interpolate_point}.', "green"))

# depths_i = depths[:]
# depths_i.append(interpolate_depth)
# white_percents_i = white_percents[:]
# white_percents_i.append(interpolate_point)


# # make two plots: one that doesn't contain the interpolated point, just the data calculated from your images, and one that also contains the interpolated point (shown in red)
# fig, axs = plt.subplots(2, 1)

# axs[0].scatter(depths, white_percents, marker='o', linestyle='-', color='blue')
# axs[0].set_title('Plot of depth of image vs percentage white pixels')
# axs[0].set_xlabel('depth of image (in microns)')
# axs[0].set_ylabel('white pixels as a percentage of total pixels')
# axs[0].grid(True)


# axs[1].scatter(depths_i, white_percents_i, marker='o',
#                linestyle='-', color='blue')
# axs[1].set_title(
#     'Plot of depth of image vs percentage white pixels with interpolated point (in red)')
# axs[1].set_xlabel('depth of image (in microns)')
# axs[1].set_ylabel('white pixels as a percentage of total pixels')
# axs[1].grid(True)
# axs[1].scatter(depths_i[len(depths_i)-1], white_percents_i[len(white_percents_i)-1],
#                color='red', s=100, label='Highlighted point')


# # Adjust layout to prevent overlap
# plt.tight_layout()
# plt.show()
