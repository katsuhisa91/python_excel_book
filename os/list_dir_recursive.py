import glob

files = glob.glob('../**', recursive=True)
print(files)
