from io import BytesIO
from deepface import DeepFace
import numpy as np
from PIL import Image

model = None


def analyze(img_path, actions, detector_backend, enforce_detection, align):
    result = {}
    demographies = DeepFace.analyze(
        img_path=img_path,
        actions=actions,
        detector_backend=detector_backend,
        enforce_detection=enforce_detection,
        align=align,
    )
    result["results"] = demographies
    return result

def predict(image: Image.Image): # 
    # image = np.asarray(image.resize((224, 224)))[..., :3]
    # image = np.expand_dims(image, 0)
    # image = image / 127.5 - 1.0
    image = np.asarray(image)

    demographies = analyze(
        img_path= image,
        actions= ["age", "gender", "emotion", "race"],
        detector_backend="opencv",
        enforce_detection=True,
        align=True,
    )
    return demographies


def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
