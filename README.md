# UNSW-NB15 Realtime Flow Scoring

This repository provides a practical SOC-oriented workflow for training a machine-learning model on the UNSW-NB15 dataset and scoring network flows with per-flow malicious probability.  
It is designed as a follow-up to the UNSW-NB15 Feature Engineering Module and focuses on operational detection, rather than just preprocessing.

## What This Project Delivers
- Trainable ML pipeline (Logistic Regression + automatic preprocessing)
- One-click scoring tool for batch network flows
- Outputs:
  - `prediction` (0 = benign, 1 = malicious)
  - `probability_malicious` (confidence score 0.0–1.0)

## Why This Matters for SOC
Most SOCs sit on massive volumes of flow logs that never get enriched.  
This tool acts as a lightweight enrichment layer that can be inserted into:
- threat-hunting workflows  
- alert enrichment pipelines  
- triage automation  
- anomaly detection baselines  

SOC analysts get **per-flow probability scores**, enabling:
- faster prioritization  
- easier threat surfacing  
- better correlation with existing alerts  

## Files
- `train_model.py` — trains UNSW-based model + saves `.pkl`
- `score_flows.py` — scores any flow CSV using the model
- `logreg_unsw.pkl` — saved model (after training)
- `results.csv` — example output
- `UNSW-NB15.csv` — input dataset

## How to Train

`python train_model.py`

This outputs:

`logreg_unsw.pkl`


## How to Score Flows

`python score_flows.py --input unsw-nb15.csv --output results.csv --model logreg_unsw.pkl`


## Output Columns
- `prediction` → model decision  
- `probability_malicious` → confidence score  
- Warning is shown automatically if file contains only one class.

Dataset source: UNSW Canberra Cyber.


## How to Train
