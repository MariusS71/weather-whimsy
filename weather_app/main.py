import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
from api_utils import get_weather


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather Whimsy")
        self.setFixedSize(400, 400)

        # Layout
        self.layout = QVBoxLayout()

        # Input field
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter city...")
        self.layout.addWidget(self.city_input)

        # Button
        self.button = QPushButton("Get Weather")
        self.button.clicked.connect(self.show_weather)
        self.layout.addWidget(self.button)

        # Labels
        self.weather_label = QLabel("Weather info will appear here")
        self.layout.addWidget(self.weather_label)

        # Funny message
        self.message_label = QLabel("")
        self.layout.addWidget(self.message_label)

        # Character Image
        self.character_label = QLabel(self)
        pixmap = QPixmap("assets/character.jpg")  # put any image here
        self.character_label.setPixmap(pixmap.scaledToWidth(200))
        self.layout.addWidget(self.character_label)

        self.setLayout(self.layout)

    def show_weather(self):
        city = self.city_input.text()
        print(city)
        data = get_weather()


        if not data:
            self.weather_label.setText("Could not fetch weather.")
            return

        # Update labels
        self.weather_label.setText(
            f"{data['city']}: {data['temp']}°C, {data['description']}"
        )

        # Funny reactions
        if data["main"].lower() == "rain":
            self.message_label.setText("☔ Your character is grumpy in the rain!")
        elif data["main"].lower() == "clear":
            self.message_label.setText("😎 It's sunny! Time to flex shades.")
        elif data["main"].lower() == "clouds":
            self.message_label.setText("☁️ Fluffy sky, fluffy mood.")
        else:
            self.message_label.setText("🤔 Weather is confusing today...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
