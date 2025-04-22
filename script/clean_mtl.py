import os

def clean_mtl_files(directory):
    """
    遍历指定目录中的所有 .mtl 文件，去除 map_Kd 行中的多余空格。
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".mtl"):
                mtl_path = os.path.join(root, file)
                clean_mtl_file(mtl_path)

def clean_mtl_file(mtl_path):
    """
    去除单个 .mtl 文件中 map_Kd 行的多余空格。
    """
    try:
        with open(mtl_path, "r") as f:
            lines = f.readlines()

        cleaned_lines = []
        for line in lines:
            if line.strip().startswith("map_Kd"):
                parts = line.split()
                if len(parts) > 1:
                    # 去除 map_Kd 后的多余空格
                    cleaned_line = f"map_Kd {parts[1].strip()}\n"
                    cleaned_lines.append(cleaned_line)
                else:
                    cleaned_lines.append(line)
            else:
                cleaned_lines.append(line)

        # 将清理后的内容写回文件
        with open(mtl_path, "w") as f:
            f.writelines(cleaned_lines)

        print(f"Cleaned: {mtl_path}")
    except Exception as e:
        print(f"Error processing {mtl_path}: {e}")

if __name__ == "__main__":
    # 指定要遍历的目录
    directory = "/home/jerry/code/RoboTwin/ycb_urdfs/ycb_assets"
    clean_mtl_files(directory)