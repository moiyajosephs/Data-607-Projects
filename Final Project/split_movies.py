
f = open('C:/Users/josep/Downloads/combined_data_1.txt/combined_data_1.txt', "r") 
os.chdir('C:/Users/josep/OneDrive/Documents/Data-607-Projects/Final Project/movie data')
lines = [line for line in f.readlines()]
i = 1
o = open("{}.txt".format(i), "w")
for line in lines:
    if (line.find(":") != -1):
        o.close()
        print("close")
        i = i + 1
        o = open("{}.txt".format(i), "w")
    else:
        o.write(line)
        print("writed!")