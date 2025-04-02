import numpy as np
import matplotlib.pyplot as plt

def setup_parameters():
    """
    设置模拟牛顿环所需的参数
    
    返回:
    tuple: 包含激光波长(lambda_light,单位m)、透镜曲率半径(R_lens,单位m)的元组
    """
    # 氦氖激光波长 (m)
    lambda_light = 632.8e-9
    # 透镜曲率半径 (m)
    R_lens = 0.1
    return lambda_light, R_lens

def generate_grid():
    """
    生成模拟所需的网格坐标
    
    返回:
    tuple: 包含网格坐标X、Y以及径向距离r的元组
    """
    # 在此生成x和y方向的坐标网格
    x = np.linspace(-size, size, points)
    y = np.linspace(-size, size, points)
    X, Y = np.meshgrid(x, y)  # 创建二维网格
    r = np.sqrt(X**2 + Y**2)  # 计算每个点到中心的径向距离
    return X, Y, r

def calculate_intensity(r, lambda_light, R_lens):
    """
    计算干涉强度分布
    
    参数:
    r (np.ndarray): 径向距离数组
    lambda_light (float): 激光波长(m)
    R_lens (float): 透镜曲率半径(m)
    
    返回:
    np.ndarray: 干涉强度分布数组
    """
    # 在此实现光强计算
    # 计算空气薄膜厚度d = R - √(R² - r²)
    d = R_lens - np.sqrt(R_lens**2 - r**2)
    # 计算光强分布 I = 4sin²(2πd/λ)
    intensity = 4 * np.sin(2 * np.pi * d / lambda_light)**2
    return intensity

def plot_newton_rings(intensity):
    """
    绘制牛顿环干涉条纹图像
    
    参数:
    intensity (np.ndarray): 干涉强度分布数组
    """
    # 在此实现图像绘制
    plt.figure(figsize=(8, 8))
    plt.imshow(intensity, cmap=cmap, extent=[-2, 2, -2, 2])  # 显示范围为±2mm
    plt.colorbar(label='光强强度')
    plt.title("牛顿环干涉图样")
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.axis('on')
    plt.show()

if __name__ == "__main__":
    # 1. 设置参数
    lambda_light, R_lens = setup_parameters()
    
    # 2. 生成网格坐标
    X, Y, r = generate_grid()
    
    # 3. 计算干涉强度分布
    intensity = calculate_intensity(r, lambda_light, R_lens)
    
    # 4. 绘制牛顿环
    plot_newton_rings(intensity)
