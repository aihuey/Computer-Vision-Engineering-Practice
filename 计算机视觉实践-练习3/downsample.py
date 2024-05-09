import os  
from PIL import Image  
  
def downsample_image_bicubic(input_image_path, output_image_path, scale_factor):  
    """  
    使用bicubic插值对图片进行下采样  
      
    :param input_image_path: 输入图片路径  
    :param output_image_path: 输出图片路径  
    :param scale_factor: 下采样比例（例如，0.5表示减半）  
    """  
    original_image = Image.open(input_image_path)  
    width, height = original_image.size  
    new_width = int(width * scale_factor)  
    new_height = int(height * scale_factor)  
    downsampled_image = original_image.resize((new_width, new_height), Image.BICUBIC)  
    downsampled_image.save(output_image_path)  

if __name__ == '__main__':
    # 设置Set5文件夹的路径和输出文件夹的路径  
    set5_folder = 'Set5'
    output_folder = 'Set5_0.25'
    if not os.path.exists(output_folder):  
        os.makedirs(output_folder)  
    
    # 遍历Set5文件夹中的所有图片，并进行下采样  
    scale_factor = 0.25   
    for filename in os.listdir(set5_folder):  
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):  
            input_image_path = os.path.join(set5_folder, filename)  
            base, ext = os.path.splitext(filename)  
            output_image_path = os.path.join(output_folder, f"{base}{ext}")  
            downsample_image_bicubic(input_image_path, output_image_path, scale_factor)  
    
    print("处理完成！")