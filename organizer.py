import os
import shutil

# Step 1: Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

# Step 2: Function to create folder if not exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

# Step 3: Function to handle duplicate file names
def get_unique_filename(folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename
    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{base}({counter}){ext}"
        counter += 1
    return new_name

# Step 4: Main function to organize files
def organize_files(folder_path):
    # Step 4a: Create folder if missing
    create_folder(folder_path)

    # Step 4b: Loop through files
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False

        # Check categories
        for category, extensions in file_types.items():
            if ext in extensions:
                category_path = os.path.join(folder_path, category)
                create_folder(category_path)

                new_filename = get_unique_filename(category_path, filename)
                shutil.move(file_path, os.path.join(category_path, new_filename))
                print(f"Moved {filename} → {category}/{new_filename}")
                moved = True
                break

        # If file did not match any category
        if not moved:
            others_path = os.path.join(folder_path, "Others")
            create_folder(others_path)

            new_filename = get_unique_filename(others_path, filename)
            shutil.move(file_path, os.path.join(others_path, new_filename))
            print(f"Moved {filename} → Others/{new_filename}")

# Step 5: Run the organizer
if __name__ == "__main__":
    folder_to_organize = "files"  # Folder containing files to organize
    organize_files(folder_to_organize)
    print("All files have been organized successfully!")
