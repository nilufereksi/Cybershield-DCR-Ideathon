import hashlib
import pandas as pd
from typing import List, Optional

class ZeroKnowledgeTransformer:
    def __init__(self, salt: str = "CyberShield_2026_Global_Salt"):
        self.salt = salt

    def _generate_hash(self, value: str) -> str:
        """SHA-256 ile geri döndürülemez hash üretir."""
        data = f"{value}{self.salt}".encode()
        return hashlib.sha256(data).hexdigest()[:16] # 16 karakter yeterli ve temizdir

    def transform(self, df: pd.DataFrame, sensitive_cols: List[str]) -> pd.DataFrame:
        """Hassas verileri maskeler ve ham veriyi drop eder."""
        df_transformed = df.copy()
        for col in sensitive_cols:
            if col in df_transformed.columns:
                df_transformed[f'masked_{col.lower().replace(" ", "_")}'] = \
                    df_transformed[col].apply(self._generate_hash)
        
        # KVKK Gereği: Ham veriyi sistemden temizle
        df_transformed.drop(columns=[c for c in sensitive_cols if c in df_transformed.columns], inplace=True)
        return df_transformed