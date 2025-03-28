from PIL import Image
import os
import shutil
from PyPDF2 import PdfMerger


def images2pdf(root_path, image_paths, output_path):
    image_paths.sort(key=lambda x: int(x.strip('第页.jpg')))
    # print(image_paths)
    images = [Image.open(root_path + image).convert('RGB') for image in image_paths]
    images[0].save(root_path + output_path, save_all=True, append_images=images[1:])
    print(f"已将{len(image_paths)}张图片合并为 PDF 文件 {output_path}")


def replace_in_filenames(directory, old_str, new_str):
    for filename in os.listdir(directory):
        if old_str in filename:
            new_filename = filename.replace(old_str, new_str)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


def main():
    for i in range(1, 42):
        string = str(i).zfill(2)
        root_path = "C:\\Users\\24335\\Desktop\\葬送的芙莉莲\\第" + string + "话\\"
        paths = os.listdir("C:\\Users\\24335\\Desktop\\葬送的芙莉莲\\第" + string + "话\\")
        images2pdf(root_path, paths, f'第{i}话.pdf')


def move():
    for i in range(43, 141):
        string = str(i).zfill(2)
        root_path = "C:\\Users\\24335\\Desktop\\葬送的芙莉莲\\第" + string + "话\\"
        new_path = "C:\\Users\\24335\\Desktop\\葬送的芙莉莲\\"
        shutil.copy(root_path + f'第{i}话.pdf', new_path)


def merge():
    pdf_merger = PdfMerger()
    for i in range(1, 141):
        if i == 42:
            continue
        file = f"C:\\Users\\24335\\Desktop\\葬送的芙莉莲\\第{i}话.pdf"
        pdf_merger.append(file)
    f = open('C:\\Users\\24335\\Desktop\\葬送的芙莉莲.pdf', 'wb')
    pdf_merger.write(f)


merge()
