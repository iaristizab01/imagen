import os
import time
import streamlit as st
import base64
from openai import OpenAI
import openai
from PIL import Image
import numpy as np
from gtts import gTTS
from streamlit_drawable_canvas import st_canvas
import json
import paho.mqtt.client as paho

# ============================
# Fondo de la app
# ============================
def set_background(image_file: str):
    """Pone una imagen de fondo en toda la app de Streamlit."""
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ============================
# Config MQTT
# ============================
BROKER = "157.230.214.127"
PORT = 1883
MQTT_CLIENT_ID = "STREAMLIT_MYSTIC_PUB"

def mqtt_publish(topic: str, payload: dict, qos: int = 0, retain: bool = False):
    """Conecta al broker, publica el mensaje (JSON) y se desconecta."""
    try:
        client = paho.Client(MQTT_CLIENT_ID)
        client.on_publish = lambda c, u, r: pri_
