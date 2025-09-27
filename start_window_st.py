from PyQt6 import QtWidgets, uic
import sys
from play_window_st import PlayWindow
from PyQt6.QtGui import QMovie


#


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows/start screen.ui', self)
        self.original_styles = {}
        self.save_original_styles()
        self.setup_background()
        self.make_elements_transparent()
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButtonToPlay')
        self.vertical_slider = self.findChild(QtWidgets.QSlider, 'verticalSlider')
        self.vertical_slider.setMinimum(1)
        self.vertical_slider.setMaximum(4)
        self.vertical_slider.setValue(1)
        self.label1 = self.findChild(QtWidgets.QLabel, 'label1')
        self.label2 = self.findChild(QtWidgets.QLabel, 'label2')
        self.label3 = self.findChild(QtWidgets.QLabel, 'label3')
        self.label4 = self.findChild(QtWidgets.QLabel, 'label4')
        self.on_slider_released()
        self.vertical_slider.sliderReleased.connect(self.on_slider_released)
        self.style_buttons()
        self.button.clicked.connect(self.on_button_click)

    def save_original_styles(self):
        """Сохраняет оригинальные стили элементов"""
        for widget in self.findChildren(QtWidgets.QWidget):
            self.original_styles[widget] = widget.styleSheet()

    def setup_background(self):
        """Настраивает GIF фон"""
        self.bg_label = QtWidgets.QLabel(self)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.bg_label.setScaledContents(True)
        self.bg_label.lower()

        self.movie = QMovie("pictures/3a8d54d3c0bbaa991cdf8d468b5f7cd8ad506460r1-500-423_hq.gif")
        self.bg_label.setMovie(self.movie)
        self.movie.start()

    def make_elements_transparent(self):
        """Делает элементы прозрачными для отображения фона"""
        transparent_style = "background: transparent; border: none;"

        for widget in self.findChildren(QtWidgets.QWidget):
            if widget != self.bg_label:
                current_style = widget.styleSheet()
                if "background:" not in current_style:
                    widget.setStyleSheet(current_style + transparent_style)

    def resizeEvent(self, event):
        """Обновляет размер фона при изменении размера окна"""
        super().resizeEvent(event)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())

    def on_button_click(self):
        slider_value = self.vertical_slider.value()

        if hasattr(self, 'play_window'):
            del self.play_window
        self.play_window = PlayWindow(slider_value, self)
        self.play_window.show()
        self.close()

    def style_buttons(self):
        """Применяет стиль ко всем кнопкам в окне"""
        buttons = self.findChildren(QtWidgets.QPushButton)

        for button in buttons:
            button.setStyleSheet("""
                   QPushButton {
                       color: #333333;
                       background-color: #ffffff;
                       border: 2px solid #dddddd;
                       padding: 8px 16px;
                       border-radius: 4px;
                       font-size: 14px;
                   }
                   QPushButton:hover {
                       color: #ff0000;  /* Красный текст при наведении */
                       background-color: #f8f8f8;
                       border: 2px solid #bbbbbb;
                   }
                   QPushButton:pressed {
                       color: #cc0000;  /* Темно-красный при нажатии */
                       background-color: #eeeeee;
                   }
               """)

    def on_slider_released(self):
        """Изменение цвета текста в зависимости от значения слайдера"""
        # Сюда впишите код настройки игры

        # Сюда впишите код настройки игры

    def set_label_color(self, label, color):
        """Установка цвета текста для label"""
        if label:
            label.setStyleSheet(f"color: {color}; font-weight: bold;")

    def reset_text_colors(self):
        """Сброс цвета текста всех labels"""
        labels = [self.label1, self.label2, self.label3, self.label4]
        for label in labels:
            if label:
                label.setStyleSheet("color: black; font-weight: normal;")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
