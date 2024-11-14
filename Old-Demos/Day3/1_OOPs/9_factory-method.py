# from abc import ABC, abstractmethod

# # Step 1: Define the Model Interface
# class Model(ABC):
#     @abstractmethod
#     def train(self, data: list) -> None:
#         """Train the model with the given data."""
#         pass

#     @abstractmethod
#     def predict(self, inputs: list) -> list:
#         """Make predictions based on inputs."""
#         pass

# # Step 2: Implement Specific Model Classes
# class LinearRegression(Model):
#     def train(self, data: list) -> None:
#         print(f"Training Linear Regression model with {len(data)} data points.")

#     def predict(self, inputs: list) -> list:
#         return [sum(inputs) * 0.5]  # Dummy prediction logic

# class DecisionTree(Model):
#     def train(self, data: list) -> None:
#         print(f"Training Decision Tree model with {len(data)} data points.")

#     def predict(self, inputs: list) -> list:
#         return [max(inputs)]  # Dummy prediction logic

# # Step 3: Create a Factory with Dynamic Registration
# class ModelFactory:
#     _registry = {}

#     @classmethod
#     def register_model(cls, model_type: str, model_class: type[Model]) -> None:
#         """Register a new model type with its corresponding class."""
#         cls._registry[model_type] = model_class

#     @classmethod
#     def create_model(cls, model_type: str) -> Model:
#         """Create a model instance based on the registered type."""
#         if model_type not in cls._registry:
#             raise ValueError(f"Unknown model type: {model_type}")
#         return cls._registry[model_type]()

# # Step 4: Register Model Types
# ModelFactory.register_model("linear_regression", LinearRegression)
# ModelFactory.register_model("decision_tree", DecisionTree)

# # Usage Example
# model = ModelFactory.create_model("linear_regression")
# model.train([1, 2, 3, 4, 5])
# print(model.predict([1, 2, 3]))  # Output: [3.0]

# model = ModelFactory.create_model("decision_tree")
# model.train([10, 20, 30, 40])
# print(model.predict([5, 10, 15]))  # Output: [15]

# # Future: Add New Model
# class KMeans(Model):
#     def train(self, data: list) -> None:
#         print(f"Training KMeans model with {len(data)} data points.")

#     def predict(self, inputs: list) -> list:
#         return [len(set(inputs))]  # Dummy logic to count unique elements

# ModelFactory.register_model("kmeans", KMeans)
# model = ModelFactory.create_model("kmeans")
# model.train([1, 1, 2, 2, 3])
# print(model.predict([1, 2, 2, 3]))  # Output: [3]

# ------------------ Using Decorator
from abc import ABC, abstractmethod

# Step 1: Define the Abstract Base Class for Models
class Model(ABC):
    @abstractmethod
    def train(self, data: list) -> None:
        """Train the model with the given data."""
        pass

    @abstractmethod
    def predict(self, inputs: list) -> list:
        """Make predictions based on inputs."""
        pass

    # Non-abstract method: Can be inherited by all subclasses
    def evaluate(self, inputs: list, labels: list) -> float:
        """Evaluate the model using dummy accuracy logic."""
        predictions = self.predict(inputs)
        correct = sum(1 for p, l in zip(predictions, labels) if p == l)
        return correct / len(labels)
    
# Step 2: Implement the Model Factory with Registration Decorator
class ModelFactory:
    _registry = {}  # Store registered models

    @classmethod
    def register(cls, model_name: str):
        """A decorator for registering new models."""
        def decorator(model_class: type[Model]) -> type[Model]:
            cls._registry[model_name] = model_class
            return model_class  # Return the class to allow normal usage
        return decorator

    @classmethod
    def create_model(cls, model_name: str) -> Model:
        """Create a model instance based on the registered name."""
        if model_name not in cls._registry:
            raise ValueError(f"Unknown model type: {model_name}")
        return cls._registry[model_name]()

# Step 3: Register Models Using the Decorator
@ModelFactory.register("linear_regression")
class LinearRegression(Model):
    def train(self, data: list) -> None:
        print(f"Training Linear Regression with {len(data)} data points.")

    def predict(self, inputs: list) -> list:
        return [sum(inputs) * 0.5]  # Dummy logic

@ModelFactory.register("decision_tree")
class DecisionTree(Model):
    def train(self, data: list) -> None:
        print(f"Training Decision Tree with {len(data)} data points.")

    def predict(self, inputs: list) -> list:
        return [max(inputs)]  # Dummy logic

# Step 4: Usage Example
model = ModelFactory.create_model("linear_regression")
model.train([1, 2, 3, 4, 5])
print(model.predict([1, 2, 3]))  # Output: [3.0]
print(model.evaluate([1, 2, 3], [1, 1, 1]))  # Output: 0.666...

model = ModelFactory.create_model("decision_tree")
model.train([10, 20, 30, 40])
print(model.predict([5, 10, 15]))  # Output: [15]
print(model.evaluate([5, 15, 25], [25, 15, 25]))  # Output: 0.666...

# Step 5: Adding a New Model Dynamically
@ModelFactory.register("kmeans")
class KMeans(Model):
    def train(self, data: list) -> None:
        print(f"Training KMeans model with {len(data)} data points.")

    def predict(self, inputs: list) -> list:
        return [len(set(inputs))]  # Dummy logic to count unique elements

model = ModelFactory.create_model("kmeans")
model.train([1, 1, 2, 2, 3])
print(model.predict([1, 2, 2, 3]))  # Output: [3]
print(model.evaluate([5, 15, 25], [25, 15, 25]))
