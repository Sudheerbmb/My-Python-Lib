def say_hello(name):
    return f"Hello, {name}!"
class LoanPredictor:
    def __init__(self,model):
        self.model=model
    def predict(self,data):
        return self.model.predict(data)
        