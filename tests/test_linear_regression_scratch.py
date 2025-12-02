import numpy as np

from ml_recipes.models.linear_regression_scratch import LinearRegressionScratch


def test_linear_regression_scratch_simple():
    # Simple linear relation y = 2x + 1
    X = np.array([[0.0], [1.0], [2.0], [3.0]])
    y = 2 * X.flatten() + 1

    model = LinearRegressionScratch()
    model.fit(X, y)
    preds = model.predict(X)

    assert preds.shape == y.shape
    # Check that predictions are reasonably close
    assert np.allclose(preds, y, atol=1e-6)
