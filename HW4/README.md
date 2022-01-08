# VRDL HW4 - Image super resolution
Selected Topics in Visual Recognition using Deep Learning - HW4

## Hardware and Requirements
### Hardware
NVDIA GeForce RTX 3050 Laptop GPU
### Requirements
* Python 3 (Anaconda is recommended)
* skimage
* imageio
* Pytorch (Pytorch version >=0.4.1 is recommended)
* tqdm
* pandas
* cv2 (pip install opencv-python)
* Matlab

## Reproducing Submission 

### Dataset Download
Download public data on newE3 <br>

Training image and mask in the directory "training_hr_images"
```
training_hr_images
    |-training_hr_images
        |-2092.png....
```
Testing image in the directory "testing_lr_images"
```
testing_lr_images
    |-testing_lr_images
        |-00.png....
```


### Model and data preparation 
#### model preparation
Clone the SRFBN by following command
```
git clone https://github.com/Paper99/SRFBN_CVPR19.git
```

#### data preparation
Put the dataset into SRFBN_CVPR19 and run src\Prepare_TrainData_HR_LR.m, you will get 2910 pairs of data from 291 high resolution images provided by TA.


### Training
Put src\train_SRFBN_example.json into SRFBN_CVPR19\options\train<br>Run following command
```
python test.py -opt options/test/test_SRFBN_example.json
```

### Evaluation
It will automatically select validation data and calculate loss and PSNR to each epoch<br>

### Generate Result
Set the path to your testing data and the model first or you can directly clone src\test_SRFBN_example.json to SRFBN_CVPR19\options\test, and replace SRFBN_CVPR19\test.py to src\test.py then run following command
```
python test.py -opt options/test/test_SRFBN_example.json
```
You will get super resolution images in results\SR\MyImage\SRFBN\x3


## Pre-trained weight
[HW4 model weight](https://drive.google.com/drive/folders/1IILl5pKeX46MdkrotQ7ISGtZWpdVPCyi?usp=sharing)

## Reference
SRFBN: https://github.com/Paper99/SRFBN_CVPR19 


###### tags: `VRDL`
