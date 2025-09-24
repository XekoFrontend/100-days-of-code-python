import requests
import os
import json
import time
import random
from pathlib import Path

client_id = "3c38aa12-8458-4b15-bd2c-39b001dca0ed"
client_secret = "cJz8Q~sMTktI2lE1Qp4Y3oFRLRE1yH0KH_O3AbJw"
tenant_id = "8ffdd271-09c3-46c5-b82b-8ff463ac7a61"
user_email = "vc8bv@tsd06.onmicrosoft.com"

# Step 1 - Get token
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
scopes = ["https://graph.microsoft.com/.default"]
data = {
    "client_id": client_id,
    "scope": " ".join(scopes),
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}
print("🔐 Đang lấy access_token...")
resp = requests.post(token_url, data=data)
token = resp.json().get("access_token")
if not token:
    print("❌ Lỗi lấy token:", resp.text)
    exit()

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def safe_get(url, label):
    try:
        res = requests.get(url, headers=headers)
        print(f"{label} → Status:", res.status_code)
        return res
    except Exception as e:
        print(f"{label} → Lỗi:", e)

# Step 2 - Gửi mail tới nhiều người
recipients = [
    "AdeleV@tsd06.onmicrosoft.com", "alt.jl-0d5gewa@yopmail.com",
    "pocequegoisa-5899@yopmail.com", "nguyenlethuong1309@tsd06.onmicrosoft.com",
    
]

mail_payload = {
  "message": {
    "subject": "Mail khen thưởng nội bộ và ngoài hệ thống",
    "body": {
      "contentType": "Text",
      "content": (
        "Chào buổi sáng cả nhà,\n\n"
        "Hy vọng mọi người có một khởi đầu ngày mới thật nhiều năng lượng!\n\n"
        "Tôi muốn dành vài phút để gửi lời khen thưởng đặc biệt đến toàn thể đội ngũ về những nỗ lực và thành quả xuất sắc trong tháng vừa qua. "
        "Nhờ sự cống hiến không ngừng nghỉ và tinh thần làm việc nhóm tuyệt vời của các bạn, chúng ta đã đạt được những mục tiêu ấn tượng và vượt qua nhiều thử thách.\n\n"
        "Thật sự tự hào khi được làm việc cùng một tập thể tài năng và nhiệt huyết như các bạn. Hãy cùng nhau giữ vững phong độ này và tiếp tục gặt hái thêm nhiều thành công hơn nữa trong thời gian tới nhé!\n\n"
        "Chúc các bạn một ngày làm việc hiệu quả và tràn đầy niềm vui!\n\n"
        "Trân trọng,\n"
        "Ban Quản Lý"  # Thay vì tên cá nhân
      )
    },
    "toRecipients": [{"emailAddress": {"address": email}} for email in recipients],
    # Thêm phần này để ẩn/thay đổi tên người gửi
    "from": {
      "emailAddress": {
        "address": user_email,
        "name": "Hệ Thống Thông Báo"  # Tên hiển thị thay vì tên thật
      }
    }
  }
}

print("📬 Gửi mail nội bộ và ngoài hệ thống ...")
res = requests.post(
    f"https://graph.microsoft.com/v1.0/users/{user_email}/sendMail",
    headers=headers,
    json=mail_payload
)
print("📤 Trạng thái gửi mail:", res.status_code)

# Step 3 - Ping Graph API nhiều dịch vụ
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}", "👤 User info")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/drive", "📁 OneDrive")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/mailFolders", "📨 MailFolders")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/mailFolders/inbox/messages?$top=1", "📥 Inbox latest")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/joinedTeams", "💬 Teams")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/calendars", "📅 Calendar list")

# Step 4 - Xoá nội dung thư mục OneDrive và tạo file giả trực tiếp trên cloud
print("🧹 Xoá toàn bộ nội dung trong thư mục PingE5 (giữ nguyên thư mục)...")
# Thay đổi tên remote và đường dẫn theo config mới của bạn
os.system("rclone delete e5renew:PingE5 --leave-root")

print("📄 Tạo ngẫu nhiên 3-4 file giả trực tiếp trên OneDrive...")
for i in range(random.randint(3, 4)):
    filename = f"note_{random.randint(1000, 9999)}.txt"
    content = f"Đây là file giả số {i+1} để giữ OneDrive hoạt động."
    # Đường dẫn folder trong OneDrive
    upload_url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/root:/PingE5/{filename}:/content"
    res = requests.put(upload_url, headers=headers, data=content.encode("utf-8"))
    print(f"📎 Upload {filename} → Status:", res.status_code)

# Step 5 - Upload ảnh từ thư mục local lên OneDrive
print("🖼️ Upload ảnh từ local lên OneDrive...")
# local_folder = r"C:\Users\haola\Downloads\PingE5"
# remote_folder = "PingE5Images"

# ĐÚNG: Dùng f-string
os.system(r'rclone copy "C:\Users\haola\Downloads\PingE5" e5renew:PingE5Images --transfers=4 --checkers=8 --fast-list')