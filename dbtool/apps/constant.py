from pathlib import Path
import os

CUT_RANGE = ["IDEAL", "PREMIUM", "VERY GOOD", "GOOD", "FAIR"]
COLOR_RANGE = ["D", "E", "F", "G", "H", "I", "J"]
CLARITY_RANGE = ["FL", "SI1", "SI2", "VS1", "VS2", "VVS1", "VVS2", "I1"]
DB_COMMAND_RANGE = ['INSERT', 'UPDATE', 'DELETE']
EXCEL_COLUMNS = ['db_command', 'index', 'carat', 'cut', 'color', 'clarity',
                 'depth', 'table', 'price', 'x', 'y', 'z', 'status']

SUCCESS_200 = "success"
FAIL_OVERALL = {"STATUS": "FALSE",
                "ERRORS": "{}"}
FAIL_OPEN_EXCEL = "Can't find such that file with address {}"
FAIL_OPEN_SHEET = "Can't find such that sheet with name {}"
FAIL_RECORD = "Can't find such that record with id {}"

EXIST_ID = "Already there is an id {}"

PATH_FILE = os.path.join(Path(__file__).resolve().parent.parent, 'test.xlsx')
DIAMOND_COLUMNS = 13

MSG_MISSING_INFO = 'missing {}'
MSG_WRONG_COMMAND = '{} is not a command'
