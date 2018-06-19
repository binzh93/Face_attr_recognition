# -*- coding: utf-8 -*-
import os

age_dict = {"0": 0, "3": 3, "6_15": 10, "16_25": 20, "26_35": 30, "36_45": 40, "46_60": 53, "60p": 65}

basepath = "/Users/bin/Desktop/人脸属性识别/"
age_path = "AgeAndGenderCopImgs/Age/AgeGenderTrainCopImgRandRGB64x64Normal/"
gender_path = "AgeAndGenderCopImgs/Gender/GenderTrainCopImgRandRGB64x64Normal/"
train_txt_path = "/Users/bin/Desktop/train.txt"
with open(train_txt_path, 'wb') as f:
    num1 = 1
    for root in os.listdir(os.path.join(basepath, age_path)):
        if root == '.DS_Store':
            continue
        else:
            for gender in os.listdir(os.path.join(basepath, age_path, root)):
                if gender == '.DS_Store':
                    continue
                else:
                    if gender == 'Male':
                        gender_label = 0
                    else:
                        gender_label = 1
                    for age in os.listdir(os.path.join(basepath, age_path, root, gender)):
                        if age == '.DS_Store':
                            continue
                        else:
                            for pic in os.listdir(os.path.join(basepath, age_path, root, gender, age)):
                                if pic == '.DS_Store':
                                    continue
                                else:
                                    pic_path = os.path.join(age_path, root, gender, age, pic)
                                    f.write(pic_path + " " + str(gender_label) + " " + str(age_dict[age]) + "\n")
                                    #print os.path.join(age_path, root, gender, age, pic), gender_label, age_dict[age]
                                    num1 += 1

    print num1

    num2 = 0
    for root in os.listdir(os.path.join(basepath, gender_path)):
        if (root == '.DS_Store') | (root == 'FaceLabel_rand.txt') | (root == 'FaceLabel.txt'):
            continue
        else:
            for gender in os.listdir(os.path.join(basepath, gender_path, root)):
                if gender == '.DS_Store':
                    continue
                if gender == 'Male':
                    gender_label = 0
                else:
                    gender_label = 1
                for pic in os.listdir(os.path.join(basepath, gender_path, root, gender)):
                    if pic == '.DS_Store':
                        continue
                    else:
                        pic_path = os.path.join(gender_path, root, gender, pic)
                        f.write(pic_path + " " + str(gender_label) + " " + "-1" + "\n")
                        #print os.path.join(gender_path, root, gender, pic), gender_label, -1
                        num2 += 1
    print num2

