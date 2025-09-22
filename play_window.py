import time

from PyQt6 import QtWidgets, uic
import sys

from random import randint

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

        # Начинаем первую комнату
        self.next_room()

    def setup_game(self):
        """Настройка параметров игры"""
        slider_to_difficult = {
            1: "easy",
            2: "normal",
            3: "hard",
            4: "infinity"
        }

        self.difficulty = slider_to_difficult.get(self.slider_value, "normal")

        difficult_rooms = {
            "easy": 5,
            "normal": 8,
            "hard": 15,
            "infinity": 0
        }

        self.total_rooms = difficult_rooms[self.difficulty]
        self.first_door = self.findChild(QtWidgets.QPushButton, 'firstDoor')
        self.second_door = self.findChild(QtWidgets.QPushButton, 'secondDoor')
        self.third_door = self.findChild(QtWidgets.QPushButton, 'thirdDoor')
        self.label_info = self.findChild(QtWidgets.QLabel, 'labelInfo')
        self.label_score = self.findChild(QtWidgets.QLabel, 'labelScore')
        self.label_room = self.findChild(QtWidgets.QLabel, 'labelRoom')

        door_width, door_height = 200, 250  # или нужные вам размеры

        for door in [self.first_door, self.second_door, self.third_door]:
            door.setFixedSize(door_width, door_height)
        icon = QIcon("Closed door.png")

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
        # Блокируем кнопки до следующего раунда
        self.set_buttons_enabled(False)

        doors = {"1": self.first_door,
                 "2": self.second_door,
                 "3": self.third_door}
        for i in doors:
            if int(i) == door_number:
                doors[i].setIcon(QIcon("opened door.png"))
            doors[i].setIconSize(doors[i].size())

        if door_number != self.ghost_door:
            # Игрок выиграл раунд
            points = self.calculate_points()
            self.score += points

            if self.label_info:
                self.label_info.setText(f"✅ Нет приведения! +{points} очков")

            # Задержка перед следующим раундом
            QtWidgets.QApplication.processEvents()  # Обновляем UI
            time.sleep(1.5)
            self.next_room()
        else:
            # Игрок проиграл
            if self.label_info:
                self.game_over()

    def next_room(self):
        """Подготовка следующей комнаты"""
        self.first_door.setIcon(QIcon("Closed door.png"))
        self.first_door.setIconSize(self.first_door.size())
        self.second_door.setIcon(QIcon("Closed door.png"))
        self.second_door.setIconSize(self.second_door.size())
        self.third_door.setIcon(QIcon("Closed door.png"))
        self.third_door.setIconSize(self.third_door.size())

        if self.difficulty != "infinity" and self.current_room >= self.total_rooms:
            self.game_over(win=True)
            return

        self.current_room += 1
        self.ghost_door = randint(1, 3)

        # Обновляем UI
        self.update_ui()

        # Активируем кнопки для выбора
        self.set_buttons_enabled(True)

    def game_over(self, win=False):
        """Завершение игры"""
        self.set_buttons_enabled(False)

        if win:
            self.label_info.setGeometry(50, 100, 200, 150)
            pixmap = QPixmap("win.png")

            # Масштабируем и устанавливаем
            self.label_info.setPixmap(pixmap.scaled(
                350, 300,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

            # Можно сделать фон прозрачным
            self.label_info.setStyleSheet("background: transparent;")
            self.label_info.setGeometry(50, 100, 400, 400)
            message = f"🎉 Победа! Итоговый счет: {self.score}"
        else:
            self.label_info.setGeometry(50, 100, 200, 150)
            pixmap = QPixmap("boo.png")

            # Масштабируем и устанавливаем
            self.label_info.setPixmap(pixmap.scaled(
                350, 300,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

            # Можно сделать фон прозрачным
            self.label_info.setStyleSheet("background: transparent;")
            self.label_info.setGeometry(50, 100, 400, 400)
            message = f"💀 Игра окончена! Счет: {self.score}"

        if self.label_score:
            self.label_score.setText(message)

            self.again = QPushButton("Играть снова", self)
            self.again.setGeometry(300, 300, 200, 50)
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
        if self.difficulty == "infinity":
            return self.current_room * 10
        else:
            return self.total_rooms * self.current_room

    def go_to_start(self):

        if not hasattr(self, 'start_window'):
            self.start_window = self.window()
        self.close()
        self.start_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PlayWindow(2)  # Тестовое значение
    window.show()
    sys.exit(app.exec())
