import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
from streamlit_option_menu import option_menu
import re
import base64
from fpdf import FPDF
import sqlite3

# ---------- DATABASE SETUP ----------
def get_db_connection():
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Patient_Name TEXT,
            Age INTEGER,
            Gender TEXT,
            Contact TEXT,
            Prediction TEXT
        )
    ''')
    conn.commit()
    return conn, cursor

# ---------- BACKGROUND IMAGE ----------
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-position: center;
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./images/bg3.png')

# ---------- LOAD MODEL ----------
model = tf.keras.models.load_model('model.h5')
class_labels = ['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very Mild Demented']

def preprocess_image(image):
    image = image.convert('RGB')
    image = image.resize((176, 176))
    image = np.array(image)/255.0
    image = np.expand_dims(image, axis=0)
    return image

# ---------- INPUT VALIDATION ----------
def validate_phone_number(phone_number):
    if not re.match(r'^\d{10}$', str(phone_number)):
        st.error('Please enter a 10 digit number!')
        return False
    return True

def validate_name(name):
    if not all(char.isalpha() or char.isspace() for char in name):
        st.error("Name should not contain numbers or special characters.")
        return False
    return True

def validate_input(name, age, contact, file):
    if not name:
        st.error('Please enter the patient\'s name!')
        return False
    if not age:
        st.error('Please enter age!')
        return False
    if not contact:
        st.error('Please enter contact number!')
        return False
    if not file:
        st.error('Please upload the MRI scan!')
        return False
    return True

# ---------- OPTION MENU ----------
selected = option_menu(
    menu_title=None,
    options=["Home", "Alzheimer Detection", "About US"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# ---------- HOME ----------
if selected == 'Home':
    st.title("Alzheimer's Disease")
    st.write("Alzheimer disease is the most common type of dementia...")
    st.write("Stages:")
    st.write("1. Mild Demented\n2. Very Mild Demented\n3. Moderate Demented\n4. Non Demented")

# ---------- ABOUT US ----------
elif selected == 'About US':
    st.title('Welcome!')
    st.write('This web app uses a CNN model to recognize Alzheimer\'s disease...')
    st.write('MINI Project by Shubham Shinde')

# ---------- ALZHEIMER DETECTION ----------
elif selected == 'Alzheimer Detection':
    st.title('Alzheimer Detection Web App')
    st.write('Please enter your details and upload MRI scan.')

    conn, cursor = get_db_connection()  # SQLite DB

    with st.form(key='myform', clear_on_submit=True):
        name = st.text_input('Name')
        age = st.number_input('Age', min_value=1, max_value=150, value=40)
        gender = st.radio('Gender', ('Male', 'Female','Other'))
        contact = st.text_input('Contact Number', value='', key='contact')
        file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])
        submit = st.form_submit_button("Submit")

        if submit:
            if validate_input(name, age, contact, file) and validate_phone_number(contact) and validate_name(name):
                st.success('Your information has been recorded.', icon="✅")
                image = Image.open(file)
                st.image(image, caption='Uploaded Image', width=200)
                image_processed = preprocess_image(image)
                prediction = model.predict(image_processed)
                prediction = np.argmax(prediction, axis=1)
                st.success('Predicted class: '+ class_labels[prediction[0]])

                # Insert into SQLite DB
                cursor.execute(
                    "INSERT INTO predictions (Patient_Name, Age, Gender, Contact, Prediction) VALUES (?, ?, ?, ?, ?)",
                    (name, age, gender, contact, class_labels[prediction[0]])
                )
                conn.commit()

                # PDF Export
                export_as_pdf = st.button("Export Report")
                if export_as_pdf:
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font('Times', 'B', 24)
                    pdf.cell(200, 20, 'Alzheimer Detection Report', 0, 1, 'C')
                    pdf.set_font('Arial', '', 12)
                    pdf.cell(200, 10, f'Name: {name}', 0, 1)
                    pdf.cell(200, 10, f'Age: {age}', 0, 1)
                    pdf.cell(200, 10, f'Gender: {gender}', 0, 1)
                    pdf.cell(200, 10, f'Contact: {contact}', 0, 1)
                    image.save("image.png")
                    pdf.image("image.png", x=40, y=80, w=50, h=50)
                    pdf.set_font('Arial', 'B', 16)
                    pdf.cell(200, 10, f'Prediction: {class_labels[prediction[0]]}', 0, 1)
                    pdf_bytes = pdf.output(dest='S').encode('latin-1')
                    b64 = base64.b64encode(pdf_bytes).decode()
                    href = f'<a href="data:application/octet-stream;base64,{b64}" download="report.pdf">Download PDF</a>'
                    st.markdown(href, unsafe_allow_html=True)

    conn.close()
