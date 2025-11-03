data :- text, image, audio, Video
textual :- .txt

file1 = open("first.txt","w")
file1.write("I am Sunny")
file1.close()


file2 = open("first.txt","r")
y = file2.read()
print(y)

file2.close()

