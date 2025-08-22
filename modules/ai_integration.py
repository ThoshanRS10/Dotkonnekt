# modules/ai_integration.py

import os
import requests
import json
import time

# --- Securely get the token from the environment ---
HF_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
if not HF_API_TOKEN:
    raise ValueError("Hugging Face API Token not found. Please set the HUGGINGFACE_API_TOKEN environment variable.")

HF_HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# --- Define API URLs for different models ---
TABLE_QA_API_URL = "https://api-inference.huggingface.co/models/google/tapas-base-finetuned-wtq"
TEXT_GEN_API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"


def query_huggingface_api(api_url, payload, retries=3, delay=10):
    """A robust function to query the Hugging Face API with retry logic."""
    for attempt in range(retries):
        response = requests.post(api_url, headers=HF_HEADERS, json=payload)
        
        # If successful, return the JSON
        if response.status_code == 200:
            return response.json()
        
        # If the model is loading, wait and retry
        elif response.status_code == 503:
            error_data = response.json()
            estimated_time = error_data.get('estimated_time', delay)
            print(f"Model is loading. Retrying in {estimated_time} seconds...")
            time.sleep(estimated_time)
        
        # For other errors, print them and break
        else:
            print(f"API request failed with status code {response.status_code}: {response.text}")
            return {"error": response.text, "status_code": response.status_code}
            
    return {"error": "Model failed to load after several retries."}


def ask_question_on_data(df, query):
    """Uses a Table Question-Answering model."""
    # Convert dataframe to the format required by the model
    table = df.astype(str).to_dict(orient='list')
    payload = {
        "inputs": {
            "query": query,
            "table": table
        }
    }
    result = query_huggingface_api(TABLE_QA_API_URL, payload)
    return result.get('answer', 'Sorry, I could not find an answer from the data.')


def get_ai_explanation(prompt):
    """Uses a powerful text-generation model to get an explanation."""
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 250, # Limit the length of the response
            "return_full_text": False, # Only return the generated part
            "temperature": 0.7
        }
    }
    result = query_huggingface_api(TEXT_GEN_API_URL, payload)
    
    if "error" in result:
        return f"There was an error generating the explanation: {result['error']}"
        
    # The response is a list, we take the first element's generated text
    return result[0].get('generated_text', 'Could not generate an explanation.')