try:
    file1 = open('sample.txt','r')
    reading = file1.read()
    print("Reading File Contents:\n",reading)
except FileNotFoundError:
    print("File Not Found")
