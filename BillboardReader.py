import csv2dict
import database


class BillboardReader:
    def __init__(self, filename):
        self.collection = "BillboardLyrics"
        self.filename = filename
        self.data = None

    def run(self):
        self.data = csv2dict.csv2dict(self.filename)
        status = database.db_save(self.collection, self.data)
        if status:
            print("error")

    # def debug(self, collection_name):
    #     database.db_check(collection_name)



if __name__ == "__main__":
    b = BillboardReader("billboard_lyrics_1964-2015.csv")
    b.run()
