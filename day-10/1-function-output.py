def function_1(f_name, l_name):
  format_f_name = f_name.title()
  format_l_name = l_name.title()
  return f"{format_f_name} {format_l_name}"

def function_2(full_name):
  return f"{"Hello " * 3}! {full_name}"  

output = function_2(function_1(f_name="truOnG", l_name="tAm"))
print(output)


# Explain
# full_name = function_1(f_name="luCIa", l_name="PaKER")
# greeting = function_2(full_name)
# print(greeting)