# © 2025 SuRec Contributors. All Rights Reserved.
# Distributed under the terms of the Apache License 2.0.
# For more details, visit: https://www.apache.org/licenses/LICENSE-2.0

class ModelRegistry:
    def __init__(self):
        self.models = {}

    def register(self, model):
        self.models[model.name] = model

    def get(self, name):
        return self.models[name]

    def update(self, model):
        if model.name in self.models:
            self.models[model.name] = model
        else:
            raise ModuleNotFoundError(f"Model {model.name} not found in registry")
        
    def delete(self, name):
        del self.models[name]
    
    