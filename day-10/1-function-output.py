def function_1(f_name, l_name):
  # Show notification if user don't type anything.
  if f_name == "" and l_name == "":
    return "You need to type a name."
  
  format_f_name = f_name.title()
  format_l_name = l_name.title()
  return f"{format_f_name} {format_l_name}"

def function_2(full_name):
  return f"{"Hello " * 3}! {full_name}."  

f_name = input("First name: ")
l_name = input("Last name: ")
# Dùng kết quả của function_1 làm tham số cho function_2.
output = function_2(function_1(f_name, l_name))
print(output)




# Explain
# full_name = function_1(f_name="luCIa", l_name="PaKER")
# greeting = function_2(full_name)
# print(greeting)