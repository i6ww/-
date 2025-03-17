import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import huoquname
import rename_files

class FileApp:
    def __init__(self, master):
        self.master = master
        master.title("文件重命名工具-韵网小工具")
        master.geometry("1200x500")

        # 主布局
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 左侧文件列表生成模块
        self.left_frame = ttk.LabelFrame(self.main_frame, text="标题爬取生成")
        self.left_frame.grid(row=0, column=0, sticky='nsew', padx=5)

        # 右侧文件重命名模块
        self.right_frame = ttk.LabelFrame(self.main_frame, text="文件批量重命名")
        self.right_frame.grid(row=0, column=1, sticky='nsew', padx=5)

        # 配置网格权重
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # 初始化左侧组件
        self.setup_left_panel()
        # 初始化右侧组件
        self.setup_right_panel()

    def setup_left_panel(self):
        # 路径选择
        ttk.Label(self.left_frame, text="目标文件夹：").grid(row=0, column=0, sticky='w')
        self.left_path = tk.StringVar()
        ttk.Entry(self.left_frame, textvariable=self.left_path, width=30).grid(row=0, column=1)
        ttk.Button(self.left_frame, text="浏览...", command=self.select_left_folder).grid(row=0, column=2)

        # 生成按钮
        ttk.Button(self.left_frame, text="生成文件列表", command=self.generate_list).grid(row=1, column=1, pady=10)

        # 状态显示
        self.left_status = ttk.Label(self.left_frame, text="")
        self.left_status.grid(row=2, column=0, columnspan=3)

        # 分步教程区域
        self.notebook = ttk.Notebook(self.left_frame)
        self.notebook.grid(row=3, column=0, columnspan=3, sticky='nsew', pady=5)

        # 文件列表生成教程页
        self.tab1 = ttk.Frame(self.notebook)
        self._create_tutorial_tab(self.tab1, 
            "标题爬取步骤：",
            [
                "1. 选择目标文件夹路径",
                "2. 点击'生成文件列表'按钮",
                "3. 生成的列表文件将保存在目标文件夹中"
            ],
            [
                "⚠️ 请确保文件夹包含有效文件",
                "⚠️ 文件按名称排序生成"
            ]
        )

        # 文件重命名教程页
        self.tab2 = ttk.Frame(self.notebook)
        self._create_tutorial_tab(self.tab2, 
            "文件重命名步骤：",
            [
                "1. 在右侧选择目标文件夹",
                "2. 选择包含标题的txt文件",
                "3. 点击'开始重命名'按钮",
                "4. 在日志区域查看操作结果"
            ],
            [
                "⚠️ 确保标题数量与文件数量一致",
                "⚠️ 重命名前建议备份原始文件"
            ]
        )

        self.notebook.add(self.tab1, text='标题爬取教程')
        self.notebook.add(self.tab2, text='重命名教程')

    def _create_tutorial_tab(self, parent, title, steps, notes):
        # 标题
        ttk.Label(parent, text=title, font=('微软雅黑', 10, 'bold'))\
            .grid(row=0, column=0, sticky='w', pady=(0,5))
        
        # 步骤说明
        for i, step in enumerate(steps, 1):
            ttk.Label(parent, text=step, foreground='#2c3e50')\
                .grid(row=i, column=0, sticky='w', padx=10)
        
        # 注意事项
        ttk.Label(parent, text="注意事项：", font=('微软雅黑', 9, 'bold'), foreground='#c0392b')\
            .grid(row=len(steps)+1, column=0, sticky='w', pady=(10,5))
        
        for j, note in enumerate(notes, len(steps)+2):
            lbl = ttk.Label(parent, text=note, foreground='#c0392b', 
                          background='#f9ebea', padding=5)
            lbl.grid(row=j, column=0, sticky='ew', padx=10)
            parent.columnconfigure(0, weight=1)

    def setup_right_panel(self):
        # 文件夹选择
        ttk.Label(self.right_frame, text="目标文件夹：").grid(row=0, column=0, sticky='w')
        self.right_path = tk.StringVar()
        ttk.Entry(self.right_frame, textvariable=self.right_path, width=30).grid(row=0, column=1)
        ttk.Button(self.right_frame, text="浏览...", command=self.select_right_folder).grid(row=0, column=2)

        # 标题文件选择
        ttk.Label(self.right_frame, text="标题文件：").grid(row=1, column=0, sticky='w')
        self.title_path = tk.StringVar()
        ttk.Entry(self.right_frame, textvariable=self.title_path, width=30).grid(row=1, column=1)
        ttk.Button(self.right_frame, text="浏览...", command=self.select_title_file).grid(row=1, column=2)

        # 执行按钮
        ttk.Button(self.right_frame, text="开始重命名", command=self.rename_files).grid(row=2, column=1, pady=10)

        # 进度条
        self.progress = ttk.Progressbar(self.right_frame, orient='horizontal', mode='determinate')
        self.progress.grid(row=3, column=0, columnspan=3, sticky='ew')

        # 状态显示
        self.right_status = ttk.Label(self.right_frame, text="")
        self.right_status.grid(row=4, column=0, columnspan=3)

        # 新增日志区域
        from tkinter.scrolledtext import ScrolledText
        self.log_area = ScrolledText(self.right_frame, height=8, wrap=tk.WORD)
        self.log_area.grid(row=5, column=0, columnspan=3, sticky='nsew', pady=5)

        # 调整布局权重
        self.right_frame.rowconfigure(5, weight=1)

    def select_left_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.left_path.set(path)

    def generate_list(self):
        try:
            folder = self.left_path.get()
            if not os.path.isdir(folder):
                raise ValueError("请选择有效文件夹")

            files = sorted(huoquname.get_filenames(folder))
            output_path = huoquname.create_output_filename(folder)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(files))

            self.left_status.config(text=f"成功生成 {len(files)} 个文件列表：{os.path.basename(output_path)}", foreground='green')
        except Exception as e:
            messagebox.showerror("错误", f"生成失败：{str(e)}")
            self.left_status.config(text=str(e), foreground='red')

    def select_right_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.right_path.set(path)

    def select_title_file(self):
        filetypes = [('文本文件', '*.txt')]
        path = filedialog.askopenfilename(filetypes=filetypes)
        if path:
            self.title_path.set(path)

    def rename_files(self):
        try:
            folder = self.right_path.get()
            txt_file = self.title_path.get()
            
            if not all([os.path.isdir(folder), os.path.isfile(txt_file)]):
                raise ValueError("请填写完整路径信息")

            titles = rename_files.read_titles(txt_file)
            files = sorted(huoquname.get_filenames(folder))
            
            if len(files) != len(titles):
                raise ValueError(f"文件数量({len(files)})与标题数量({len(titles)})不匹配")

            self.progress['maximum'] = len(files)
            self.progress['value'] = 0
            
            for i in range(len(files)):
                old_name = files[i]
                new_name = titles[i]
                if rename_files.rename_files(folder, titles):
                    self.progress['value'] = i+1
                    log_msg = f"重命名成功：{old_name} -> {new_name}\n"
                    self.log_area.insert(tk.END, log_msg)
                    self.log_area.see(tk.END)
                    self.master.update_idletasks()

            self.right_status.config(text="所有文件重命名完成！", foreground='green')
            messagebox.showinfo("完成", "文件重命名操作已成功完成！")
        except Exception as e:
            messagebox.showerror("错误", str(e))
            self.right_status.config(text=str(e), foreground='red')
            self.progress['value'] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = FileApp(root)
    root.mainloop()