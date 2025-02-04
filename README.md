# Diapredict - Diabetes Prediction System
Diapredict is a machine learning-powered web application that predicts the likelihood of diabetes based on user input. It uses a Flask backend, an SVM classifier, and a simple frontend for user interaction.<br>

<b> User-friendly Interface:</b>  &nbsp;&nbsp;&nbsp;&nbsp;Simple form-based input.<br>
<b> Machine Learning Model: </b> &nbsp;&nbsp;&nbsp;&nbsp;Uses an SVM classifier for prediction.<br>
<b> Flask Backend:</b>  &nbsp;&nbsp;&nbsp;&nbsp;Handles user input and model inference.<br>
<b> Automated Data Processing:</b>  &nbsp;&nbsp;&nbsp;&nbsp;Prepares and normalizes input before prediction.<br>

## 📁 Project Structure

Diapredict/<br>
├── model/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;# Trained ML model and scaler <br>
├── templates/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # HTML templates (frontend)<br>
├── static/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # CSS and other static files<br>
├── app.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Main Flask application<br>
├── TEST.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Script to test the model<br>
├── diabetes.csv &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Dataset used for training<br>
├── requirements.txt &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Dependencies<br>
├── README.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # Project documentation<br>


## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
&nbsp;&nbsp;git clone https://github.com/MalaikaAhmed7/diapredict.git
&nbsp;&nbsp;cd diapredict
### 2️⃣ Create a Virtual Environment (Optional)
&nbsp;&nbsp;python -m venv venv <br>
&nbsp;&nbsp;source venv/bin/activate  # macOS/Linux<br>
&nbsp;&nbsp;venv\Scripts\activate     # Windows <br>
### 3️⃣ Install Dependencies
&nbsp;&nbsp;pip install -r requirements.txt
### 4️⃣ Run the Flask App
&nbsp;&nbsp;python app.py
### 🧪 Testing the Model
To test the model separately, run: <br>
python TEST.py

## Technologies Used

 &nbsp;&nbsp;<b>Python</b> (Flask, NumPy, Pandas)  <br>
 &nbsp;&nbsp;<b>Machine Learning</b> (SVM Classifier) <br>
 &nbsp;&nbsp;<b>HTML, CSS (Frontend), Bootstrap </b><br>
 &nbsp;&nbsp;<b>Pickle</b> (Model Serialization) <br>

## Contributors
&nbsp;&nbsp; <b> Frontend: </b> MALAIKA NISAR AHMED <br>
&nbsp;&nbsp;<b> Backend & Model:</b>  AMEER HAMZA<br>
&nbsp;&nbsp;<b> Documentation :</b>  ARFA SHAHBAZ<br>
