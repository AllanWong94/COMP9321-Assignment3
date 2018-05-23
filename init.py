from BillboardReader import BillboardReader
from WordFrequency import FrequencyGetter


br = BillboardReader("billboard_lyrics_1964-2015.csv")
br.run()
fg = FrequencyGetter(br.data)
