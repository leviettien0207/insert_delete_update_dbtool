from .constant import *
from .models import diamond


class Item:
    def __init__(self, data_row):
        self.data_errors = []
        self.id = data_row[1]
        self.carat = data_row[2]
        self.cut = data_row[3]
        self.color = data_row[4]
        self.clarity = data_row[5]
        self.depth = data_row[6]
        self.table = data_row[7]
        self.price = data_row[8]
        self.x = data_row[9]
        self.y = data_row[10]
        self.z = data_row[11]

    def validate_cut(self):
        if self.cut is not None and self.cut.upper() not in CUT_RANGE:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[3]))

    def validate_color(self):
        if self.color is not None and self.color.upper() not in COLOR_RANGE:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[4]))

    def validate_clarity(self):
        if self.clarity is not None and self.clarity.upper() not in CLARITY_RANGE:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[5]))

    def validate_float(self):
        try:
            self.carat = float(self.carat)
        except:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[2]))
        try:
            self.depth = float(self.depth)
        except:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[6]))
        try:
            self.table = float(self.table)
        except:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[7]))
        try:
            self.price = float(self.price)
        except:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[8]))
        try:
            self.x = float(self.x)
        except:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[9]))
        try:
            self.y = float(self.y)
        except:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[10]))
        try:
            self.z = float(self.z)
        except:
            self.data_errors.append(MSG_MISSING_INFO.format(EXCEL_COLUMNS[11]))

    def validate_all(self):
        self.data_errors.clear()
        self.validate_cut()
        self.validate_color()
        self.validate_clarity()

    def validate_primary_key(self):
        return True if self.id is not None else False

    def convertDiamond(self):
        return diamond(id=self.id, carat=self.carat, cut=self.cut, clarity=self.clarity,
                       color=self.color, depth=self.depth, table=self.table, price=self.price,
                       x=self.x, y=self.y, z=self.z)

    def __getitem__(self, item):
        # this is reason why some methods in real code project look like this?
        pass
