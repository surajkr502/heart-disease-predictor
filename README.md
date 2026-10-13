# Heart Disease Predictor

A machine learning web application that estimates the probability of heart disease from a patient's clinical data. It uses a trained scikit-learn pipeline, a FastAPI backend, and an HTML/CSS/JavaScript frontend.

> **Disclaimer:** This project is for educational purposes only. It is not a medical device and must not be used to diagnose, treat, or prevent any medical condition. Always consult a qualified healthcare professional for medical advice.

## Live Demo

- **Live App:** https://heart-disease-predictor-pifd.onrender.com/
- **Health Check:** https://heart-disease-predictor-pifd.onrender.com/api/health
- **API Documentation:** https://heart-disease-predictor-pifd.onrender.com/docs

The health-check endpoint should return:

```json
{"status": "ok"}
```

## Features

- Web form for entering patient information such as age, blood pressure, cholesterol, ECG results, and maximum heart rate
- Returns a heart disease probability and a binary prediction label
- Input validation using Pydantic
- Health-check endpoint
- Interactive API documentation with Swagger UI
- Loads the trained model when the application starts

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI, Uvicorn |
| Validation | Pydantic |
| Machine Learning | scikit-learn, pandas, NumPy, joblib |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render |

## Project Structure

```text
heart-disease-predictor/
├── api/
│   └── index.py              # FastAPI application and prediction endpoints
├── model/
│   └── heart_model.joblib    # Trained scikit-learn pipeline
├── public/
│   └── index.html            # Frontend form
├── requirements.txt          # Python dependencies
└── README.md
```

## How It Works

1. A machine learning pipeline is trained offline and saved as `heart_model.joblib`.
2. The FastAPI application loads the saved model.
3. The user enters clinical values in the web form.
4. The frontend sends the form data as JSON to `POST /api/predict`.
5. The backend validates the input, creates a pandas DataFrame, runs the model, and returns the predicted probability and class.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the web form |
| `GET` | `/api/health` | Health check; returns `{"status": "ok"}` |
| `POST` | `/api/predict` | Returns probability and prediction |
| `GET` | `/docs` | Interactive Swagger API documentation |

### Example request

Send this JSON body to `POST /api/predict`:

```json
{
  "Age": 54,
  "Sex": "M",
  "ChestPainType": "ASY",
  "RestingBP": 140,
  "Cholesterol": 239,
  "FastingBS": 0,
  "RestingECG": "Normal",
  "MaxHR": 160,
  "ExerciseAngina": "N",
  "Oldpeak": 1.2,
  "ST_Slope": "Flat"
}
```

### Input fields

| Field | Type | Expected values / notes |
|---|---|---|
| `Age` | Integer | 1–120 |
| `Sex` | String | `M` or `F` |
| `ChestPainType` | String | `ATA`, `NAP`, `ASY`, or `TA` |
| `RestingBP` | Number | Resting blood pressure; must not be `0` |
| `Cholesterol` | Number | Serum cholesterol |
| `FastingBS` | Integer | `0` or `1` |
| `RestingECG` | String | `Normal`, `ST`, or `LVH` |
| `MaxHR` | Integer | Maximum heart rate achieved |
| `ExerciseAngina` | String | `N` or `Y` |
| `Oldpeak` | Number | ST depression value |
| `ST_Slope` | String | `Up`, `Flat`, or `Down` |

### Example success response

```json
{
  "heart_disease_probability": 0.7812,
  "prediction": 1,
  "disclaimer": "For educational purposes only. Not medical advice."
}
```

`prediction` is `1` when the model's probability is at least `0.5`, otherwise it is `0`. This threshold is a project default, not a clinically validated decision threshold.

## Dataset Source

The project uses the [Heart Failure Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction).

- **Dataset creator:** Fedesoriano
- **Target column:** `HeartDisease`

Please check the Kaggle page for the dataset's license and usage terms.

## Getting Started (Local Setup)

### Prerequisites

- Python installed
- `pip`

### 1. Clone the repository

```bash
git clone https://github.com/surajkr502/heart-disease-predictor.git
cd heart-disease-predictor
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```bat
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure the scikit-learn version in your environment is compatible with the version used to train and save `heart_model.joblib`. Loading a model with a different scikit-learn version may cause warnings or errors.

### 4. Start the server

Run this command from the project root:

```bash
uvicorn api.index:app --reload
```

### 5. Open the application

- Web form: http://127.0.0.1:8000/
- API docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/api/health

## Deployment on Render

This project is deployed on Render:

**Live URL:** https://heart-disease-predictor-pifd.onrender.com/

To deploy your own copy:

1. Push the project to a GitHub repository.
2. In the [Render Dashboard](https://dashboard.render.com/), create a new **Web Service** and connect the repository.
3. Choose the appropriate Python runtime for your dependencies.
4. Set the build command to:

   ```bash
   pip install -r requirements.txt
   ```

5. Set the start command to:

   ```bash
   uvicorn api.index:app --host 0.0.0.0 --port $PORT
   ```

6. Deploy the service and open the URL provided by Render.

Ensure the trained model file exists at `model/heart_model.joblib` in the deployed repository and that all required dependencies are listed in `requirements.txt`.

## Known Limitations

- The default decision threshold is `0.5`; it has not been clinically validated or tuned for a medical use case.
- A cholesterol value of `0` can represent missing data in the source dataset; the current backend does not reject it.
- The application is an educational demo and is not suitable for clinical decision-making.
- Automated tests are not currently documented in this repository.

## Future Improvements

- Add automated API tests using `pytest` and FastAPI's `TestClient`
- Add logging and robust error handling around model inference
- Add loading and network-error states to the frontend
- Move validation/business rules into Pydantic validators
- Evaluate model performance using metrics such as ROC-AUC, precision, and recall
- Document the model-training workflow and reproducibility steps

## Contributing

Contributions are welcome. For major changes, please open an issue to discuss the proposed change first.

## License

This project states that it uses the MIT License. Ensure a `LICENSE` file containing the MIT License is included in the repository if you intend to publish it under that license.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [scikit-learn](https://scikit-learn.org/)
- [Heart Failure Prediction Dataset — Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
