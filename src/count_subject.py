import os
from utils.file import get_file_name, list_files


def count_subject(img_dir):
    print(img_dir)
    img_path_list, img_path_length = list_files(img_dir)
    subject_set = set()
    for img_path in img_path_list:
        # Image names are in the form SUBJECT_ACTIVITY_HAND_ENCOUNTER_TECHNIQUE_DIGITIZER_
        # RESOLUTION_DEPTH_CHANNELS_LPNUMBER_SOURCE.EXT
        # 00002302_1A_R_L01_BP_S04_1200PPI_8BPC_1CH_LP01_1
        name = get_file_name(img_path)
        name_split = name.split("_")
        subject = name_split[0]
        subject_set.add(subject)
    print("Number of subject:", len(subject_set))


if __name__ == "__main__":
    nist_sd302b_dir = (
        r"H:\Workspace\KSIP\02_Database\00_ORIGINAL\NIST_SD302\sd302b\images\baseline"
    )

    img_dir = os.path.join(nist_sd302b_dir, r"\R\500\slap-segmented\png")
    count_subject(img_dir)

    img_dir = os.path.join(nist_sd302b_dir, r"\S\500\slap-segmented\png")
    count_subject(img_dir)

    img_dir = os.path.join(nist_sd302b_dir, r"\U\500\roll\png")
    count_subject(img_dir)

    img_dir = os.path.join(nist_sd302b_dir, r"\V\500\roll\png")
    count_subject(img_dir)

    # Merge images from R and S devices.
    img_dir = os.path.join(nist_sd302b_dir, r"\R_S")
    count_subject(img_dir)

    # \R\500\slap-segmented\png
    # Number of subject: 92
    # \S\500\slap-segmented\png
    # Number of subject: 108
    # \U\500\roll\png
    # Number of subject: 200
    # \V\500\roll\png
    # Number of subject: 200
    # \R_S
    # Number of subject: 200
