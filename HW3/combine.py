import json

with open("answer.json", 'r') as fd1:
    result1 = json.load(fd1)

with open("answer_id4.json", 'r') as fd2:
    result2 = json.load(fd2)

answer = []
for i in range(6):
    now_id = i + 1
    now_bbox = []
    now_json = []
    print(i)

    if now_id == 4:
        for item in result2:
            if item["image_id"] == now_id:
                answer.append(item)
    else:
        for item in result1:
            if item["image_id"] == now_id:
                answer.append(item)

with open("answer.json", 'w') as fd:
    json.dump(answer, fd)
