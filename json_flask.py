'''
Following code sends and recieves an image file using JSon in Flask
Input ex. - earth.png, example_02.mp4
Output ex. - new_image.png, new_video.mp4
'''


from flask import Flask, request,jsonify
import base64
import json 


app = Flask(__name__)

@app.route('/', methods = ['GET', "POST"] )
def index():
    #opens image file, converts into bytes using b64encode() and then converts into string using decode function
    with open("example_02.mp4", "rb") as image_file:
        result = base64.b64encode(image_file.read()).decode('utf-8')
    #jsonify the image string
    result = jsonify(result)
    #extracts string from the JSON oject and converts it into bytes using encode()
    json_string = json.loads(result.get_data()).encode('utf-8')
    #creates a png file and converts it into image files using decodebytes()
    with open("new_video.mp4", "wb") as fh:
        fh.write(base64.decodebytes(json_string))       
    return result
  
    

    
if __name__ == '__main__':
    app.run(debug=True)