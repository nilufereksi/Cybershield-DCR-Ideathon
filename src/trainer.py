from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pandas as pd
from typing import List

class ThreatDetectionEngine:
    def __init__(self, contamination: float = 0.05):
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self.scaler = StandardScaler()

    def analyze(self, df: pd.DataFrame, feature_cols: List[str]) -> pd.DataFrame:
        """Veriyi ölçeklendirir ve anomali tahmini yapar."""
        X = self.scaler.fit_transform(df[feature_cols])
        
        # -1: Anomali (Tehdit), 1: Normal
        df['anomaly_score'] = self.model.fit_predict(X)
        df['confidence_score'] = self.model.decision_function(X)
        
        return df