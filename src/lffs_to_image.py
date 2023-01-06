import os
import io
import PIL.Image as Image
from utils.file import list_files, make_dirs, get_file_name


def lffs_to_image(lffs_dir, img_dir):
    make_dirs(img_dir)
    path_list, length = list_files(lffs_dir)

    for i, path in enumerate(path_list):
        print(i, path)
        name = get_file_name(path)
        out_path = os.path.join(img_dir, '%s.jpg' % name)
        with open(path, mode='rb') as file:
            content = file.read()
            content_split = content.split(b'13.999')
            content_split = content_split[1][1:].split(b'IEND')
            img_byte = content_split[0]
            image = Image.open(io.BytesIO(img_byte))
            image.save(out_path)


if __name__ == '__main__':
    lffs_dir = r'H:\Workspace\KSIP\02_Database\00_ORIGINAL\NIST_SD302\sd302h\ebts\latent\lffs\original\1000'
    out_dir = r'H:\Workspace\KSIP\02_Database\00_ORIGINAL\NIST_SD302\sd302h\png\latent\lffs\original\1000'
    lffs_to_image(lffs_dir, out_dir)
