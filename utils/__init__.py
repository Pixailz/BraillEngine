import os
import cv2
import time
import atexit
import random

TMP_DIR="./tmp"
if not os.path.isdir(TMP_DIR):
	os.mkdir(TMP_DIR)

EXT_IMG = ".bim" # braille image
EXT_VID = ".bvi" # braille video

from utils.ansi				import ansi
from utils.braillEngine		import braille

import utils.signal

