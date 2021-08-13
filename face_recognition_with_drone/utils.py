import pandas as pd
import numpy as np 
import os


def importDataInfo(path):
	columns = ["center","left_right","forward_backward","up_down","yaw"]
	data = pd.read_excel(os.path.join(path, "driving_log"), names = columns)
	print(data.head())