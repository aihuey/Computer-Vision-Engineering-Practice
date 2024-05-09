import os
import cv2
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity
from skimage.metrics import peak_signal_noise_ratio


def eval(clear_img_path, hazy_img_path):
    """
    该函数用于读取图像并计算去雾前后图像的PSNR与SSIM值。
    :param clear_img_path: 清晰图像路径
    :param hazy_img_path: 待去雾图像路径
    :return: None
    """
    # 读取清晰图像和待去雾图像
    clear_img = cv2.imread(clear_img_path)
    hazy_img = cv2.imread(hazy_img_path)

    print(clear_img.shape)
    print(hazy_img.shape)

    # 计算PSNR和SSIM值，PSNR越大表示图像质量越好，SSIM越大表示两图像越相似
    PSNR = peak_signal_noise_ratio(clear_img, hazy_img)
    print('PSNR: ', PSNR)
    SSIM = structural_similarity(clear_img, hazy_img, channel_axis=2)
    print('SSIM: ', SSIM)

if __name__ == '__main__':
    clear_img_dir = 'Set5'
    hazy_img_dir = 'Set5_0.25_x4'
    for filename in os.listdir(clear_img_dir):
        print(filename)
        clear_img_path = os.path.join(clear_img_dir, filename)
        hazy_img_path = os.path.join(hazy_img_dir, filename)
        eval(clear_img_path, hazy_img_path)
    print("评估完成！")
