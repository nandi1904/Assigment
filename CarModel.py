class CarModel1:
    def __init__(self, model_id, display_name):
        self.model = {
            "id": model_id,
            "displayName": display_name
        }
        self.acceptOrders = True
        self.engine = {
            "id": "MTGBD37489IDUDU",
            "dateOfMake": "2022-03-28",
            "fuelType": "diesel"
        }
        self.price = 700000

class LEModel(CarModel1):
    def __init__(self, model_id, display_name):
        super().__init__(model_id, display_name)
        self.price = self.price * 3

class SPXModel(CarModel1):
    def __init__(self, model_id, display_name):
        super().__init__(model_id, display_name)
        self.price = self.price * 2

ga_model = CarModel1("8787878d8d7d878d78efee", "Tata Nano - GA")
spx_model = SPXModel("8787878d8d7d878d78efee", "Tata Nano - SPX")
le_model = LEModel("8787878d8d7d878d78efee", "Tata Nano - LE")

print(ga_model.price)   
print(spx_model.price)  
print(le_model.price)