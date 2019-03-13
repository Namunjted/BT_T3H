
data = ["newfile.txt","photoshop.psd","word.docx","server.js","index.html","test.py"]
result = []
for name in data:
	for character in name:
		if(character == "."):
			result.append(name[:name.index(character)])
print(result)

'''
['newfile', 'photoshop', 'word', 'server', 'index', 'test']
'''

