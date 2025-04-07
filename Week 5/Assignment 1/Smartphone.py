class Smartphone:
    def __init__(self, brand, model, battery_life):
        # Constructor to initialize attributes
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in percentage

    def make_call(self, phone_number):
        # Simulate making a phone call
        print(f"Calling {phone_number}...")

    def send_message(self, phone_number, message):
        # Simulate sending a message
        print(f"Sending message to {phone_number}: {message}")

    def check_battery(self):
        # Check the battery life
        print(f"Battery life is {self.battery_life}%")

# Creating an instance of Smartphone
my_phone = Smartphone("Apple", "iPhone 14", 95)

# Using methods
my_phone.make_call("254-741-140250")
my_phone.send_message("254-741-140250", "Hey, how's it going?")
my_phone.check_battery()


class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_resolution):
        # Call the parent constructor using super()
        super().__init__(brand, model, battery_life)
        self.camera_resolution = camera_resolution  # in megapixels

    def take_picture(self):
        # Simulate taking a picture
        print(f"Taking a picture with {self.camera_resolution}MP camera...")

# Creating an instance of SmartphoneWithCamera
my_camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S24", 92, 200)

# Using inherited methods from Smartphone class
my_camera_phone.make_call("987-654-3210")
my_camera_phone.send_message("987-654-3210", "Here's a photo!")
my_camera_phone.check_battery()

# Using the new method specific to SmartphoneWithCamera
my_camera_phone.take_picture()
