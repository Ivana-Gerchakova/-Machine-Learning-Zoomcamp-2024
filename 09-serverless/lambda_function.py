import tensorflow as tf
import numpy as np
from io import BytesIO
from urllib import request
from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def normalize_image(image):
    return image / 255.0

def predict(image_url, model_path="model_2024_hairstyle.tflite"):
    """Функција за директно предвидување од слика"""
    try:
        image = download_image(image_url)
        
        target_size = (200, 200)
        prepared_image = prepare_image(image, target_size)
        image_array = np.array(prepared_image, dtype=np.float32)
        normalized_image = normalize_image(image_array)
        batched_image = np.expand_dims(normalized_image, axis=0)
        
        interpreter = tf.lite.Interpreter(model_path=model_path)
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        
        interpreter.set_tensor(input_details[0]['index'], batched_image)
        interpreter.invoke()
        output = interpreter.get_tensor(output_details[0]['index'])[0]
        
        return float(output)
    except Exception as e:
        raise RuntimeError(f"Error during prediction: {e}")

def lambda_handler(event, context):
    try:
        image_url = event.get('url')
        if not image_url:
            return {
                "statusCode": 400,
                "body": "Missing 'url' in the request."
            }

        prediction = predict(image_url)
        return {
            "statusCode": 200,
            "body": {"prediction": prediction}
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error processing the request: {e}"
        }
    
    
    
    