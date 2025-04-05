# © 2025 SuRec Contributors. All Rights Reserved.
# Distributed under the terms of the Apache License 2.0.
# For more details, visit: https://www.apache.org/licenses/LICENSE-2.0

class Cart:
    """Cart is a Model Manage Interface that manages models in a cart."""

    def __init__(self, num_slots: int):
        self.num_slots = num_slots
        self.models = {}
    
    def get_num_slots(self):
        return self.num_slots
    
    def set_num_slots(self, num_slots):
        self.num_slots = num_slots

    def add_model(self, model):
        if len(self.models) == self.num_slots:
            raise OverflowError("Cart is full. Update or remove a model before adding a new one.")
        self.models[model.name] = model
    
    def get_model(self, name):
        return self.models[name]
    
    def update_model(self, model):
        if model.name in self.models:
            self.models[model.name] = model

    

