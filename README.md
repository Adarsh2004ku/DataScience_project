# End-to-End Data Science Project: Wine Quality Prediction

A complete machine learning pipeline for predicting wine quality using data ingestion, validation, transformation, model training, and evaluation. Includes a Flask web application for interactive predictions.

## Project Overview

This project implements a modular ML pipeline with the following stages:

### ML Pipeline Stages
1. **Data Ingestion** - Load and extract raw wine quality data
2. **Data Validation** - Validate data schema and structure
3. **Data Transformation** - Train-test split and feature preparation
4. **Model Training** - Train ElasticNet regression model
5. **Model Evaluation** - Evaluate metrics and log to MLflow

## Prerequisites

- **Python 3.10+** (tested on 3.10)
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- macOS, Linux, or Windows with command line access

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd DataScience_project
```

### Step 2: Create a Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Project

The project uses YAML configuration files:
- **`config/config.yaml`** - Artifact paths and data directories
- **`params.yaml`** - Model hyperparameters
- **`schema.yaml`** - Data validation schema

Review and update these files if needed for your environment.

## For Other Users: Getting Started with This Project

If someone shared this project with you, follow these steps to run it on your device:

### Quick Start (5 minutes)

```bash
# 1. Clone the repository from GitHub
git clone https://github.com/<owner>/DataScience_project.git
cd DataScience_project

# 2. Create and activate virtual environment
# macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask web app
python app.py

# 5. Open in browser: http://localhost:8080
```

### Using the Web Interface

1. Navigate to `http://localhost:8080`
2. Click **Home** to see the input form
3. Fill in the wine quality features (11 fields)
4. Click **Predict** to get the wine quality score
5. (Optional) Click **Train** to retrain the model with new data

### Using the Command Line

To run the full ML pipeline (data ingestion → training → evaluation):

```bash
python main.py
```

Output will be in:
- `artifacts/` - trained model and data
- `logs/` - execution logs
- `mlflow_runs/` - MLflow experiment tracking (if using local MLflow)

## Running the Project

### Option 1: Training & Evaluation (Command Line)

Train the model and evaluate it:

```bash
python main.py
```

This will:
1. Ingest data from `artifacts/data_ingestion/`
2. Validate data structure
3. Split data into train/test sets
4. Train the model
5. Evaluate and log metrics to MLflow

### Option 2: Interactive Web Interface (Flask App)

Start the Flask application to make predictions through a web browser:

```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:8080
```

**Available Routes:**
- `/` - Home page with input form
- `/train` - Trigger model training (takes ~1-2 minutes)
- `/predict` - Submit wine features and get quality prediction

### Making Predictions

Fill in the wine quality features:
- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

Click **Predict** to get the predicted wine quality score.

## Project Structure

```
DataScience_project/
├── src/datascience/
│   ├── components/          # ML pipeline components
│   ├── config/              # Configuration management
│   ├── constants/           # Constants and file paths
│   ├── entity/              # Data classes for configs
│   ├── pipeline/            # ML pipeline orchestration
│   └── utils/               # Utility functions
├── artifacts/               # Generated data and models
├── templates/               # HTML templates for Flask
├── config/config.yaml       # Configuration file
├── params.yaml              # Model parameters
├── schema.yaml              # Data schema validation
├── main.py                  # Training pipeline entry point
├── app.py                   # Flask web app entry point
└── requirements.txt         # Python dependencies
```

## Development Workflow

When modifying the pipeline, follow this workflow:

1. Update **`config/config.yaml`** with new paths or settings
2. Update **`params.yaml`** with new hyperparameters
3. Update **`schema.yaml`** if data structure changes
4. Update **`src/datascience/entity/config_entity.py`** with new config classes
5. Update **`src/datascience/config/configuration.py`** with new configuration managers
6. Update **`src/datascience/components/`** with new pipeline components
7. Update **`src/datascience/pipeline/`** with pipeline orchestration
8. Update **`main.py`** to call the new pipeline stages

## Troubleshooting

### Model File Not Found
If you get `FileNotFoundError: Model file not found`, run the training pipeline first:
```bash
python main.py
```

### MLflow Registry Error (403)
If you see "API request to endpoint /api/2.0/mlflow/registered-models/create failed with error code 403", the model is still logged but not registered. This is a non-fatal error related to MLflow permissions.

### scikit-learn Version Warning
Version mismatch warnings between sklearn versions are informational. Consider retraining the model if you update sklearn.

## Environment Variables (Optional)

### Local MLflow Tracking (Default)

By default, MLflow tracks experiments locally in `mlflow_runs/`. No setup needed.

### Using a Shared MLflow Server

If the project maintainer is running a shared MLflow server, set the tracking URI before running the pipeline:

**macOS/Linux:**
```bash
export MLFLOW_TRACKING_URI=http://<mlflow-server-ip>:5000
python main.py
```

**Windows (Command Prompt):**
```bash
set MLFLOW_TRACKING_URI=http://<mlflow-server-ip>:5000
python main.py
```

**Windows (PowerShell):**
```powershell
$env:MLFLOW_TRACKING_URI = "http://<mlflow-server-ip>:5000"
python main.py
```

Replace `<mlflow-server-ip>` with the actual IP address or hostname where MLflow is running.

### Example: Using a Remote MLflow Server

```bash
# If MLflow is running on 192.168.1.100:5000
export MLFLOW_TRACKING_URI=http://192.168.1.100:5000
python main.py
# Now all experiments will be logged to the shared MLflow server
```

You can then view experiments at: `http://<mlflow-server-ip>:5000`

## Environment Variables (Custom Configuration)

## Notes

- The dataset used is the **Wine Quality** dataset (red wine)
- Model: **ElasticNet** regression
- Test/train split: 75/25
- All logs are stored in the `logs/` directory
- Metrics and models are persisted in `artifacts/`

## License

See `LICENSE` file for details.

## Contact

For questions or issues, please reach out to the project maintainer.