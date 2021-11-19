# VRDL HW2 - SVHN detection
Selected Topics in Visual Recognition using Deep Learning - HW2

## Hardware and Requirements
Google Colab Notebook with GPU

## Reproducing Submission

### Dataset Download
Codalab and download public data: <br>https://competitions.codalab.org/competitions/35888#learn_the_details<br>

Training image in the directory "train"
```
1.png
10.png...
```
Testing image in the directory "test"
```
117.png
162.png...
```
Training labels in "train/digitStruct.mat"<br> Each bbox and number in each training image<br>

### Model and data preparation
#### model preparation
Run 1st kernel to mount drive.<br>Run 2nd to 4th kernel to git clone yolov4 and make file.<br>reference: https://github.com/AlexeyAB/darknet<br>Download pretrain weight [yolov4.conv.137](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137)and put it in folder "darknet" <br>and put [yolov4-obj.cfg](https://github.com/axde954e6/NYCU_VRDL/blob/main/HW2/yolov4-obj.cfg) into darknet/cfg.

#### data preparation
Clone "get_label.m" to train folder and run it.<br>You will get each training label with .txt file in train folder.<br>

```
1.txt
1 0.386640 0.532857 0.109312 0.625714
9 0.500675 0.544286 0.129555 0.625714

10.txt....
```
Each line in txt file means
```
<label> <x_center> <y_center> <width> <height>
```
"get_label.m" will convert label 10 to 0, which means number 0.<br><br>Put train and test folder into darknet/data<br>and put [obj.name](https://github.com/axde954e6/NYCU_VRDL/blob/main/HW2/obj.names) and [obj.data](https://github.com/axde954e6/NYCU_VRDL/blob/main/HW2/obj.data) into darknet/data <br><br>Run 5th to 14th kernel to generate train.txt, valid.txt and test.txt


### Training
Run 15th and 16th kernels to start your model training <br>
In this homework I use 4 models to get predict from testing data, so run the 1st kernels to 11th kernels 4 times.

### Evaluation
I split 200 image from 3000 training data as validation data.<br>
For each model, it will get accuracy around 66% to 70% on validation data.<br>
With four models ensembled, it will get 66% accuracy on testing data.

## Pre-trained model
https://drive.google.com/drive/folders/1FBJSirBWKEJAb-yMBe5uVzmChkkfnLOR?usp=sharing

