def stylesheet(self):
    return """
        QPushButton
        {   
            color: white;
            background: black;
            border: 0px;
        }

        QPushButton:hover
        {
            color: white;
            background: Black;
            border: 1px solid #e2222e;
        }

        QLabel
        {   
            color: white;
            background: black;
            border-bottom: 1px solid #e2222e;
            border-left: 1px solid #e2222e;
            border-right: 1px solid #e2222e;
        }

        QLineEdit
        {
            color: white;
            background: black;
            font-size: 16pt;
            font-weight: bold;
            border-top: 1px solid #e2222e;
            border-left: 1px solid #e2222e;
            border-right: 1px solid #e2222e;
        }

        QStatusBar
        {
            color: white;
            background: black;
        }"""

def stylesheet0(self):
    return """
        QPushButton
        {   
            color: white;
            background: Black;
            border: 0px;
            font-size: 14pt;
            font-weight: bold;
        }

        QPushButton:hover
        {
            color: white;
            background: Black;
            border: 1px solid #e2222e;
            font-weight: bold;
        }

        QLabel
        {   
            color: white;
            background: black;
        }

        QLineEdit
        {
            color: white;
            background: #2b2b2b;
            font-size: 16pt;
            font-weight: bold;
        }

        QTextEdit
        {
            color: white;
            background: black;
            border: 1px solid #e2222e;
            font-size: 8pt;
        }

        QStatusBar
        {
            color: white;
            background: black;
        }"""