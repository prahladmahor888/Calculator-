import turtle as tu
import cv2
from svgpathtools import svg2paths2
from svg.path import parse_path
from tqdm import tqdm
class sketch_from_svg:

    def __init__(self,path,scale=30,x_offset=400,y_offset=400):
        
        self.path = path
        self.x_offset = x_offset
