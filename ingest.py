# run_once_ingest.py
import os
from embedchain import App
from dotenv import load_dotenv
load_dotenv()




# === INIT APP ===
app = App.from_config(config_path="config.yaml")

# === CSV FILES ===
json_folder = r"Chatbot\json"
for file in os.listdir(json_folder):
    if file.endswith(".json"):
        csv_path = os.path.join(json_folder, file)
        app.add(csv_path, data_type="json")

# === TXT FILES ===


# === AUDIO FILES ===


print("✅ All documents ingested (CSV, TXT, AUDIO). You may now run the query interface.")
