import requests

data = {
    "Year_Birth": 1957,
    "Education": "Graduation",
    "Marital_Status": "Single",
    "Kidhome": 0,
    "Teenhome": 0,
    "Recency": 58,
    "NumWebVisitsMonth": 7,
    "AcceptedCmp3": 0,
    "AcceptedCmp4": 0,
    "AcceptedCmp5": 0,
    "AcceptedCmp1": 0,
    "AcceptedCmp2": 0,
    "Complain": 0,
    "Total_Purchases": 22
}

response = requests.post(
    "http://127.0.0.1:5000/predict",
    json=data
)

print(response.json())