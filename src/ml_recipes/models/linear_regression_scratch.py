from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class LinearRegressionScratch:
    """Very small, educational linear regression using the normal equation.

    This implementation is for learning only and is not optimized.
    """

    fit_intercept: bool = True
    coefficients_: np.ndarray | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LinearRegressionScratch":
        if self.fit_intercept:
            ones = np.ones((X.shape[0], 1))
            X_design = np.hstack([ones, X])
        else:
            X_design = X

        # theta = (X^T X)^-1 X^T y
        XtX = X_design.T @ X_design
        Xty = X_design.T @ y
        self.coefficients_ = np.linalg.pinv(XtX) @ Xty
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.coefficients_ is None:
            raise RuntimeError("Model is not fitted yet.")

        if self.fit_intercept:
            ones = np.ones((X.shape[0], 1))
            X_design = np.hstack([ones, X])
        else:
            X_design = X

        return X_design @ self.coefficients_
