from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

income_model = joblib.load("models/income_model.pkl")
spending_model = joblib.load("models/spending_model.pkl")
ohe = joblib.load("models/encoder.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_columns = joblib.load("models/features_names.pkl")

print("===== FEATURE COLUMNS =====")
print(feature_columns)
print("Count:", len(feature_columns))

print("\n===== SCALER FEATURES =====")
print(scaler.feature_names_in_)
print("Count:", len(scaler.feature_names_in_))

# categorical columns (same as training)
cat_cols = ["Education", "Marital_Status"]

@app.route("/")
def home():
    return {
        "message": "ML Prediction API Running 🚀",
        "endpoint": "/predict (POST)"
    }
def preprocess(data):

    df = pd.DataFrame([data])

    cat_data = df[cat_cols]
    num_data = df.drop(cat_cols, axis=1)

    cat_encoded = ohe.transform(cat_data)
    cat_encoded_df = pd.DataFrame(
        cat_encoded,
        columns=ohe.get_feature_names_out(cat_cols)
    )

    final_df = pd.concat(
        [num_data.reset_index(drop=True),
         cat_encoded_df.reset_index(drop=True)],
        axis=1
    )

    final_df = final_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    final_df = scaler.transform(final_df)

    return final_df
    
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "GET":
        return {"message": "Use POST with JSON"}
    try:
        data = request.get_json()

        processed = preprocess(data)

        income_pred = income_model.predict(processed)
        spending_pred = spending_model.predict(processed)

        return jsonify({
            "income_prediction": float(income_pred[0]),
            "spending_prediction": float(spending_pred[0])
        })

    except Exception as e:
        return jsonify({"error": str(e)})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)


