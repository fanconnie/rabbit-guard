# Advanced Rabbit Deterrence System

## Project Overview

fanconnie presents a sophisticated rabbit deterrence system using computer vision on a Raspberry Pi and Roboflow to detect and deter rabbits from your garden. Whenever a Rabbit is detected, the system triggers a noise like a baby crying or a car honking from a Bluetooth speaker, intended to scare the rabbit away.

## Special Features of the System

This system provides unique features including:

- Model training using Roboflow Train (based on YOLOv5, cutting-edge object detection model)
- Portable operation with the MakerHawk External Power Supply
- Active learning via the Roboflow Upload API
- Remote view of detections through a Flask Web Server
- Bluetooth Speaker Integration for rabbit deterrence

## Materials/Software Used

**Hardware:**

- Raspberry Pi
- [External Power Supply](https://www.amazon.com/MakerHawk-Raspberry-Uninterruptible-Management-Expansion/dp/B082CVWH3R/ref=sr_1_6?crid=3LJGHA055O4VL&dchild=1&keywords=battery+for+raspberry+pi&qid=1623698007&sprefix=battery+for+raspbe%2Caps%2C184&sr=8-6)
- [Camera for the Pi](https://www.amazon.com/Arducam-Megapixels-Sensor-OV5647-Raspberry/dp/B012V1HEP4/ref=sr_1_6?dchild=1&keywords=Raspberry+Pi+camera&qid=1624689746&sr=8-6)
- [Bluetooth Speaker](https://www.amazon.com/AUDIOVOX-SP881BL-Portable-Bluetooth-Rechargeable/dp/B07F8N6KJ9/ref=sr_1_4?crid=2363N4JZD3B18&dchild=1&keywords=canz+bluetooth+speaker&qid=1626056945&sprefix=CANZ+bluetoot%2Caps%2C173&sr=8-4)

**Software:**

- [Public Dataset](https://public.roboflow.com/object-detection/eastern-cottontail-rabbits)
- [Roboflow Annotate](https://docs.roboflow.com/annotate)
- [Roboflow Train](https://docs.roboflow.com/train)
- [Roboflow Inference API](https://docs.roboflow.com/inference)

## Further Information

- Blog: [https://blog.ro