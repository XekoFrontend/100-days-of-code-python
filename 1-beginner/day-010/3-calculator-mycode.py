import art

print(art.logo)

temp_result = []
def calculator(n1, operation, n2):
  """ Thực hiện các phép toán và ghi kết quả vào list tạm """
  if operation == "+":
    result = n1 + n2 
  if operation == "-":
    result = n1 - n2
  if operation == "*":
    result = n1 * n2
  if operation == "/":
    result = n1 / n2
  
  # Hiển thị kết quả linh hoạt theo 'int' hoặc 'float'
  if result % 1 == 0:
    result = int(result)
  # Ghi kết quả vào temp_result  
  temp_result.append(result)
  return result


n1 = float(input("Enter the first number: "))
continue_math = True
while continue_math:
  operation = input("Enter the operation (+, -, *, /): ")
  while operation != "+" and  operation != "-" and operation != "*" and operation != "/":
    operation = input("Enter the operation (+, -, *, /): ")
  n2 = float(input("Enter the next number: "))
  continue_cal = input("Do you want to continue or exit (yes/no): ").lower()
  while continue_cal != "yes" and continue_cal != "no":
    continue_cal = input("Do you want to continue or exit (yes/no): ").lower()
  
  # Gọi hàm tính toán 'calculator' và hiển thị kết quả
  output_cal = calculator(n1, operation, n2)
  print(output_cal)
  # Thoát chương trình
  if continue_cal == "no":
    continue_math = False
  # Tiếp tục chương trình
  elif continue_cal == "yes":
    for num_result in temp_result:
      index_result = temp_result.index(num_result)
    # Lấy kết quả sau cùng trong list tạm để dùng làn input cho 'n1'
    n1 = temp_result[index_result]



# TODO: Hiện thông báo nếu nhập sai: phép tính, yes, no ... (dùng try-except: chưa học tới)