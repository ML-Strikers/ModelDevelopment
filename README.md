# TravelGuide

---

## Project Structure

```
TravelGuide/
├── app/                       # Actual project
│   ├── __init__.py            
│   ├── routes.py              
├── Database/                  # Database connections and functions
├── modelfiles/                # LLM fine-tuning
│   ├── financeAdvisor         # Finance planner model training
│   ├── travelPlanner          # Travel planner model training
│   ├── customerSupport        # Customer support model training
├── models/                    # Model functions
│   ├── __init__.py            
│   ├── customerSupport.py     
│   ├── financeAdvisor.py      
│   ├── travelPlanning.py      
├── tests/                     # Unit tests
│── imports.py                 # All imports
│── run.py                     # Final execution
│── .env                       # Environment variables
```

---

## Project Setup

### **1. Create a Virtual Environment**
Run the following command to set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```

### **2. Install Dependencies**
Ensure all required dependencies are installed:
```bash
pip install -r requirements.txt
```

---

## Model Setup

The AI models are fine-tuned using **Ollama** for various functionalities:

### **Fine-tune and Prepare the Models**
```bash
ollama create finance-advisor -f ./TravelGuide/modelfiles/financeAdvisor
ollama create travel-planner -f ./TravelGuide/modelfiles/travelPlanner
ollama create customer-support -f ./TravelGuide/modelfiles/customerSupport
```

---

## Running the Application

To start the application, run:
```bash
python run.py
```

## Notes
This project is currently under development.

