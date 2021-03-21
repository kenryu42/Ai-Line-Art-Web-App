import os
import cv2
import dlib
import shutil
import base64
import tempfile
import numpy as np
from flask_cors import CORS
from imutils import face_utils
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

class HelloWorld(Resource):
    def post(self):
        temp_dirPath = ""
        some_json = request.get_json()
        if "image" in some_json and some_json["image"] != None and len(some_json["image"]) > 10000:
            data = some_json["image"]
            data = data.split(",")[-1]
            return data_to_image(data, temp_dirPath)
        else:
            return "Data not exist", 403

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def data_to_image(data_uri, temp_dirPath):
    # create temp_dirPath
    temp_dirPath = tempfile.mkdtemp(dir=".")
    _, temp_imgPath = tempfile.mkstemp(dir=temp_dirPath)
    # print(temp_imgPath)
    imgData = base64.b64decode(data_uri)
    with open(temp_imgPath, 'wb') as f:
        f.write(imgData)
    return detect_face(temp_imgPath, temp_dirPath)

def crop_boundary(top, bottom, left, right, faces):
    if faces:
        top = max(0, top - 200)
        left = max(0, left - 100)
        right += 100
        bottom += 100
    else:
        top = max(0, top - 50)
        left = max(0, left - 50)
        right += 50
        bottom += 50

    return (top, bottom, left, right)

def detect_face(imgpath, temp_dirPath):
    frame = cv2.imread(imgpath)
    # resize image if too large
    if frame.shape[0] > 1000:
        # print(f"resized image with height {frame.shape[0]}.")
        frame = image_resize(frame, height=1000)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detect = dlib.get_frontal_face_detector()
    rects = face_detect(gray, 1)
    ans = [-1, 0]
    faces = []
    
    # print("faces: ", len(rects))
    """
        Take the biggest face
    """
    for (i, rect) in enumerate(rects):
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        (x1, y1, x2, y2) = x, y, x + w, y + h
        faces.append((y1, y2, x1, x2))
        if (x2 - x1) > ans[1]:
            ans[0] = i
            ans[1] = x2 - x1
            
    # print(ans)
    if (len(rects)):
        (x, y, w, h) = face_utils.rect_to_bb(rects[ans[0]])
        (x1, y1, x2, y2) = x, y, x + w, y + h
        top, bottom, left, right = crop_boundary(y1, y2, x1, x2, len(rects) <= 2)
        for (i, rect) in enumerate(faces):
            if (i == ans[0]):
                continue
            t, b, l, r = rect
            # print(i, t, b, l, r)
            if (l < right < r or left < l < r < right) and t < bottom:
                right = l
            if (l < left < r or left < l < r < right) and t < bottom:
                left = r
            if (b < top < t or bottom < b < t < top) and l < right:
                top = b
            if (b < bottom < t or bottom < b < t < top) and l < right:
                bottom = t
        # crop the image and save
        crop_img = frame[top: bottom, left: right]
        cropped_imgPath = imgpath + ".png"
        cv2.imwrite(cropped_imgPath, cv2.cvtColor(crop_img, cv2.COLOR_RGB2BGR))
        
        # delete the full origin image
        baseName = os.path.basename(imgpath)
        os.remove(imgpath)
        return draw_portrait(baseName, cropped_imgPath, temp_dirPath)
        

    # clean up and return no face error    
    shutil.rmtree(temp_dirPath)
    return "No face detected", 400

def image_to_data(imgPath):
    prefix = f"data:image/png;base64,"
    with open(imgPath, "rb") as f:
            img = f.read()
    data = prefix + base64.b64encode(img).decode("utf-8")
    return data

def draw_portrait(basename, cropped_imgPath, temp_dirPath):
    exp = "pretrained"
    imgsize = 512
    dataroot = temp_dirPath
    epoch = "200"
    gpu_id = "-1"

    for vec in [[1,0,0]]:
        svec = '%d,%d,%d' % (vec[0],vec[1],vec[2])
        img1 = 'imagesstyle%d-%d-%d'%(vec[0],vec[1],vec[2])
        # print('results/%s/test_%s/index%s.html'%(exp,epoch,img1[6:]))
        os.system('python draw.py --dataroot %s --name %s --model test --output_nc 1 --no_dropout --model_suffix _A --num_test 1000 --epoch %s --imagefolder %s --sinput svec --svec %s --crop_size %d --load_size %d --gpu_ids %s' % (dataroot,exp,epoch,img1,svec,imgsize,imgsize,gpu_id))
    
    result_imgPath = "results/pretrained/test_200/imagesstyle1-0-0/" + basename + "_fake.png"
    # create data url for both cropped and fake image
    crop = image_to_data(cropped_imgPath)
    result = image_to_data(result_imgPath)
    # clean up temp dir and tempfile
    shutil.rmtree(temp_dirPath)
    os.remove(result_imgPath)
    # return json result
    return {"result": result, "crop": crop}, 200
    
api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
