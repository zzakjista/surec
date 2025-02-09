# © 2025 SuRec Contributors. All Rights Reserved.
# Distributed under the terms of the Apache License 2.0.
# For more details, visit: https://www.apache.org/licenses/LICENSE-2.0

from abc import ABC, abstractmethod


class BaseTrainer(ABC):
    @abstractmethod
    def train(self):
        pass

    def train_one_epoch(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass
