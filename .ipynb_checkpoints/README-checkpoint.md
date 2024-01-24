## How to run?

1. Setup
```bash
# Instal requirements
pip install -r requirements.txt

# Run the server
uvicorn application.server.main:app
```

2. Go to the end point
[http://127.0.0.1:8000](http://127.0.0.1:8000/docs#/default/predict_api_predict_image_post) 

3. Locate and click "try it out" button

4. "Browse" button will appear and use that to upload an image from local directory or use supplied images i.e., img1.jpg and img2.jpg

5. Click execute

6. Example of server response for img1.jpg

```json
{
  "results": [
    {
      "age": 25,
      "region": {
        "x": 334,
        "y": 171,
        "w": 507,
        "h": 507
      },
      "face_confidence": 9.922150114667602,
      "gender": {
        "Woman": 0.014402360829990357,
        "Man": 99.98559951782227
      },
      "dominant_gender": "Man",
      "emotion": {
        "angry": 0.0023715212591923773,
        "disgust": 4.385299293293253e-12,
        "fear": 0.00009383556403008697,
        "happy": 0.0003069455033255508,
        "sad": 0.03943679912481457,
        "surprise": 0.000010802163075140925,
        "neutral": 99.95778203010559
      },
      "dominant_emotion": "neutral",
      "race": {
        "asian": 51.62799954414368,
        "indian": 7.981083542108536,
        "black": 2.2472819313406944,
        "white": 12.244433164596558,
        "middle eastern": 5.233797058463097,
        "latino hispanic": 20.665405690670013
      },
      "dominant_race": "asian"
    }
  ]
}
