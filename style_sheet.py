def stylesheet(self):
    return """
        QPushButton
        {   
            color: white;
            background: #2b2b2b;
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
        }

        QLineEdit
        {
            color: white;
            background: #2b2b2b;
            border: 1px solid #e2222e;
            font-size: 16pt;
            font-weight: bold;
        }

        QStatusBar
        {
            color: white;
            background: black;
        }"""