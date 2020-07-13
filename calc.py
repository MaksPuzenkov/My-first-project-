from design import Ui_MainWindow
from PyQt5 import QtWidgets


class CalcGui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button0.clicked.connect(lambda: self.on_button_click(0))
        self.button1.clicked.connect(lambda: self.on_button_click(1))
        self.button2.clicked.connect(lambda: self.on_button_click(2))
        self.button3.clicked.connect(lambda: self.on_button_click(3))
        self.button4.clicked.connect(lambda: self.on_button_click(4))
        self.button5.clicked.connect(lambda: self.on_button_click(5))
        self.button6.clicked.connect(lambda: self.on_button_click(6))
        self.button7.clicked.connect(lambda: self.on_button_click(7))
        self.button8.clicked.connect(lambda: self.on_button_click(8))
        self.button9.clicked.connect(lambda: self.on_button_click(9))
        self.buttonDiv.clicked.connect(lambda: self.on_button_click('/'))
        self.buttonEqual.clicked.connect(self.calc_result)
        self.buttonMin.clicked.connect(lambda: self.on_button_click('-'))
        self.buttonMul.clicked.connect(lambda: self.on_button_click('*'))
        self.buttonPlus.clicked.connect(lambda: self.on_button_click('+'))

        self.pushButton_2.clicked.connect(lambda: self.clean())

    def clean(self):
        self.lineEditResult.setText('')

    def on_button_click(self, buttoncontent):
        current_text = self.lineEditResult.text()
        self.lineEditResult.setText(current_text + str(buttoncontent))

    def calc_result(self):
        try:
            expression = self.lineEditResult.text()
            eval_result = eval(expression)
            self.lineEditResult.setText(str(eval_result))
        except ZeroDivisionError:
            print("На ноль нельзя делить!")
        except SyntaxError:
            print('Пиши правильно!')
        

app = QtWidgets.QApplication([])  # Создаем приложение
window = CalcGui()                # Создаем окно
window.show()                     # отображаем
app.exec_()                       # запускаем приложение
