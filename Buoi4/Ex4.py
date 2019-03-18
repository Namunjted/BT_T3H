import string
lines = '''
Ngư60ời 'theo hư@ơng' hoa 100mây mù [giăng lối]
Làn 25 sương khó30i phôi phai 90 đưa bư$ớc ai xa rồi 35
100Đơn c#ôi m99ình ta {vấn vương} hồi ức tro^ng ... men say (chiều mưa) buồ80n
Ng~ăn "giọt lệ" ngừng k2hiến khoé mi sầu bi.1
'''
lines = lines.splitlines()
result = []
for line in lines:
    for word in line:
        if word not in string.punctuation and word not in string.digits:
            result.append(word)
    result.append("\n")
for data in result:
    print(data, end="")
