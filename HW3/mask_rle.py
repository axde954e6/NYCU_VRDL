import mask
import skimage.io as io
import os
import numpy
import json

img_name_to_id = {
    "TCGA-A7-A13E-01Z-00-DX1": 1,
    "TCGA-50-5931-01Z-00-DX1": 2,
    "TCGA-G2-A2EK-01A-02-TSB": 3,
    "TCGA-AY-A8YK-01A-01-TS1": 4,
    "TCGA-G9-6336-01Z-00-DX1": 5,
    "TCGA-G9-6348-01Z-00-DX1": 6
}

id_to_img_name = {
    1: "TCGA-A7-A13E-01Z-00-DX1",
    2: "TCGA-50-5931-01Z-00-DX1",
    3: "TCGA-G2-A2EK-01A-02-TSB",
    4: "TCGA-AY-A8YK-01A-01-TS1",
    5: "TCGA-G9-6336-01Z-00-DX1",
    6: "TCGA-G9-6348-01Z-00-DX1"
}

path = "/content/gdrive/MyDrive/Mask_RCNN/Mask_RCNN/results/mask"
read_json_path = "/content/gdrive/MyDrive/Mask_RCNN/Mask_RCNN/"
read_json_path += "results/nucleus/submit_20211129T165203/answer.json"
save_json_path = "/content/gdrive/MyDrive/Mask_RCNN/answer.json"
with open(read_json_path, 'r') as fin:
    read_json = json.load(fin)

order = []
for tmp in read_json:
    if id_to_img_name[tmp["image_id"]] not in order:
        order.append(id_to_img_name[tmp["image_id"]])

ans_list = []
now = 0
for tmp in order:
    png_list = os.listdir(path + "/" + tmp)
    png_list.sort()
    for item in png_list:
        mask_format = read_json[now].copy()
        file = path + "/" + tmp + "/" + item
        print(item)
        print("{} {}".format(mask_format["image_id"], now))
        I = io.imread(file)
        I = numpy.asfortranarray(I)
        rle = mask.encode(I)
        mask_format["bbox"] = numpy.ndarray.tolist(mask.toBbox(rle))
        rle["counts"] = rle["counts"].decode('utf-8')
        mask_format["segmentation"] = rle
        print(rle)
        ans_list.append(mask_format)
        now += 1

with open(save_json_path, 'w') as fout:
    json.dump(ans_list, fout)
