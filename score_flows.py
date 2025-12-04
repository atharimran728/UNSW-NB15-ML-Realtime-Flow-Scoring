import argparse
import pandas as pd
import joblib

def load_model(model_path):
    return joblib.load(model_path)

def main():
    parser = argparse.ArgumentParser(description="Network Flow Scoring Tool")
    parser.add_argument("--input", required=True, help="Input CSV of network flows")
    parser.add_argument("--output", required=True, help="Output CSV with predictions")
    parser.add_argument("--model", required=True, help="Path to trained model .pkl")
    args = parser.parse_args()

    print("[+] Loading data and model...")
    df = pd.read_csv(args.input)
    model = load_model(args.model)

    drop_cols = [c for c in ["label", "prediction", "probability_malicious"] if c in df]
    if drop_cols:
        X = df.drop(columns=drop_cols)
    else:
        X = df.copy()

    print("[+] Scoring flows...")
    preds = model.predict(X)
    probs = model.predict_proba(X)[:, 1]

    df["prediction"] = preds
    df["probability_malicious"] = probs
    df.to_csv(args.output, index=False)

    print(f"[+] Done! Results saved to {args.output}")
    if df["prediction"].nunique() == 1:
        unique_val = df["prediction"].iloc[0]
        print(f"[!] Warning: All predictions are {unique_val}. "
              f"This may mean input file only contains one class (e.g., all Normal traffic).")

if __name__ == "__main__":
    main()