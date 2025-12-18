import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

import logging
from flask import Flask, request, jsonify, redirect, url_for, render_template_string
import torch
import numpy as np
import faiss
from transformers import CLIPProcessor, CLIPModel
import cv2
from datetime import datetime
import redis
import threading
from datetime import datetime, timedelta