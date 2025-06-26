import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class Worker(QThread):
    output_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self, script_path):
        super().__init__()
        self.script_path = script_path
        self.process = None
        self.running = True

    def run(self):
        try:
            self.process = subprocess.Popen(
                [sys.executable, self.script_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                bufsize=1
            )
            while self.running:
                output = self.process.stdout.readline()
                if output:
                    self.output_signal.emit(output)
                elif self.process.poll() is not None:
                    break

            # Process any remaining output
            for output in self.process.stdout.readlines():
                self.output_signal.emit(output)

        except Exception as e:
            self.error_signal.emit(str(e))
        finally:
            self.finished_signal.emit()

    def write_input(self, text):
        if self.process and self.process.stdin:
            self.process.stdin.write(text + "\n")
            self.process.stdin.flush()

    def stop(self):
        if self.process:
            self.process.terminate()
        self.running = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("学生成绩管理系统")
        self.setGeometry(100, 100, 1280, 1020)
        self.setStyleSheet("background-color: #87CEEB;")  # 青蓝色背景

        # 创建主窗口布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 添加抬头标签
        self.title_label = QLabel("学生成绩管理系统", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.layout.addWidget(self.title_label)

        # 初始化四个按钮
        self.buttons = []
        self.scripts = ["build_score.py", "score_analysis.py", "student_analysis.py", "Visualization.py"]
        self.button_texts = ["创建成绩表单", "学生成绩分析", "学生成绩排名", "可视化建图"]
        for text, script in zip(self.button_texts, self.scripts):
            button = QPushButton(text)
            button.setStyleSheet("background-color: #ADD8E6; font-size: 16px;")  # 浅蓝色按钮
            button.clicked.connect(lambda checked, s=script: self.run_script(s))
            self.layout.addWidget(button)
            self.buttons.append(button)

        # 添加终端输出文本框
        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet("background-color: #ADD8E6; font-size: 14px;")  # 浅蓝色
        self.layout.addWidget(self.output_area)

        # 添加输入框
        self.input_area = QTextEdit(self)
        self.input_area.setPlaceholderText("在此输入命令...")
        self.input_area.setStyleSheet("background-color: #ADD8E6; font-size: 14px;")  # 浅蓝色
        self.layout.addWidget(self.input_area)

        self.input_area.textChanged.connect(self.send_input)

        self.worker = None

    def run_script(self, script_path):
        if self.worker is not None:
            self.append_output("已有程序运行，请先停止当前程序！\n")
            return

        self.worker = Worker(script_path)
        self.worker.output_signal.connect(self.append_output)
        self.worker.error_signal.connect(self.append_output)
        self.worker.finished_signal.connect(self.reset_worker)
        self.worker.start()

    def send_input(self):
        if self.worker and self.worker.isRunning():
            text = self.input_area.toPlainText().strip()
            if text:
                self.worker.write_input(text)
                self.input_area.clear()

    def append_output(self, text):
        self.output_area.append(text)

    def reset_worker(self):
        self.worker = None
        self.append_output("程序已完成运行！\n")

    def stop_script(self):
        if self.worker:
            self.worker.stop()
            self.worker = None
            self.append_output("程序已停止！\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
