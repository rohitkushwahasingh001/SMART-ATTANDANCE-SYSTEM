# Facial Recognition Attendance System (Tkinter Version)

This is a Python-based **Facial Recognition Attendance System** built using **Tkinter** for GUI, **OpenCV** for face recognition, and **MySQL** for storing student information. It captures facial images, trains a recognition model, and marks attendance based on recognized faces.

## 🚀 Features

- GUI built using Tkinter
- Student registration form (with department, course, name, etc.)
- Capture 50 facial images per student
- Train model using captured images
- Real-time face recognition via webcam
- Attendance saved in `attendance.csv`
- Import and view attendance logs

## 🧰 Technologies Used

- Python
- OpenCV
- Tkinter
- MySQL (via `mysql-connector-python`)
- CSV for attendance storage

## 📁 Project Structure

```
facial_recognition_attendance_system/
│
├── student_details.py          # Student registration & image capture
├── train.py                    # Train recognizer and generate classifier.xml
├── facial_recognition.py       # Webcam-based real-time face recognition
├── attendance.py               # View/Import attendance from CSV
├── data/                       # Folder containing captured face images
├── classifier/                 # Contains classifier.xml file
├── attendance.csv              # Attendance logs
└── database_config.py          # MySQL database connection config
```

## 🛠 Setup Instructions

1. **Install Required Libraries**
   ```bash
   pip install opencv-python mysql-connector-python
   ```

2. **Create MySQL Database**

   Create a database named `face_recognition` and a table named `student_detail` with fields:

   ```sql
   CREATE TABLE student_detail (
       student_id INT PRIMARY KEY,
       name VARCHAR(45),
       email VARCHAR(45),
       gender VARCHAR(45),
       phone VARCHAR(45),
       address VARCHAR(45),
       guardian VARCHAR(45),
       dob VARCHAR(45),
       dep VARCHAR(45),
       course VARCHAR(45),
       year VARCHAR(45),
       semester VARCHAR(45),
       teacher VARCHAR(45),
       eno VARCHAR(45),
       photosample VARCHAR(45)
   );
   ```

3. **Run the Application**

   - Open `student_details.py` to register a student and capture photos.
   - Run `train.py` to train and generate `classifier.xml`.
   - Use `facial_recognition.py` to recognize faces and mark attendance.
   - Use `attendance.py` to view and manage attendance logs.

## 📸 How Attendance Works

1. Student registers and takes 50 photos.
2. Model is trained using these photos to create `classifier.xml`.
3. During attendance, webcam matches face with trained data.
4. Recognized students are marked present in `attendance.csv`.

## 🙋‍♂️ Author

**Rohit Kushwaha**
