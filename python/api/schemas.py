from pydantic import BaseModel

class CustomerData(BaseModel):
    gender: str                 # "Male" ou "Female"
    SeniorCitizen: int          # 0 ou 1
    Partner: str                # "Yes" ou "No"
    Dependents: str             # "Yes" ou "No"
    tenure: int                 # Meses
    PhoneService: str           # "Yes" ou "No"
    MultipleLines: str          # "Yes", "No" ou "No phone service"
    InternetService: str        # "DSL", "Fiber optic" ou "No"
    OnlineSecurity: str         # "Yes" ou "No"
    OnlineBackup: str           # "Yes" ou "No"
    DeviceProtection: str       # "Yes" ou "No"
    TechSupport: str            # "Yes" ou "No"
    StreamingTV: str            # "Yes" ou "No"
    StreamingMovies: str        # "Yes" ou "No"
    Contract: str               # "Month-to-month", "One year" ou "Two year"
    PaperlessBilling: str       # "Yes" ou "No"
    PaymentMethod: str          # "Electronic check", "Mailed check", "Bank transfer (automatic)" ou "Credit card (automatic)"
    MonthlyCharges: float
    TotalCharges: float