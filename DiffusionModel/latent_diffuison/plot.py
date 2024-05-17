import matplotlib.pyplot as plt
import numpy as np

import torch

import cv2

# # 指定图片文件的路径
# image_path = 'AHNU.jpg'  # 请将此路径替换为您图片的实际路径
#
# # 使用OpenCV读取图片
# image= cv2.imread(image_path)
#
# # OpenCV默认以BGR格式读取图片，如果需要以RGB格式显示，需要转换颜色空间
# data = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # 使用matplotlib显示图片
# import matplotlib.pyplot as plt
# plt.imshow(data)
# plt.axis('off')  # 不显示坐标轴
# plt.show()

# # 如果需要获取图片的尺寸等信息
# print("图片尺寸:", image.shape[1], image.shape[0])  # 返回宽度和高度
# print("图片通道数:", image.shape[2])  # 图片的色彩通道数
# # 构建数据集
from PIL import Image
import numpy as np

# 打开图像文件
image = Image.open('AHNU.jpg')

# 将图像转换为numpy数组
data = np.array(image)
# 使用matplotlib显示图片
import matplotlib.pyplot as plt
plt.imshow(data)
plt.axis('off')  # 不显示坐标轴
plt.show()

#确定超参数的值
num_steps = 1000
#制定每一步的beta，beta按照时间从小到大变化
betas = torch.linspace(-6,6,num_steps)  # 使用linespace指定bata的值，也可以用其他方法
betas = torch.sigmoid(betas)*(0.5e-2 - 1e-5)+1e-5
alphas = 1-betas
alphas_prod = torch.cumprod(alphas,0)
alphas_bar_sqrt = torch.sqrt(alphas_prod)
one_minus_alphas_bar_log = torch.log(1 - alphas_prod)
one_minus_alphas_bar_sqrt = torch.sqrt(1 - alphas_prod)

blue = data[:,:,0]
green = data[:,:,1]
red =  data[:,:,2]

def q_x(x_0 , t):
    """可以基于x[0]得到任意时刻t的x[t]"""
    #生成正态分布采样
    noise = np.random.randn(*x_0.shape)
    #得到均值方差，根据时间步选择alphas_bar_sqrt值和one_minus_alphas_bar_sqrt值
    alphas_t = alphas_bar_sqrt[t]
    alphas_1_m_t = one_minus_alphas_bar_sqrt[t]
    #根据x0求xt
    return (alphas_t * x_0 + alphas_1_m_t * noise)  # 在x[0]的基础上添加噪声

new_blue = np.asarray(q_x(blue,999))
new_green = np.asarray(q_x(green,999))
new_red = np.asarray(q_x(red,999))


new_data =np.empty(data.shape)
new_data[:,:,0] = new_blue
new_data[:,:,1] = new_green
new_data[:,:,2] = new_red
# processed_image_bgr = cv2.cvtColor(processed_image_bgr, cv2.COLOR_RGB2BGR)
# 显示原始图像和处理后的图像
array =new_data.astype(np.uint8)

# 使用Pillow的Image.fromarray()方法将NumPy数组转换为图像
image_2 = Image.fromarray(array)

image.show()
image_2.show()
# 等待用户按键然后关闭所有窗口


