# VRDL HW1 - Bird Images Classification
Selected Topics in Visual Recognition using Deep Learning - HW1

## Hardware and Requirements
Google Colab Notebook with GPU

## Reproducing Submission

### Dataset Download
Codalab and download public data: 
https://competitions.codalab.org/competitions/35668#participate-get_starting_kit<br>
<br>
Training image in the directory "training_images"
```
0003.jpg
0008.jpg...
```
Testing image in the directory "testing_images"
```
0001.jpg
0002.jpg...
```
Training labels in "training_labels.txt"
```
4283.jpg 115.Brewer_Sparrow
3982.jpg 162.Canada_Warbler
5836.jpg 144.Common_Tern ...
```
All bird species in "classes.txt"
```
001.Black_footed_Albatross
002.Laysan_Albatross
003.Sooty_Albatross...
```



### Training
In "VRDL_HW1.ipynb"<br>
The 1st to 8th kernels are data preprocessing.<br>
The 9th to 11th kernels will define model and train model.<br>
<br>
In this homework I use 4 models to get predict from testing data, so run the 1st kernels to 11th kernels 4 times.

### Evaluation
I split 200 image from 3000 training data as validation data.<br>
For each model, it will get accuracy around 66% to 70% on validation data.<br>
With four models ensembled, it will get 66% accuracy on testing data.

## Pre-trained model
https://drive.google.com/drive/folders/1FBJSirBWKEJAb-yMBe5uVzmChkkfnLOR?usp=sharing

