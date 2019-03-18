### BT1: cho 1 biến data kiểu string như bên dưới

```
data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''
# https://www.poetrysoup.com/poem/cross_my_heart_609765
```

- Yêu cầu: giải mã mật thư, lấy tất cả các chữ cái đầu của từng dòng rồi ghép lại để được 1 câu cụ thể.

### BT2:

- Sử dụng vòng lặp in ra các số từ 1 đến 100, nếu số đó chia hết cho 3 thì thay bằng Buzz, chia hết cho 5 thì thay bằng Fizz, nếu chia hết cho cả 3 và 5 thì thay bằng FizzBuzz. Đồng thời, lưu giữ kết quả đạt được vào 1 list

### BT3

- Viết chương trình loại bỏ phần mở rộng của 1 tên file bất kì
VD: newfile.txt -> newfile, photoshop.psd -> photoshop, word.docx -> word, ....

### BT4

- Có bao nhiêu bộ ba A, B, C thỏa mãn điều kiện sau:
    - A, B, C đều là số nguyên dương
    - A + B / C = 10
    
- Lưu các giá trị tìm đc vào 1 list lớn chứa các list con: vd: [[9, 1, 1], ....]

### BT5

- Luyện tập dùng list comprehension với các câu hỏi sau:
    - Tạo 1 list chứa N số 2
    - Tạo 1 list chứa các số nguyên dương dưới 100, chia hết cho 3 hoặc 5
    - Tạo ra 1 list có dạng như sau: ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN], với N = 20
    - Tạo 1 list chứa N số nguyên ngẫu nhiên, gợi ý sử dụng thư viện random: `import random`
    
### BT6

- Tính tổng tất cả các số trong kết quả của phép tính `2**10000`

### BT7

- Viết chương trình tính tổng và tích tất cả các số trong 1 list: dùng vòng lặp, ko dùng hàm có sẵn (sum)

### BT8

- Viết chương trình tìm số lớn nhất và nhỏ nhất trong 1 list chứa cả kiểu int và float, ko dùng hàm có sẵn (max, min)

### BT9

- Viết chương trình để flatten list sau: [[1, 2, 3], [4, 5], [6, [7, 8], 9], [10]]
- Kết quả cần đạt được: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

### BT10

- Nếu lần lượt cho các giá trị trong bảng chữ cái tiếng Anh như sau: a = 1, b = 2, c = 3, .... thì tổng giá trị của các từ khi quy đổi ra số là như sau:

```
abc = 1 + 2 + 3 = 6
defgh = 4 + 5 + 6 + 7 + 8 = 30 
....
```

- Hỏi các từ sau có giá trị là bao nhiêu: python, patience, documents, students, homework, practice, success, english, university, congratulation