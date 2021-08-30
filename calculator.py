from PyQt5.QtGui import QFont, QKeySequence, QCursor, QWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, QMessageBox, 
        QShortcut, QGridLayout, QPushButton, QTextEdit,
        QLineEdit, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
from style_sheet import *

class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.init_ui()
        self.init_numpad()
        self.init_layout()
        self.init_signals()
        self.hot_keys()

    def init_ui(self):
        self.display = QLineEdit(self)
        self.display.setFixedWidth(160)
        self.display.setAlignment(Qt.AlignLeft)
        self.display.setFont(QFont('Arial', 32))
        self.display.setStyleSheet(stylesheet(self))

        self.answer = QLabel()
        self.answer.setFixedSize(160,24)
        self.answer.setAlignment(Qt.AlignRight)
        self.answer.setFont(QFont('Arial', 16))
        self.answer.setStyleSheet(stylesheet(self))

        
        text = "Calculator"
        self.title = QStatusBar()
        self.title.showMessage(text)
        #self.title.setWordWrap(True)
        #self.title.setAlignment(Qt.Qt.AlignCenter)
        self.title.setStyleSheet(stylesheet(self))

        self.text_editor = QTextEdit()
        self.text_editor.setStyleSheet(stylesheet(self))
    
    def init_numpad(self):
        self.push_0 = QPushButton("0")
        self.push_0.setFixedSize(32, 32)
        self.push_0.setStyleSheet(stylesheet(self))
        self.push_0.clicked.connect(self._push_0)

        self.push_1 = QPushButton("1")
        self.push_1.setFixedSize(32, 32)
        self.push_1.setStyleSheet(stylesheet(self))
        self.push_1.clicked.connect(self._push_1)

        self.push_2 = QPushButton("2")
        self.push_2.setFixedSize(32, 32)
        self.push_2.setStyleSheet(stylesheet(self))
        self.push_2.clicked.connect(self._push_2)
        
        self.push_3 = QPushButton("3")
        self.push_3.setFixedSize(32, 32)
        self.push_3.setStyleSheet(stylesheet(self))
        self.push_3.clicked.connect(self._push_3)

        self.push_4 = QPushButton("4")
        self.push_4.setFixedSize(32, 32)
        self.push_4.setStyleSheet(stylesheet(self))
        self.push_4.clicked.connect(self._push_4)

        self.push_5 = QPushButton("5")
        self.push_5.setFixedSize(32, 32)
        self.push_5.setStyleSheet(stylesheet(self))
        self.push_5.clicked.connect(self._push_5)

        self.push_6 = QPushButton("6")
        self.push_6.setFixedSize(32, 32)
        self.push_6.setStyleSheet(stylesheet(self))
        self.push_6.clicked.connect(self._push_6)

        self.push_7 = QPushButton("7")
        self.push_7.setFixedSize(32, 32)
        self.push_7.setStyleSheet(stylesheet(self))
        self.push_7.clicked.connect(self._push_7)

        self.push_8 = QPushButton("8")
        self.push_8.setFixedSize(32, 32)
        self.push_8.setStyleSheet(stylesheet(self))
        self.push_8.clicked.connect(self._push_8)

        self.push_9 = QPushButton("9")
        self.push_9.setFixedSize(32, 32)
        self.push_9.setStyleSheet(stylesheet(self))
        self.push_9.clicked.connect(self._push_9)
        
        self.Action_dot = QPushButton(".")
        self.Action_dot.setFixedSize(32, 32)
        self.Action_dot.setStyleSheet(stylesheet(self))
        self.Action_dot.clicked.connect(self.action_dot)

        self.Action_del = QPushButton("DEL")
        self.Action_del.setFixedSize(32, 32)
        self.Action_del.setStyleSheet(stylesheet(self))
        self.Action_del.clicked.connect(self.action_del)

        self.Action_clear = QPushButton("CLR")
        self.Action_clear.setFixedSize(32, 32)
        self.Action_clear.setStyleSheet(stylesheet(self))
        self.Action_clear.clicked.connect(self.action_clear)

        self.Action_plus = QPushButton("+")
        self.Action_plus.setFixedSize(32, 32)
        self.Action_plus.setStyleSheet(stylesheet(self))
        self.Action_plus.clicked.connect(self.action_plus)

        self.Action_minus = QPushButton("-")
        self.Action_minus.setFixedSize(32, 32)
        self.Action_minus.setStyleSheet(stylesheet(self))
        self.Action_minus.clicked.connect(self.action_minus)

        self.Action_multiplication = QPushButton("×")
        self.Action_multiplication.setFixedSize(32, 32)
        self.Action_multiplication.setStyleSheet(stylesheet(self))
        self.Action_multiplication.clicked.connect(self.action_multiplication)
        

        self.Action_divide = QPushButton("÷")
        self.Action_divide.setFixedSize(32, 32)
        self.Action_divide.setStyleSheet(stylesheet(self))
        self.Action_divide.clicked.connect(self.action_divide)

        self.Action_equal = QPushButton("=")
        self.Action_equal.setFixedSize(32, 32)
        self.Action_equal.setStyleSheet(stylesheet(self))
        self.Action_equal.clicked.connect(self.action_equal)

        self.push_ans = QPushButton("Ans")
        self.push_ans.setFixedSize(32, 32)
        self.push_ans.setStyleSheet(stylesheet(self))

        self.push_percent = QPushButton("%")
        self.push_percent.setFixedSize(24, 24)
        self.push_percent.setStyleSheet(stylesheet(self))

        self.push_root = QPushButton("√")
        self.push_root.setFixedSize(24, 24)
        self.push_root.setStyleSheet(stylesheet(self))

        self.push_bracket_start = QPushButton("(")
        self.push_bracket_start.setFixedSize(24, 24)
        self.push_bracket_start.setStyleSheet(stylesheet(self))
        self.push_bracket_start.clicked.connect(self.bracket_start)

        self.push_bracket_end = QPushButton(")")
        self.push_bracket_end.setFixedSize(24, 24)
        self.push_bracket_end.setStyleSheet(stylesheet(self))
        self.push_bracket_end.clicked.connect(self.bracket_end)

        self.push_s_d = QPushButton("S<=>D")
        self.push_s_d.setFixedSize(64, 24)
        self.push_s_d.setStyleSheet(stylesheet(self))

        self.close_button = QPushButton("❌")
        self.close_button.setFixedSize(24, 24)
        self.close_button.setStyleSheet(stylesheet(self))
        self.close_button.clicked.connect(self.close)
        
        self.minimize_button = QPushButton("━")
        self.minimize_button.setFixedSize(24, 24)
        self.minimize_button.setStyleSheet(stylesheet(self))
        self.minimize_button.clicked.connect(self.minimize)

        # create a info
        self.myinfo = """
©2021
Created By Hamim Ally


HotKeys:
    Mouse Wheel = Zoom
    UP = Volume Up
    DOWN = Volume Down + 
    LEFT = < 1 Minute
    RIGHT = > 1 Minute + 
    SHIFT+LEFT = < 10 Minutes
    SHIFT+RIGHT = > 10 Minutes"""

    def minimize(self, event):
            self.setWindowState(self.windowState() | QWindow.Minimized)
        
    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()
    
    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()
            
    def closeEvent(self, event):
            event.accept()


    def hot_keys(self):
        pass

    def init_layout(self):

        self.layout_A = QHBoxLayout()
        self.layout_A.setContentsMargins(0, 0, 0, 0)
        self.layout_A.setSpacing(0)
        self.layout_A.addWidget(self.title)
        self.layout_A.addWidget(self.minimize_button)
        self.layout_A.addWidget(self.close_button)

        # create layout_A
        self.layout_B = QHBoxLayout()
        self.layout_B.setSpacing(0)
        #self.layout_A.addWidget(self.open_button)
        #self.layout_A.addWidget(self.photo_tab)
        #self.layout_A.addWidget(self.video_tab)
        #self.layout_A.addWidget(self.info_button)
        
        # create numpad
        self.numpad = QGridLayout()
        self.numpad.setColumnStretch(2, 0)
        self.numpad.setSpacing(0)
        self.numpad.addWidget(self.push_7)
        self.numpad.addWidget(self.push_8)
        self.numpad.addWidget(self.push_9)
        self.numpad.addWidget(self.push_4)
        self.numpad.addWidget(self.push_5)
        self.numpad.addWidget(self.push_6)
        self.numpad.addWidget(self.push_1)
        self.numpad.addWidget(self.push_2)
        self.numpad.addWidget(self.push_3)
        self.numpad.addWidget(self.push_0)
        self.numpad.addWidget(self.Action_dot)

        self.operator = QGridLayout()
        self.operator.setColumnStretch(1, 0)
        self.operator.setSpacing(0)
        self.operator.addWidget(self.Action_del)
        self.operator.addWidget(self.Action_clear)
        self.operator.addWidget(self.Action_multiplication)
        self.operator.addWidget(self.Action_divide)
        self.operator.addWidget(self.Action_plus)
        self.operator.addWidget(self.Action_minus)
        self.operator.addWidget(self.push_ans)
        self.operator.addWidget(self.Action_equal)

        self.operator_2 = QGridLayout()
        self.operator_2.setColumnStretch(5, 0)
        self.operator_2.setSpacing(0)
        #self.operator_2.addWidget(self.push_percent)
        #self.operator_2.addWidget(self.push_root)
        self.operator_2.addWidget(self.push_bracket_start)
        self.operator_2.addWidget(self.push_bracket_end)
        #self.operator_2.addWidget(self.push_s_d)

        self.H_layout = QHBoxLayout()
        self.H_layout.setSpacing(0)
        self.H_layout.addLayout(self.numpad)
        self.H_layout.addLayout(self.operator)

        # create layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.layout_A)
        self.layout.addLayout(self.layout_B)
        self.layout.addWidget(self.display)
        self.layout.addWidget(self.answer)
        self.layout.addLayout(self.operator_2)
        self.layout.addLayout(self.H_layout)

        self.setLayout(self.layout)

    def init_signals(self):
        pass

    def _push_0(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "0")

    def _push_1(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "1")

    def _push_2(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "2")

    def _push_3(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "3")
    
    def _push_4(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "4")

    def _push_5(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "5")

    def _push_6(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "6")
    
    def _push_7(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "7")
    
    def _push_8(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "8")

    def _push_9(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "9")
    
    def action_dot(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + ".")

    def bracket_start(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + "(")
    
    def bracket_end(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + ")")
    
    def action_equal(self):
        # get the display text
        equation = self.display.text()
  
        try:
            # getting the ans
            ans = eval(equation)
  
            # setting text to the display
            self.answer.setText(str(ans))
  
        except:
            # setting text to the display
            self.display.setText("Syntax Error")
    
    def action_plus(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + " + ")
    
    def action_minus(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + " - ")
    
    def action_divide(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + " / ")
    
    def action_multiplication(self):
        # appending display text
        text = self.display.text()
        self.display.setText(text + " * ")

    
    def action_clear(self):
        # clearing the display text
        self.display.setText("")
        self.answer.setText("")

    def action_del(self):
        # clearing a single digit
        text = self.display.text()
        print(text[:len(text)-1])
        self.display.setText(text[:len(text)-1])
    

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    player = window()
    player.widescreen = True
    player.setWindowFlags(Qt.FramelessWindowHint)
    player.setGeometry(100, 300, 160, 200)
    player.setStyleSheet("background: black; color: #e2222e")
    player.setWindowOpacity(0.8)
    player.show()
    sys.exit(app.exec_())