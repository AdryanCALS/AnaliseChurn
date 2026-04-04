from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import joblib
import pandas as pd
from schemas import CustomerData

app = FastAPI(title="Churn Prediction API", 
              description="API for churn prediction using a pretrained model", 
              version="1.0"
              )
model = joblib.load("modelo_treinado.pkl")

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

def preprocess_input(cliente: CustomerData) -> pd.DataFrame:
    """Função para pré-processar os dados de entrada antes de fazer a previsão"""
    
    def yes_no(value):
        if value in ["No", "No Internet Service", "No phone service"]:
            return 0
        return 1 if value == "Yes" else 0
    
    dados_formatados = {
        'gender': 1 if cliente.gender == "Male" else 0,
        'SeniorCitizen': cliente.SeniorCitizen,
        'Partner': yes_no(cliente.Partner),
        'Dependents': yes_no(cliente.Dependents),
        'tenure': cliente.tenure,
        'PhoneService': yes_no(cliente.PhoneService),
        'MultipleLines': yes_no(cliente.MultipleLines),
        'OnlineSecurity': yes_no(cliente.OnlineSecurity),
        'OnlineBackup': yes_no(cliente.OnlineBackup),
        'DeviceProtection': yes_no(cliente.DeviceProtection),
        'TechSupport': yes_no(cliente.TechSupport),
        'StreamingTV': yes_no(cliente.StreamingTV),
        'StreamingMovies': yes_no(cliente.StreamingMovies),
        'PaperlessBilling': yes_no(cliente.PaperlessBilling),
        'MonthlyCharges': cliente.MonthlyCharges,
        'TotalCharges': cliente.TotalCharges,
        
        # Simulando o get_dummies (One-Hot Encoding)
        'InternetService_Fiber optic': 1 if cliente.InternetService == "Fiber optic" else 0,
        'InternetService_No': 1 if cliente.InternetService == "No" else 0,
        
        'Contract_One year': 1 if cliente.Contract == "One year" else 0,
        'Contract_Two year': 1 if cliente.Contract == "Two year" else 0,
        
        'PaymentMethod_Credit card (automatic)': 1 if cliente.PaymentMethod == "Credit card (automatic)" else 0,
        'PaymentMethod_Electronic check': 1 if cliente.PaymentMethod == "Electronic check" else 0,
        'PaymentMethod_Mailed check': 1 if cliente.PaymentMethod == "Mailed check" else 0
    }
    
    return pd.DataFrame([dados_formatados])
    
@app.post("/predict")
def predict_churn(data: CustomerData):
    
    # Converte os dados de entrada para um DataFrame
    input_data = preprocess_input(data)
    
    # Realiza a previsão usando o modelo carregado
    probability = model.predict_proba(input_data)[:, 1][0] # Probabilidade de churn
    cancel = int(probability >= 0.7) # baseaedo nas nossas regras de negócio do modelo
    
    return {
        "churn_probability": float(probability),
        "cancel": cancel,
        "mensagem": "Alto risco de cancelamento" if cancel == 1 else "Cliente estável"
    }