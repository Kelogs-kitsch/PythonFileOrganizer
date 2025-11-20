# PythonFileOrganizer
Project Description

The Python File Organizer is a script that automatically organizes files in a folder into categorized subfolders based on their file types. It handles duplicates, creates necessary folders if missing, and logs all file movements. This project demonstrates Python automation, file handling, and console logging.
Features

Automatically organizes files by type:

Images: .jpg, .jpeg, .png, .gif, .bmp

Documents: .pdf, .docx, .doc, .txt, .xlsx, .pptx

Audio: .mp3, .wav, .aac

Videos: .mp4, .mkv, .avi, .mov

Archives: .zip, .rar, .tar, .gz

Files with unrecognized extensions are moved to an Others folder.

Automatically creates required folders if they do not exist.

Handles duplicate filenames by appending (1), (2), etc.

Prints all file movements to the console.

Project Structure
PythonFileOrganizer/
│
├── organizer.py       # Main Python script
├── files/             # Folder containing files to organize
│   ├── file1.pdf
│   ├── file2.jpg
│   └── file3.txt
└── README.md

Installation

Make sure Python is installed (Python 3.x recommended).

Clone the repository:

git clone https://github.com/Kelogs-kitsch/PythonFileOrganizer.git


Navigate to the project folder:

cd PythonFileOrganizer

Usage

Place the files you want to organize in the files folder.

Run the script:

python organizer.py


Observe the console logs showing how files are moved.

Check the files folder – files will now be organized into subfolders.

Example Console Output
Created folder: files
Created folder: files/Documents
Moved file1.pdf → Documents/file1.pdf
Created folder: files/Images
Moved file2.jpg → Images/file2.jpg
Moved file3.txt → Documents/file3.txt
All files have been organized successfully!

Technologies Used

Python – Core language

os module – File system operations

shutil module – Move files between folders

Future Improvements

Add a GUI interface for non-technical users.

Add drag-and-drop functionality for selecting folders.

Organize files based on creation date or size.
