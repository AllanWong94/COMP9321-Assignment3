# import re
# a = "billboard_lyrics_1964-2015.csv"
# collection_name = re.sub("\.csv", "", a)
# collection_name = re.sub("[^a-zA-Z]", "", collection_name)
# print(collection_name)

import subprocess
import os
path = "~/MongoDB/"
command = "mongod --dbpath "
command = os.path.join(command, path)
subprocess.call(command, shell=True)
