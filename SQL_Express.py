import pyodbc
from datetime import datetime

class Sql:
    def __init__(self, database, server="LAZY-BOOK"):

        username = 'sa'
        password = 'ТуЦеЩт4994'
        self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                    "username="+username+";"
                                    "password="+password+";"
                                    "Trusted_Connection=yes;")
        self.query = "-- {}\n\n-- Made in Python".format(datetime.now()
                                                         .strftime("%d/%m/%Y"))


def get_diskount_level_from_SQL(CardType, CardNumber):

    sql_obj = Sql('Semya_Discount')
    query = "SELECT MAX(CardsLevels.[DiscountLevel]) as MaxCardLevel " \
            "FROM [dbo].[Levels] as CardsLevels " \
            "WHERE CardsLevels.[Cardnumber] = " + CardNumber + " " \
            "GROUP BY CardsLevels.[Cardnumber]"

    # query = "SELECT (CardsLevels.[DiscountLevel]) as MaxCardLevel " \
    #         "FROM [dbo].[Levels] as CardsLevels " \
    #         "WHERE CardsLevels.[Cardnumber] = " + CardNumber + " " \

    crsr = sql_obj.cnxn.execute(query)
    Result_list = list(crsr)

    Result_tuple = Result_list[0]

    return (Result_tuple[0])

# diskount_level = get_diskount_level_from_SQL('999664779')
# print(diskount_level)
