# Alzheimer_Detection 🧠
Leveraging MRI scans to detect Alzheimer's disease using CNN and vision transformers, aimed at enhancing diagnostic accuracy and supporting early intervention.

The app is live here: https://detect-alzheimer.streamlit.app/

## Introduction
This repository contains a deep learning framework designed to detect Alzheimer's disease using MRI scan images. The project aims to assist radiologists and medical professionals in early diagnosis through automated image analysis.

## Project Description
Alzheimer's disease is a progressive neurodegenerative disorder where early diagnosis is pivotal yet challenging. MRI scans are vital for detecting cerebral structural changes indicative of Alzheimer's. This project utilizes advanced deep learning architectures, including CNN based ResNet-50, EfficientNet, and Vision Transformers, which are trained, validated, and tested on a dataset of MRI scans to discern intricate patterns linked to the disease.

This project consists of two main parts:

PyTorch Modeling: Jupyter notebooks that contain the modeling work using PyTorch, including the creation, training, and validation of a CNN model, EfficientNet model and vision transformer for alzheimer's disease detection.
Streamlit App: The model was deployed on streamlit and is available for use.


## Repository Structure
```
.
├── Data
├── Models
│   ├── alzheimer_cnn_model.pth       # CNN model for Alzheimer's detection
│   └── alzheimer_efficientnet_model.pth  # EfficientNet model for Alzheimer's detection
├── Notebooks
│   ├── alzheimer-detection.ipynb     # Main Jupyter notebook for the project
│   └── data_explore.ipynb            # Notebook for data exploration and visualization
├── README.md   
├── Requirements.txt
├── Src
│   ├── alzheimer_efficientnet_model.pth  # Model file (duplicate, should review)
│   └── app.py                         # Streamlit application for deploying the model
└── Visualizations
    └── class_distribution.png        # Visualization of the dataset class distribution
```


I have built a cnn model to detect the presence of dementia in a patient's MRI Scans. The accuracy the model achieved was 93.75% and data loss was seen to be 22.17%

![acc_ss](https://user-images.githubusercontent.com/71088263/233706569-3809db9a-6d9a-4697-86b2-75b7068e7825.png)

![loss_ss](https://user-images.githubusercontent.com/71088263/233706642-b277f939-f8d8-41ae-89d6-3ad036ea575b.png)

Then I have saved the model in h5 file format and the loaded it in a streamlit app to make the model accesible to users. 
![image](https://user-images.githubusercontent.com/71088263/233707755-ce40e927-6518-41fd-a756-242150f332bc.png)

The form is completely validated. 
![output1](https://user-images.githubusercontent.com/71088263/233706839-fc05612d-2924-49c4-b5aa-024ce64fbde0.png)


After submitting your details the web app generates a pdf report using fpdf and your data gets stored in a mysql database
