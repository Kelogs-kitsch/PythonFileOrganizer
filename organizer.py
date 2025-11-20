import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

# Step 1: Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

# Step 2: Create folder if it doesn't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

# Step 3: Handle duplicate filenames
def get_unique_filename(folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename
    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{base}({counter}){ext}"
        counter += 1
    return new_name

# Step 4: Log file movements
def log_file_move(original_path, new_path):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - Moved: {original_path} -> {new_path}\n")

# Step 5: Remove empty folders
def remove_empty_folders(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Removed empty folder: {dir_path}")
                with open("log.txt", "a") as log_file:
                    log_file.write(f"{datetime.now()} - Removed empty folder: {dir_path}\n")

# Step 6: Organize files
def organize_files(folder_path):
    create_folder(folder_path)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False

        for category, extensions in file_types.items():
            if ext in extensions:
                category_path = os.path.join(folder_path, category)
                create_folder(category_path)

                new_filename = get_unique_filename(category_path, filename)
                new_path = os.path.join(category_path, new_filename)
                shutil.move(file_path, new_path)
                print(f"Moved {filename} → {category}/{new_filename}")
                log_file_move(file_path, new_path)
                moved = True
                break

        if not moved:
            others_path = os.path.join(folder_path, "Others")
            create_folder(others_path)

            new_filename = get_unique_filename(others_path, filename)
            new_path = os.path.join(others_path, new_filename)
            shutil.move(file_path, new_path)
            print(f"Moved {filename} → Others/{new_filename}")
            log_file_move(file_path, new_path)

    # Remove empty folders after organizing
    remove_empty_folders(folder_path)

# Step 7: Run the organizer
if __name__ == "__main__":
    folder_to_organize = "files"  # Folder containing files to organize
    organize_files(folder_to_organize)
    print("All files have been organized successfully!")
