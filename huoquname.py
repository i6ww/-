import os
import sys

def get_filenames(folder_path):
    """获取文件夹内所有文件名（排除子目录）"""
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def create_output_filename(folder_path):
    """生成输出文件名，处理文件覆盖问题"""
    base_name = os.path.basename(folder_path.rstrip(os.sep))
    output_path = os.path.join(folder_path, f"{base_name}.txt")
    counter = 1
    
    while os.path.exists(output_path):
        output_path = os.path.join(folder_path, f"{base_name}_{counter}.txt")
        counter += 1
    return output_path

if __name__ == "__main__":
    # 交互式获取文件夹路径
    folder = input("请输入目标文件夹路径：").strip()
    while not os.path.isdir(folder):
        print(f"错误: 文件夹不存在 - {folder}")
        folder = input("请重新输入有效的目标文件夹路径：").strip()

    try:
        # 获取并排序文件名
        files = sorted(get_filenames(folder))
        output_path = create_output_filename(folder)

        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(files))
        
        print(f"\n成功生成文件列表：{os.path.basename(output_path)}")
        print(f"共找到 {len(files)} 个文件")

    except Exception as e:
        print(f"\n操作失败：{str(e)}")
        sys.exit(1)