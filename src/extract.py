import os
import kagglehub
import shutil

def extract_data():
    # Crée le dossier raw si non existant
    os.makedirs("data/raw", exist_ok=True)

    # Télécharge le dataset
    print("⬇️ Downloading dataset...")
    dataset_dir = kagglehub.dataset_download("elemento/nyc-yellow-taxi-trip-data")

    # Copie tout le contenu du dossier téléchargé dans data/raw
    for item in os.listdir(dataset_dir):
        s = os.path.join(dataset_dir, item)
        d = os.path.join("data/raw", item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    print("✅ Data copied successfully to data/raw!")

if __name__ == "__main__":
    extract_data()