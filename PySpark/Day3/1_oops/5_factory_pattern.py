# class A:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(A, cls).__new__(cls, *args, **kwargs)
#         return cls._instance

# a1 = A()
# a2 = A()

# print(a1==a2)

from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def train(self, data:list) -> None:
        pass

    @abstractmethod
    def predict(self, inputs:list) -> list:
        pass

class LinearRegression(Model):
    def train(self, data: list) -> None:
        print(f"Training Linear Regression model with {len(data)} data points.")

    def predict(self, inputs: list) -> list:
        return [sum(inputs) * 0.5]  # Dummy prediction logic
    
class DecisionTree(Model):
    def train(self, data: list) -> None:
        print(f"Training Decision Tree model with {len(data)} data points.")

    def predict(self, inputs: list) -> list:
        return [max(inputs)]  # Dummy prediction logic
    
class ModelFactory:
    _registry = {}

    @classmethod
    def register_model(cls, model_type: str, model_class: type[Model]) -> None:
        cls._registry[model_type] = model_class

    @classmethod
    def create_model(cls, model_type:str) -> Model:
        if model_type not in cls._registry:
            raise ValueError(f"Unknown model type: {model_type}")
        return cls._registry[model_type]()

ModelFactory.register_model("linear_regression", LinearRegression)
ModelFactory.register_model("decision_tree", DecisionTree)

model = ModelFactory.create_model("linear_regression")
model.train([1, 2, 3, 4, 5])
print(model.predict([1, 2, 3]))

model = ModelFactory.create_model("decision_tree")
model.train([10, 20, 30, 40])
print(model.predict([5, 10, 15]))

# Future Addition
class KMeans(Model):
    def train(self, data: list) -> None:
        print(f"Training KMeans model with {len(data)} data points.")

    def predict(self, inputs: list) -> list:
        return [len(set(inputs))]  # Dummy logic to count unique elements
    
ModelFactory.register_model("kmeans", KMeans)

model = ModelFactory.create_model("kmeans")
model.train([10, 20, 30, 40])
print(model.predict([5, 10, 15]))

# Change this code using Decorator