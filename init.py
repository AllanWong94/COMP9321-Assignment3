import os
import csv2dict
import database
import re
import rundb
# run the database
# rundb.run()

def init():
    # store the billboard_lyrics dataset into database
    filename = "billboard_lyrics_1964-2015.csv"
    collection_name = re.sub("\.csv", "", filename)
    collection_name = re.sub("[^a-zA-Z]", "", collection_name)
    data = csv2dict.csv2dict(filename)
    status = database.db_save(collection_name, data)
    if status:
        print("error")
    # status = 1 represents error in db_saving.
    database.db_check(collection_name)


if __name__ == "__main__":
    # rundb.run()
    # Can't rundb in init, need to run it before init.py
    init()
