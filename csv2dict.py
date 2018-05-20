import csv


def csv2dict(filename):
    data_collection = []
    # encoding is set to latin-1 according to the encoding of BillboardLyrics dataset
    with open(filename, encoding='latin-1') as f:
        reader = csv.reader(f)
        fieldnames = next(reader)

        print("The keys to access song info is: ", end="\t")
        for i in fieldnames:
            print(i, end="\t")
        print()

        reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in reader:
            info_dict = {}
            for key in fieldnames:
                info_dict[key] = row[key]
            data_collection.append(info_dict)
    return data_collection


if __name__ == "__main__":
    for i in csv2dict("billboard_lyrics_1964-2015.csv"):
        print(i)
