import os
import sys

def read_titles(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def rename_files(folder_path, titles):
    files = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    
    if len(files) != len(titles):
        print(f"错误：文件数量({len(files)})与标题数量({len(titles)})不匹配")
        return False

    for i, (old_name, new_name) in enumerate(zip(files, titles)):
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        
        # 处理文件覆盖问题
        counter = 1
        while os.path.exists(new_path):
            base, ext = os.path.splitext(new_name)
            new_path = os.path.join(folder_path, f"{base}_{counter}{ext}")
            counter += 1

        try:
            os.rename(old_path, new_path)
            print(f"[{i+1}/{len(files)}] 重命名成功: {old_name} -> {os.path.basename(new_path)}")
        except Exception as e:
            print(f"重命名失败: {old_name} | 错误: {str(e)}")
            return False

    return True

if __name__ == "__main__":
    # 交互式获取路径输入
    folder = input("请输入目标文件夹路径：").strip()
    while not os.path.isdir(folder):
        print(f"错误: 文件夹不存在 - {folder}")
        folder = input("请重新输入有效的目标文件夹路径：").strip()

    txt_file = input("请输入标题文件路径：").strip()
    while not os.path.isfile(txt_file):
        print(f"错误: 文件不存在 - {txt_file}")
        txt_file = input("请重新输入有效的标题文件路径：").strip()

    if not os.path.isdir(folder):
        print(f"错误: 文件夹不存在 - {folder}")
        sys.exit(1)

    try:
        title_list = read_titles(txt_file)
    except Exception as e:
        print(f"读取标题文件失败: {str(e)}")
        sys.exit(1)

    if rename_files(folder, title_list):
        print("\n所有文件重命名完成！")
    else:
        print("\n重命名过程中出现问题，请检查输出信息")
        sys.exit(1)