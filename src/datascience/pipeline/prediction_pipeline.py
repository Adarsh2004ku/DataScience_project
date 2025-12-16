import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self, model_path: str = None):
        # default model path
        if model_path is None:
            model_path = Path("artifacts/model_trainer/model.joblib")
        else:
            model_path = Path(model_path)

        if not model_path.exists():
            # Do not fail import time; raise on instantiation so callers can handle it
            raise FileNotFoundError(f"Model file not found at: {model_path}")

        self.model = joblib.load(model_path)

    def predict(self, data):
        arr = np.array(data)
        if arr.ndim == 1:
            arr = arr.reshape(1, -1)

        prediction = self.model.predict(arr)
        try:
            return prediction.tolist()
        except Exception:
            return prediction