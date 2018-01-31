from core.playground.abstract_classes import AddressInterface, AddressGeocodeQueueInterface


class AddressImplementation(AddressInterface):
    def __init__(self):
        super().__init__()

    def get_address(self, value):
        return self.conn_str + " AddressImplementation"

    def insert_address_coords(self):
        return "Random coords"

class AddressGeocodeQueueImplementation(AddressGeocodeQueueInterface):
    def __init__(self):
        super().__init__()

    def delete_address_id(self):
        super().delete_address_id()
        return self.conn_str + " AddressGeocodeQueueImplementation " + self.lol

if __name__ == "__main__":
    #AddressInterface() ## TypeError: Can't instantiate abstract class AddressInterface with abstract methods get_address
    y = AddressImplementation().get_address("hello")
    print(y)

    x = AddressGeocodeQueueImplementation().delete_address_id()
    print(x)