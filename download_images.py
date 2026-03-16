
"""
小马宝莉角色图片下载脚本
使用方法：python download_images.py
"""

import requests
import os
from pathlib import Path

# 角色图片URL（使用更可靠的图片源）
CHARACTER_IMAGES = {
    'twilight.png': 'https://mlpforums.com/uploads/profile/photo-thumb-6953.png',
    'rainbow.png': 'https://mlpforums.com/uploads/profile/photo-thumb-6954.png',
    'applejack.png': 'https://mlpforums.com/uploads/profile/photo-thumb-6955.png',
    'rarity.png': 'https://mlpforums.com/uploads/profile/photo-thumb-6956.png',
    'fluttershy.png': 'https://mlpforums.com/uploads/profile/photo-thumb-6957.png',
    'pinkie.png': 'https://mlpforums.com/uploads/profile/photo-thumb-6958.png'
}

def download_image(url, filename):
    """下载单个图片"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"✓ 成功下载: {filename}")
        return True
    except Exception as e:
        print(f"✗ 下载失败 {filename}: {str(e)}")
        return False

def main():
    """主函数"""
    print("开始下载小马宝莉角色图片...")

    # 确保images目录存在
    images_dir = Path('images')
    images_dir.mkdir(exist_ok=True)

    # 下载所有图片
    success_count = 0
    for filename, url in CHARACTER_IMAGES.items():
        filepath = images_dir / filename
        if download_image(url, filepath):
            success_count += 1

    print(f"\n下载完成！成功: {success_count}/{len(CHARACTER_IMAGES)}")

    if success_count > 0:
        print("\n现在你可以打开 index_enhanced.html 查看效果了！")
    else:
        print("\n图片下载失败，请手动下载图片到 images 文件夹")

if __name__ == "__main__":
    main()
