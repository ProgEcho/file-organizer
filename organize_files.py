import os
import shutil


downloads_folder = "C:/Users/DeinBenutzername/Downloads" # Ändere dies auf deinen Benutzernamen!

folders = {
    "Bilder": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Dokumente": [".docx",".doc" ".txt"],
    "Excel": [".xlsx", ".csv"],
    "Anwendungen":[".exe"],
    "Videos": [".mp4", ".avi"],
    "Musik": [".mp3", ".wav"],
    "Anderes":[".rar",".zip"]
}

for folder_name in folders:
    folder_path = os.path.join(downloads_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        
        for folder_name, extensions in folders.items():
            if file_extension in extensions:
                destination_folder = os.path.join(downloads_folder, folder_name)
                shutil.move(file_path, destination_folder)
                print(f"Verschoben: {filename} → {folder_name}")
                break