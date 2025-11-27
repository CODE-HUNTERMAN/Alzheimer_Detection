# Alzheimer's Disease Classifier

This project aims to find out if an MRI scan is Alzheimer's disease or not.
It is classified according to four different stages of Alzheimer's disease.
1. Non Demented
2. Very Mild Demented
3. Mild Demented
4. Moderate Demented

The technical purpose of this project is about to testing different deep learning models for Alzheimer's diagnosis.

Firstly, we've tested CNN, InceptionV3, ResNet50, VGG16 and DenseNet121 models using [Alzheimer's Dataset (4 class of Images)](https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images).
Then, according to results, we decided to improve our CNN model and change our dataset because it was not clarified.

We improved our CNN model and we named it **"Custom CNN"**. 


### Results

| Model             	| Accuracy 	|
|-------------------	|----------	|
| Custom CNN            | %98.18  	|
| CNN            	| %86.48  	|
| DenseNet121       	| %88.36 	|
| InceptionV3       	| %76.80  	|
| ResNet50          	| %78.20   	|
| VGG16             	| %79.45  	|

----

### Conclusion
**Confusion Matrix**

![image](https://user-images.githubusercontent.com/58422765/169306836-8d0d7cd3-f86a-4ad6-90c4-1afaf7b7ec1e.png)

The classifier made a total of 1600 predictions.
* In reality, 827 patients in the sample is "Non Demented", but the classifier predicted 822 patients correctly.
* In reality, 527 patients in the sample is "Very Mild Demented", but the classifier predicted 515 patients correctly.
* In reality, 232 patients in the sample is "Mild Demented", but the classifier predicted 220 patients correctly.
* In reality, 14 patients in the sample is "Moderate Demented", and the classifier predicted all patients correctly.

**Accuracy on test data :  %98.18**

**According to results, we see that Custom CNN model is trained properly and tested well.**

----

### Dataset
* [Alzheimer MRI Preprocessed Dataset](https://www.kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset/data/discussion)
    * The data is collected from several websites, hospitals, and public repositories. 
    * The dataset is consists of Preprocessed MRI (Magnetic Resonance Imaging) Images.
    * All the images are resized into 128 x 128 pixels.

## Repository Structure
```
.
├── images
├── Models
│   ├── CNN
│   └── Custom CNN
│   └── DenseNet121
│   └── InceptionV3
│   └── RestNet50
│   └── VGG16
├── alzheimer-detection.ipynb
├── Requirements.txt
├── app2.py                  
├── README.md   

```

![acc_ss](https://user-images.githubusercontent.com/71088263/233706569-3809db9a-6d9a-4697-86b2-75b7068e7825.png)

![loss_ss](https://user-images.githubusercontent.com/71088263/233706642-b277f939-f8d8-41ae-89d6-3ad036ea575b.png)

Then I have saved the model in h5 file format and the loaded it in a streamlit app to make the model accesible to users. 
![image](https://user-images.githubusercontent.com/71088263/233707755-ce40e927-6518-41fd-a756-242150f332bc.png)

The form is completely validated. 
![output1](https://user-images.githubusercontent.com/71088263/233706839-fc05612d-2924-49c4-b5aa-024ce64fbde0.png)


After submitting your details the web app generates a pdf report using fpdf and your data gets stored in a mysql database
