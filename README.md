# Food Delivery Time Prediction

**Aaditi Gaikwad | PRN 23070521052**  
**Predictive Analytics | Submitted to Dr. Deepak Asudani**

## Problem statement
Predict total food delivery time in minutes from distance, traffic, weather, time of day, vehicle and courier experience. The project demonstrates the end-to-end KDD process using supervised regression.

## Dataset and scope
The unchanged `Food_Delivery_Times.csv` is from Den_Kuznetz (`denkuznetz`), [Food Delivery Time Prediction](https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction), Kaggle version 1. Provider metadata lists Apache 2.0. Attribution, license text and source metadata are included under `data/`.

The CSV contains 1,000 orders and nine columns. There are 120 missing predictor cells: 30 each in weather, traffic, time of day and courier experience. No missing targets or duplicate order IDs were found. The source does not document a collection period, geography or sampling protocol. This is an educational benchmark, not verified data from a named delivery company.

Target: `Delivery_Time_min`. Six predictors: `Distance_km`, `Courier_Experience_yrs`, `Weather`, `Traffic_Level`, `Time_of_Day`, `Vehicle_Type`.

**Excluded:** `Order_ID` is an identifier; recorded `Preparation_Time_min` may not be known at order time and is excluded to protect the prediction boundary. Supplied weather/traffic are contextual conditions, not verified archived forecasts. Live early-ETA use would require availability checks.

## Methodology / KDD stages
1. Define a regression problem and validation-MAE selection criterion.
2. Select the dataset, interpret columns and audit missingness, ranges and duplicates.
3. Reserve a fixed random 20% test set before exploratory plots; use 800 development orders for model selection.
4. Fit numerical imputation, missing indicators and scaling, plus categorical imputation and one-hot encoding, within each training fold.
5. Compare seven configurations: median baseline, Ridge (alpha 1/10), random forest (leaf size 2/5), histogram boosting (7/15 leaves).
6. Choose lowest mean five-fold CV MAE; refit on development data and evaluate the 200 test orders once.
7. Interpret residuals, traffic-group errors and permutation importance; export/reload the pipeline and run inference.

No timestamps or restaurant/courier IDs are available. The random split assumes comparable independent orders and does not demonstrate future-period or unseen-entity generalization. No holdout-driven tuning is performed. Predictions are clipped at zero consistently; metrics use unrounded values.

## Measured results
Selected model: **Ridge alpha=10**.

| Held-out model | MAE (minutes) | RMSE (minutes) | R² | Within 10 minutes |
|---|---:|---:|---:|---:|
| Training-median baseline | 17.46 | 21.18 | -0.001 | 31.5% |
| Selected model | 8.57 | 11.14 | 0.723 | 66.5% |

MAE reduction: **50.9%**. R² is not classification accuracy. A more complex model did not win this experiment. The test MAE is slightly below training MAE, which is possible due to sampling variation; it does not mean unseen orders are intrinsically easier.

## Files
```text
Food_Delivery_Time_KDD.ipynb  Executed source notebook, explanations and charts
README.md                    Project overview and instructions
requirements.txt             Exact core dependency versions
run_notebook.py               Execute all cells and save outputs
predict.py                    Saved-model inference on input CSV
data/                         CSV, attribution, license, metadata, schema, sample
models/food_delivery.joblib    Complete fitted preprocessing + regressor
results/                      CV scores, test predictions, metrics and figures
report/                       Eight-page, six-chapter project report
```

## Reproduce (Python 3.12)
Extract the ZIP and open a terminal inside this project folder.

```bash
python -m venv .venv
```

Windows PowerShell activation:
```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux activation:
```bash
source .venv/bin/activate
```

Install, register the environment kernel and execute:
```bash
python -m pip install -r requirements.txt
python -m ipykernel install --sys-prefix --name python3 --display-name "Python 3 (food-delivery)"
python run_notebook.py
```

Alternatively open the notebook in VS Code and select this environment, or install JupyterLab and launch it from the project directory. Data are bundled; no network is needed after installing packages. The executed notebook already contains results for review. Rerunning updates generated result/model files; it does not regenerate the static PDF report.

## Prediction example
```bash
python predict.py --input data/example_input.csv --output results/example_prediction.csv
```

The input must contain the six predictor columns in `data/feature_schema.json`; no target or preparation time is required. Use kilometres and years for numeric inputs. Blank predictors are imputed by the pipeline. Categorical codes are validated and out-of-range numeric values produce an extrapolation warning. The included example is a held-out row. Load only trusted joblib files.

## Verification
All notebook code cells were executed successfully. The notebook checks split disjointness, excluded predictors, finite non-negative predictions and equality after model reload. The exported example was also tested through `predict.py`. Split order IDs and row-level predictions are saved for audit.

Dataset SHA-256: `9fc2f147a79ee7edec9cc19e70c35d460df713f942b4f1ea9197ba7c2ad6a543`.

## GitHub upload
Create a repository and upload the **extracted contents** of this folder, including notebook, dataset, README and supporting folders. Do not upload only the ZIP or include `.venv`. The notebook is ready for GitHub preview with saved outputs. The project has not been uploaded automatically.

## Limitations and future work
Small sample, limited provenance, no timestamps/entity IDs, unspecified timing of contextual measurements, no kitchen-workload information or prediction intervals. Random holdout results do not establish production reliability. Importance measures are not causal. Future work should add known-at-order preparation estimates, operational timestamps, temporal/entity holdouts and uncertainty estimates. Delivery estimates should not be used to encourage unsafe courier behaviour.

## References
1. [Kaggle dataset](https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction).
2. Garg et al. (2025), [Food Delivery Time Prediction in Indian Cities Using Machine Learning Models](https://arxiv.org/abs/2503.15177), arXiv preprint. Background only; different dataset and experiment.
3. Wen et al. (2023), [A Survey on Service Route and Time Prediction in Instant Delivery](https://arxiv.org/abs/2309.01194), arXiv preprint.
4. [scikit-learn pipelines](https://scikit-learn.org/stable/modules/compose.html).
5. [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html).
6. [Permutation importance](https://scikit-learn.org/stable/modules/permutation_importance.html).
