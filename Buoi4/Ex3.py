Date_and_Time = (("31", "January"), ("29", "February"), ("31", "March"),
                 ("30", "April"), ("31", "May"), ("30", "June"),
                 ("31", "July"), ("31", "August"), ("30", "September"),
                 ("31", "October"), ("30", "November"), ("31", "December"))

month = int(input("nhap vao mot so nguyen: "))
while True:
    if(month > 0 and month < 12):
        break
    else:
        month = int(input("vui long nhap lai: "))
print(Date_and_Time[month - 1])

'''
nhap vao mot so nguyen: 20
vui long nhap lai: 10
('31', 'October')
'''
