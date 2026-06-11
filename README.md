# FinSight AI – Customer Income & Spending Prediction System

FinSight AI is an end-to-end Machine Learning application that predicts customer income and spending behavior using demographic and financial data. The project demonstrates the complete ML lifecycle, including data preprocessing, model training, API development, containerization, and deployment.

## Features

* Customer Income Prediction
* Customer Spending Prediction
* End-to-End Machine Learning Pipeline
* REST API built with Flask
* Dockerized for portable deployment
* Cloud-ready deployment architecture

## Tech Stack

* Python
* Scikit-learn
* XGBoost
* Random Forest
* Flask
* Docker

## Machine Learning Workflow

1. Data Collection & Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training
5. Hyperparameter Tuning
6. Model Evaluation
7. API Development
8. Containerization & Deployment

## Model Performance

| Model         | Task                | Performance |
| ------------- | ------------------- | ----------- |
| XGBoost       | Income Prediction   | R² > 0.80   |
| Random Forest | Spending Prediction | R² > 0.80   |

## Project Structure

```text
FinSight-AI/
│
├── app.py
├── dockerfile
├── models.ipynb
├── requirements.txt
├── test_api.py
├── .gitignore
└── README.md

## Installation

```bash
git clone https://github.com/your-username/finsight.git
cd finsight
pip install -r requirements.txt
```

## Run Locally

```bash
python app.py
```

## Run with Docker

Build Image

```bash
docker build -t finsight .
```

Run Container

```bash
docker run -p 5000:5000 finsight
```

## API Usage

### Prediction Endpoint

```http
POST /predict
```

Example Request

```json
{
  "age": 35,
  "occupation": "Engineer",
  "annual_income": 75000
}
```

Example Response

```json
{
  "predicted_income": 78250,
  "predicted_spending": 32450
}
```

## Future Improvements

* User Authentication
* Interactive Dashboard
* Real-time Monitoring
* MLOps Pipeline Integration
* Automated Retraining

## Author

Suyash Verma

GitHub: https://github.com/suyashverma0
Docker:https://hub.docker.com/repository/docker/suyashh021/finsight/general
