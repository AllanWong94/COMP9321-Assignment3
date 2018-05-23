import requests
import re
from collections import Counter
from database import *
import bson
from time import time


# TODO delete the timer after optimizing
# TODO Cannot update information.
class FrequencyGetter:
    def __init__(self, data):
        self.year_freq = []
        self.collection = "WordFrequency"
        self.__word_frequency(data)

    def get_top_words(self, year, topn):
        # get the topn words of year, return all words if topn == 0
        query = "Year == " + year
        record = db_query(self.collection, query)
        freq_counter = record[year]
        return_list = freq_counter.most_common(topn)
        return return_list

    def __word_frequency(self, data):
        year = data[0]["Year"]
        # The data should be sorted in order of rank and year.
        lyrics_list = []

        # data = sorted(data, key=lambda k: k.get("Year", 0))
        t = time() # TODO
        for d in data:
            lyrics = d["Lyrics"]
            if lyrics != "NA":
                if year == d["Year"]:
                    lyrics_list.append(lyrics)
                else:
                    print("Finished processing Frequency data of Year: ", year, end = "\t")  # TODO
                    print("In: {:f}seconds".format(time() - t))    # TODO
                    self.__packaging(year, lyrics_list)
                    year = d["Year"]
                    lyrics_list = [lyrics]
                    t = time()
        self.__word_frequency_save()

    def __keyword_filter(self, lyrics):
        url = "http://d2dcrc.cse.unsw.edu.au:9091/ExtractionAPI-0.0.1-SNAPSHOT/rest/keyword"
        payload = {'sentence': lyrics}
        t = time()  # TODO
        response = requests.post(url, data=payload)
        print("api time: ", time() - t)  # TODO
        r = str(response.content, encoding="UTF-8")
        # the response use null instead of None, need to convert null to None in python.
        t = time()  #TODO
        r = re.sub(r'([^a-zA-Z])null([^a-zA-Z])', r'\1None\2', r)
        print("regex time: ", time() - t)  # TODO
        r = eval(r)
        t = time()
        keyword_list = r["keyword"].split(",")
        print("spliting time: ", time() - t)  # TODO
        return keyword_list

    def __packaging(self, year, lyrics_list):
        str_lyrics_list = " ".join(lyrics_list)
        w_list = self.__keyword_filter(str_lyrics_list)

        w_fq_dict = Counter(w_list)
        item = {year: w_fq_dict}
        self.year_freq.append(item)
        # self.__word_frequency_save(year, w_fq_dict)

    def __word_frequency_save(self):
        # freq_dict is a Counter type.
        status = db_save(self.collection, self.year_freq)
        if status:
            print("error in saving word frequency data.")
        else:
            print("successfully saved word frequency data.")


