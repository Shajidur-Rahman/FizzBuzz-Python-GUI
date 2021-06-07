import PyQt5.QtWidgets as pq
import PyQt5.QtGui as gui


class Main(pq.QWidget):
    def __init__(self):
        super(Main, self).__init__()

        self.setWindowTitle('FizzBuzz')
        self.setLayout(pq.QVBoxLayout())

        lable = pq.QLabel('FizzBuzz Game')
        lable.setFont(gui.QFont('saad', 16))
        self.layout().addWidget(lable)

        # enter the number
        enter = pq.QLineEdit()
        self.layout().addWidget(enter)

        button = pq.QPushButton('Submit', clicked= lambda: game())
        self.layout().addWidget(button)

        def game():
            try:
                num = enter.text()
                num = int(num)
                if num%3 == 0 and num%5 ==0:
                    lable.setText('FizzBuzz')
                    enter.setText('')
                elif num%3 == 0:
                    lable.setText('Fizz')
                    enter.setText('')
                elif num%5 == 0:
                    lable.setText('Buzz')
                    enter.setText("")
                else:
                    lable.setText('Try other numbers')
                    enter.setText('')
            except:
                pass
        self.show()
if __name__ == '__main__':
    try:
        app = pq.QApplication([])
        window = Main()
        app.exec_()
    except:
        pass