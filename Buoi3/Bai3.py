data = ["newfile.txt","photoshop.psd","word.docx","server.js","index.html","test.py","abc.psd.txt","code.psd.txt.docx"]
result = []
for name in data:
    name = name.rsplit('.',1)
    name.pop()
    result += name
print(result)


'''
['newfile', 'photoshop', 'word', 'server', 'index', 'test', 'abc.psd', 'code.psd.txt']
'''

