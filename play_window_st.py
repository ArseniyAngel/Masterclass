from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QPushButton


class PlayWindow(QtWidgets.QMainWindow):
    def __init__(self, slider_value=1, window=None):
        super().__init__()
        uic.loadUi('windows/play screen.ui', self)
        self.slider_value = slider_value
        self.score = 0
        self.current_room = 0
        self.total_rooms = 0
        self.ghost_door = 0
        self.difficulty = ""
        self.start_window = window
        self.setup_game()
        self.connect_signals()

        self.next_room()

    def setup_game(self):
        """Настройка параметров игры"""
        # Сюда впишите код настройки игры

        # Сюда впишите код настройки игры
        self.first_door = self.findChild(QtWidgets.QPushButton, 'firstDoor')
        self.second_door = self.findChild(QtWidgets.QPushButton, 'secondDoor')
        self.third_door = self.findChild(QtWidgets.QPushButton, 'thirdDoor')
        self.label_info = self.findChild(QtWidgets.QLabel, 'labelInfo')
        self.label_score = self.findChild(QtWidgets.QLabel, 'labelScore')
        self.label_room = self.findChild(QtWidgets.QLabel, 'labelRoom')

        door_width, door_height = 200, 250  # или нужные вам размеры

        for door in [self.first_door, self.second_door, self.third_door]:
            door.setFixedSize(door_width, door_height)
        icon = QIcon("pictures/Closed door.png")

        self.first_door.setIcon(icon)
        self.first_door.setIconSize(self.first_door.size())

        self.second_door.setIcon(icon)
        self.second_door.setIconSize(self.second_door.size())

        self.third_door.setIcon(icon)
        self.third_door.setIconSize(self.third_door.size())

        self.first_door.setText("")
        self.second_door.setText("")
        self.third_door.setText("")

    def connect_signals(self):
        """Подключаем сигналы кнопок"""
        if self.first_door:
            self.first_door.clicked.connect(lambda: self.door_selected(1))
        if self.second_door:
            self.second_door.clicked.connect(lambda: self.door_selected(2))
        if self.third_door:
            self.third_door.clicked.connect(lambda: self.door_selected(3))

    def update_ui(self):
        """Обновление информации на экране"""
        if self.label_room:
            if self.difficulty == "infinity":
                self.label_room.setText(f"Комната: {self.current_room} (∞)")
            else:
                self.label_room.setText(f"Комната: {self.current_room}/{self.total_rooms}")

        if self.label_score:
            self.label_score.setText(f"Счет: {self.score}")

        if self.label_info:
            self.label_info.setText("Выберите дверь (1-3)")

    def door_selected(self, door_number):
        """Обработка выбора двери"""
        # Сюда впишите код настройки игры

        # Сюда впишите код настройки игры

    def next_room(self):
        """Подготовка следующей комнаты"""
        # Сюда впишите код настройки игры

        # Сюда впишите код настройки игры

    def game_over(self, win=False):
        """Завершение игры"""
        self.set_buttons_enabled(False)

        if win:
            self.label_info.setGeometry(50, 100, 200, 150)
            pixmap = QPixmap("pictures/win.png")

            # Масштабируем и устанавливаем
            self.label_info.setPixmap(pixmap.scaled(
                350, 300,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

            self.label_info.setStyleSheet("background: transparent;")
            self.label_info.setGeometry(50, 100, 400, 400)
            message = f"🎉 Победа! Итоговый счет: {self.score}"
        else:
            self.label_info.setGeometry(50, 100, 200, 150)
            pixmap = QPixmap("pictures/boo.png")

            # Масштабируем и устанавливаем
            self.label_info.setPixmap(pixmap.scaled(
                350, 300,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

            self.label_info.setStyleSheet("background: transparent;")
            self.label_info.setGeometry(50, 100, 400, 400)
            message = f"💀 Игра окончена! Счет: {self.score}"

        if self.label_score:
            self.label_score.setText(message)

            self.again = QPushButton("Играть снова", self)
            self.again.setGeometry(400, 350, 200, 50)
            self.again.setStyleSheet("""
                               QPushButton {
                                   color: #333333;
                                   background-color: #ffffff;
                                   border: 2px solid #dddddd;
                                   padding: 8px 16px;
                                   border-radius: 4px;
                                   font-size: 14px;
                               }
                               QPushButton:hover {
                                   color: #1f43d6;  /* Красный текст при наведении */
                                   background-color: #f8f8f8;
                                   border: 2px solid #bbbbbb;
                               }
                               QPushButton:pressed {
                                   color: #0c1746;  /* Темно-красный при нажатии */
                                   background-color: #eeeeee;
                               }
                           """)
            self.again.clicked.connect(self.go_to_start)
            self.again.raise_()
            self.again.show()

    def set_buttons_enabled(self, enabled):
        """Включение/выключение кнопок"""
        for btn in [self.first_door, self.second_door, self.third_door]:
            if btn:
                btn.setEnabled(enabled)

    def calculate_points(self):
        """Расчет очков за комнату"""
        # Сюда впишите код настройки игры

        # Сюда впишите код настройки игры

    def go_to_start(self):

        if not hasattr(self, 'start_window'):
            self.start_window = self.window()
        self.close()
        self.start_window.show()
