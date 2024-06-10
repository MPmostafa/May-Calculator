import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)
        self.layout = QGridLayout()

        self.display = QLineEdit()
        self.display.setPlaceholderText("0")
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            ("7", 1, 0, 1, 1),
            ("8", 1, 1, 1, 1),
            ("9", 1, 2, 1, 1),
            ("/", 1, 3, 1, 1),
            ("4", 2, 0, 1, 1),
            ("5", 2, 1, 1, 1),
            ("6", 2, 2, 1, 1),
            ("*", 2, 3, 1, 1),
            ("1", 3, 0, 1, 1),
            ("2", 3, 1, 1, 1),
            ("3", 3, 2, 1, 1),
            ("-", 3, 3, 1, 1),
            ("0", 4, 0, 1, 1),
            (".", 4, 1, 1, 1),
            ("=", 4, 2, 1, 1),
            ("+", 4, 3, 1, 1),
            ("C", 5, 0, 1, 4),
        ]

        for text, row, col, rowspan, colspan in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.buttonClicked)
            self.layout.addWidget(button, row, col, rowspan, colspan)

        self.setLayout(self.layout)

    def buttonClicked(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            expression = self.display.text()
            try:
                result = str(eval(expression))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif text == "C":
            self.display.setText("0")
        else:
            if self.display.text() == "0":
                self.display.setText(text)
            else:
                self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
