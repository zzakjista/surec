# © 2025 SuRec Contributors. All Rights Reserved.
# Distributed under the terms of the Apache License 2.0.
# For more details, visit: https://www.apache.org/licenses/LICENSE-2.0

from typing import Any
from abc import ABC, abstractmethod


class BaseDataset(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, idx: int) -> Any:
        pass

class TorchDataset(BaseDataset):
    def __init__(self, dataset):
        self.dataset = dataset

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx: int) -> Any:
        return self.dataset[idx]