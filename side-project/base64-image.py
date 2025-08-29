import base64

# them chuc nang doc file .txt cho base64_string=

# Chuỗi Base64 của bạn
base64_string = ""

# Loại bỏ phần "data:image/png;base64,"
base64_string = base64_string.split(",")[1]

# Giải mã Base64 và lưu tệp
image_data = base64.b64decode(base64_string)
with open("image.png", "wb") as file:
    file.write(image_data)

print("Ảnh đã được lưu dưới tên image.png!")
