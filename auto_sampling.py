import ffmpeg
import os
from os import path
from pathlib import Path
import shutil
import glob
import numpy as np
import cv2

#convert video to frames
try:
    (ffmpeg.input('BLP.mp4')
          .filter('fps', fps=45)
          .output('Babylove\%d.png',
                  start_number=1)
          .run(capture_stdout=True, capture_stderr=True))
except ffmpeg.Error as e:
    print('stdout:', e.stdout.decode('utf8'))
    print('stderr:', e.stderr.decode('utf8'))

#Sample 30 frames into a different folder. Create folders prior to running the code
images = os.listdir('Babylove/')
for image_name in images:
    for i in range(10):
        if int(image_name[0:-4]) % 10 == i:
            output = 'BLP/batch%s'%(i,)
            shutil.copy('Babylove' + "/" + image_name, output)


for i in range(10):
    img_array = []
    for filename in glob.glob('BLP/batch%s/*.png'%(i,)):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
     
    out = cv2.VideoWriter('BLP/batch%s.mp4'%(i,),cv2.VideoWriter_fourcc(*'mp4v'), 1, size)
     
    for j in range(len(img_array)):
        out.write(img_array[j])
    out.release()


            

