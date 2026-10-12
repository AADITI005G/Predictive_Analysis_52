"""Predict food delivery duration from the saved pipeline. Run from project root."""
from pathlib import Path
import argparse, json
import joblib
import pandas as pd
import numpy as np

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=Path('data/example_input.csv'))
    parser.add_argument('--output',type=Path,default=Path('results/example_prediction.csv'))
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    schema=json.loads((root/'data/feature_schema.json').read_text())
    data=pd.read_csv(args.input)
    missing=set(schema)-set(data.columns)
    if missing:parser.error(f'Missing columns: {sorted(missing)}')
    if data.empty:parser.error('At least one row is required.')
    for name,spec in schema.items():
        values=data[name].dropna()
        if 'allowed' in spec:
            if not values.isin(spec['allowed']).all():parser.error(f'Invalid {name}; allowed values: {spec["allowed"]}')
        else:
            data[name]=pd.to_numeric(data[name],errors='raise')
            values=data[name].dropna()
            if not np.isfinite(values).all() or (values<0).any():parser.error(f'{name} must be finite and non-negative.')
            low,high=spec['observed_range']
            if not values.between(low,high).all():
                print(f'Warning: {name} outside observed training-source range [{low}, {high}]; extrapolation is unvalidated.')
    model=joblib.load(root/'models/food_delivery.joblib')
    data['predicted_minutes']=np.maximum(0,model.predict(data[list(schema)]))
    args.output.parent.mkdir(exist_ok=True,parents=True)
    data.to_csv(args.output,index=False)
    print(data.to_string(index=False));print(f'Saved: {args.output}')

if __name__=='__main__':main()
