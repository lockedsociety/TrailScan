import os

downloads_folder = os.path.expanduser("~" + os.sep + "Downloads")

for root, _, files in os.walk(downloads_folder):
    pass