#Bài 1

# Not_Prime_Numbers = []
# Prime_Numbers = []
# def is_prime(n, i=2): 
#    if n <= 2: 
#      return n == 2 
#    if n % i == 0: 
#      return False 
#    if i * i > n: 
#     return True 
#    return is_prime(n, i + 1) # Test the function 
# num = 1
# a = int(input("Type a number: "))
# for e in range(num, a + 1):
#  if is_prime(num) or num == 1: 
#     Prime_Numbers.append(num)
#  else: 
#     Not_Prime_Numbers.append(num)
#  num = num + 1

# print (Prime_Numbers," are prime numbers and ",Not_Prime_Numbers," are not prime numbers")

#Bài 2

# g = str(input("Vùng Ơi Mở Ra: "))
# while not g == "python":
#    if g == "python":
#        print("Xin chào")
#    else:
#        g = str(input("Vùng Oưi Mở Ra: "))

#Bài 3 [CHƯA XONG]

# e = str(input("Câu 1: Python được phát hành vào năm nào? A: 1991 B: 1989 C: 2000 D: 1995: "))
# score = 0
# ans = ["A","a"]
# if e == ans[0] or e == ans[1]:
#     print("Đúng")
#     score = score + 1
# else:
#     print("Sai")

# e = str(input("Câu 2: Ai tạo ra Python? A: Guido can Rossum B: Dennis Ritchie C: James Gosling D: Bjarne Stroustrup:  "))
# ans = ["A","a"]
# if e == ans[0] or e == ans[1]:
#     print("Đúng")
#     score = score + 1
# else:
#     print("Sai")

# e = str(input("Câu 3: Câu lệnh nào dùng để hiển thị dữ liệu ra màn hình trong Python? A: print() B:  C: James Gosling D: Bjarne Stroustrup:  "))
# ans = ["A","a"]
# if e == ans[0] or e == ans[1]:
#     print("Đúng")
#     score = score + 1
# else:
#     print("Sai")