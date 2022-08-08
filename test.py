try:
    import os
    import json
    import glob
    import argparse
    import cv2
    import numpy as np
    from scipy import signal as sg
    from numpy import array
    from scipy.ndimage import maximum_filter
    import typing
    from PIL import Image, ImageDraw
    import pandas as pd
    import tables
    import matplotlib.pyplot as plt
except ImportError:
    print("Need to fix the installation")
    raise

a = 13
a = f"{a:05}"
print(a)

