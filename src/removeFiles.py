filelist = [f for f in os.listdir()]
for f in filelist:
    print(f)
    os.remove(f)
