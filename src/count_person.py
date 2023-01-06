import os
from utils.file import get_file_name, list_files


def count_preson(img_dir):
    print(img_dir)
    img_path_list, img_path_length = list_files(img_dir)
    subject_set = set()
    for img_path in img_path_list:
        # Image names are in the form SUBJECT_ACTIVITY_HAND_ENCOUNTER_TECHNIQUE_DIGITIZER_
        # RESOLUTION_DEPTH_CHANNELS_LPNUMBER_SOURCE.EXT
        # 00002302_1A_R_L01_BP_S04_1200PPI_8BPC_1CH_LP01_1

        name = get_file_name(img_path)
        name_split = name.split('_')
        subject = name_split[0]
        subject_set.add(subject)
    print("Number of subject:", len(subject_set))


if __name__ == "__main__":
    db_dir = r"D:\OneDrive\workspace\KSIP\02_Database\00_ORIGINAL_IMAGE"
    img_dir = os.path.join(db_dir, "NIST_SD302e_resized")
    count_preson(img_dir)

    img_dir = r"H:\Workspace\KSIP\02_Database\00_ORIGINAL\NIST_SD302\sd302b\images\baseline\R\500\slap-segmented\png"
    count_preson(img_dir)

    img_dir = r"H:\Workspace\KSIP\02_Database\00_ORIGINAL\NIST_SD302\sd302b\images\baseline\S\500\slap-segmented\png"
    count_preson(img_dir)

    img_dir = r"H:\Workspace\KSIP\02_Database\00_ORIGINAL\NIST_SD302\sd302b\images\baseline\U\500\roll\png"
    count_preson(img_dir)

    img_dir = r"H:\Workspace\KSIP\02_Database\00_ORIGINAL\NIST_SD302\sd302b\images\baseline\V\500\roll\png"
    count_preson(img_dir)

    img_dir = r"H:\Workspace\KSIP\02_Database\00_ORIGINAL\NIST_SD302\sd302b\images\baseline\R_S"
    count_preson(img_dir)
