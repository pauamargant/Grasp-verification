from pathlib import Path
import shutil
from tqdm import tqdm

negative_path = Path("/home/pmarg/data/negative/train_pbr")
negative_destination = Path("/home/pmarg/data/negative/imgs")
negative_destination.mkdir(parents=True, exist_ok=True)

# get all subdirectories in the negative_path called rgb. they can be inside other subdirectories
subdirs = [x for x in negative_path.rglob("rgb")]
for folder in subdirs:
    # get folder parent name
    parent = folder.parent.name
    # get all .png files in the folder
    files = list(folder.glob("*.png"))
    # append the parent name to the file name
    for file in tqdm(files, desc=f"Processing {parent}"):
        new_name = "neg_" + parent + "_" + file.name
        # move the file to the destination folder
        print("Moved", file, "to", negative_destination / new_name)
        # make sure the destination folder exists
        shutil.move(file, negative_destination / new_name)

# repeat for positive images
positive_path = Path("/home/pmarg/data/positive/train_pbr")
positive_destination = Path("/home/pmarg/data/positive/imgs")
positive_destination.mkdir(parents=True, exist_ok=True)

subdirs = [x for x in positive_path.rglob("rgb")]
for folder in subdirs:
    parent = folder.parent.name
    files = list(folder.glob("*.png"))
    for file in tqdm(files, desc=f"Processing {parent}"):
        new_name = "pos_" + parent + "_" + file.name
        print("Moved", file, "to", positive_destination / new_name)
        shutil.move(file, positive_destination / new_name)
        