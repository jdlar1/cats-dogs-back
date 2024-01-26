from pathlib import Path
from io import BytesIO
from typing import cast

from keras import Model
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

def predict(file: bytes) -> float:
    model = cast(Model, load_model(Path(__file__).parent / "final_model.h5"))
    
    image = load_img(BytesIO(file), target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    
    image = image.astype('float32')
    image = image - [123.68, 116.779, 103.939]
    
    prediction = model.predict(image)
    
    return prediction[0][0]