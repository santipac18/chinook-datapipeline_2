# Databricks notebook source
import pandas as pd
import configparser
import os
from datetime import datetime

# Get the parent path of the notebook
notebook_path = dbutils.entry_point.getDbutils().notebook().getContext().notebookPath().get()
parent_path = os.path.dirname('/Workspace' + notebook_path)
os.chdir(parent_path)

# read config file
config = configparser.ConfigParser()
config.read('./pipeline.conf')
inputPath = config.get('DEFAULT', 'INPUT_PATH')
outputPath = config.get('DEFAULT', 'OUTPUT_PATH')
testResultPath = config.get('DEFAULT', 'TEST_RESULT_PATH')

# read files
tracksInput = pd.read_csv(inputPath)
tracksOutput = pd.read_csv(outputPath)

# open test result file
f = open(testResultPath, "a")

# write datetime
f.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S") + '\n')

# Case 1
unitPriceType = tracksOutput.dtypes['UnitPrice']
if unitPriceType == 'int64':
    f.write("Case 1: Pass\n")
else:
    f.write("Case 1: Fail\n")

Case 2
def expected_unit_price(input_price):
    return math.ceil(input_price) * 33.77

# ตรวจสอบว่าค่า UnitPrice_output ตรงกับที่คาดหวังหรือไม่
if (mergedTracks['UnitPrice_output'] == mergedTracks['UnitPrice_input'].apply(lambda x: expected_unit_price(x))).all():
    f.write("Case 2: Pass\n")
else:
    f.write("Case 2: Fail\n")

# close test result file
f.close()


# 


