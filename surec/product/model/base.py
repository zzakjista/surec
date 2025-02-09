# © 2025 SuRec Contributors. All Rights Reserved.
# Distributed under the terms of the Apache License 2.0.
# For more details, visit: https://www.apache.org/licenses/LICENSE-2.0

from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def inference(self):
        pass
