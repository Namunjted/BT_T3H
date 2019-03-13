data = ["newfile.txt","photoshop.psd","word.docx","server.js","index.html","test.py","abc.psd.txt","code.psd.txt.docx"]
result = []
for name in data:
    for character in name:
        if character == ".":
            result.append(name[:name.index(character)])
            break
print(result)

'''
['newfile', 'photoshop', 'word', 'server', 'index', 'test', 'abc', 'code']
'''

