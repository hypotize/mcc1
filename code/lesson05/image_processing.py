# Miura Computer Club 
# Lesson 05 
# Author Yoshio Hashimoto 
# First version: 2022/04/29 
#
# Copyright 2022 Yoshio Hashimoto 
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob
import os
from PIL import Image, ImageOps
import numpy as np
import cv2

def grayscale(img, filename, dirpath):
    os.makedirs(dirpath, exist_ok=True)
    img.convert('L').save(dirpath + filename)

def grayscale_binarize(img, filename, dirpath):
    os.makedirs(dirpath, exist_ok=True)
    np_img = np.array(img.convert('L')) #PILからnumpy配列へ変換
    np_img = (np_img > 128) * 255 #128より大きければ255、そうでなければ0、にする
    img = Image.fromarray(np_img.astype(np.uint8)) #numpy配列からPILへ変換
    img.save(dirpath + filename)

def posterize(img, filename, dirpath):
    os.makedirs(dirpath, exist_ok=True)
    ImageOps.posterize(img.convert('RGB'), 2).save(dirpath + filename)

def nega_posi_reverse(img, filename, dirpath):
    os.makedirs(dirpath, exist_ok=True)
    ImageOps.invert(img.convert('RGB')).save(dirpath + filename)

def sepia(img, filename, dirpath):
    os.makedirs(dirpath, exist_ok=True)
    img = img.convert('L')
    r = img.point(lambda x: x * 240 / 255)
    g = img.point(lambda x: x * 200 / 255)
    b = img.point(lambda x: x * 145 / 255)
    Image.merge('RGB', (r, g, b)).save(dirpath + filename)

def canny(cv2_gray_img, filename, dirpath):
    os.makedirs(dirpath, exist_ok=True)

    # エッジ(輪郭)であるかの判断のレベル
    # threshold2を小さくすると、エッジとして検出されやすくなる
    # threshold2を小さくすると、threshold2により検出されたエッジの隣接部分が、エッジになりやすくなる
    # https://qiita.com/Takarasawa_/items/1556bf8e0513dca34a19
    threshold1 = 250
    threshold2 = 250

    cv2_canny_img = cv2.Canny(cv2_gray_img, threshold1, threshold2)
    cv2.imwrite(dirpath + filename, cv2_canny_img)


#main
for filepath in glob.glob('./画像/*'):
    filename = os.path.basename(filepath)
    img = Image.open(filepath)
    cv2_gray_img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

    grayscale(img, filename, './グレイスケール/')
    grayscale_binarize(img, filename, './白黒/')
    posterize(img, filename, './ポスタライズ/')
    nega_posi_reverse(img, filename, './ネガポジ反転/')
    sepia(img, filename, './セピア/')
    canny(cv2_gray_img, filename, './輪郭/')
