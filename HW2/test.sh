#!/bin/bash
./darknet detector test data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj_last.weights -dont_show -ext_output -out result.json < data/test_speed.txt