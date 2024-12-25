import os

class ProjectGenerator:
    def __init__(self, md_file='FileFormat.MD'):
        self.md_file = md_file
        self.structure = []
        self.root_dir = None
        
    def parse_md_file(self):
        """解析MD文件"""
        with open(self.md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 找到项目根目录
        for line in lines:
            if '/' in line and 'trading_bot' in line:
                self.root_dir = line.split('/')[0].strip()
                break
        
        if not self.root_dir:
            raise ValueError("未找到根目录")

        current_dir = []
        for line in lines:
            line = line.rstrip()
            
            # 跳过无关行
            if not line or line.startswith('#') or not any(c in line for c in ['│', '├', '└']):
                continue
            
            # 计算当前行的缩进级别
            indent = 0
            for char in line:
                if char in ['│', ' ']:
                    indent += 1
                else:
                    break
            indent = indent // 2  # 每两个字符算一级缩进
            
            # 清理并提取路径部分
            clean_line = (line.replace('│', '')
                             .replace('├', '')
                             .replace('└', '')
                             .replace('─', '')
                             .strip())
            
            # 跳过空行
            if not clean_line:
                continue

            # 提取文件/目录名和注释
            name_part = clean_line.split('#')[0].strip('/ ')
            if not name_part:
                continue
                
            # 根据缩进调整目录层级
            if indent == 0:  # 根目录级别
                current_dir = []
            else:
                # 调整当前路径到正确的层级
                while len(current_dir) > indent - 1:
                    current_dir.pop()
                    
            # 如果是目录，添加到当前路径
            if name_part.endswith('/') or '.' not in name_part:
                current_dir.append(name_part.strip('/'))
                dir_path = os.path.join(self.root_dir, *current_dir)
                self.structure.append((dir_path, True))  # True表示是目录
            else:
                # 文件路径包括当前目录
                file_path = os.path.join(self.root_dir, *current_dir, name_part)
                self.structure.append((file_path, False))  # False表示是文件

    def create_project(self):
        """创建项目结构"""
        try:
            self.parse_md_file()
            
            # 首先创建根目录
            if not os.path.exists(self.root_dir):
                os.makedirs(self.root_dir)
                print(f"创建根目录: {self.root_dir}")
            
            for path, is_dir in self.structure:
                try:
                    if is_dir:
                        # 是目录
                        if not os.path.exists(path):
                            os.makedirs(path)
                            print(f"创建目录: {path}")
                    else:
                        # 是文件
                        dir_path = os.path.dirname(path)
                        if not os.path.exists(dir_path):
                            os.makedirs(dir_path)
                        
                        if not os.path.exists(path):
                            with open(path, 'w') as f:
                                pass
                            print(f"创建文件: {path}")
                            
                except FileExistsError:
                    print(f"已存在: {path}")
                except Exception as e:
                    raise Exception(f"处理 {path} 时出错: {str(e)}")
                    
        except Exception as e:
            raise Exception(f"创建项目结构时出错: {str(e)}")

def main():
    try:
        generator = ProjectGenerator()
        generator.create_project()
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main()  