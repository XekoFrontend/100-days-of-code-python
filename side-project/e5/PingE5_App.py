import requests
import os
import json
import time
import random
from pathlib import Path

#============================================================================
client_id = "3c38aa12-8458-4b15-bd2c-39b001dca0ed"
client_secret = "cJz8Q~sMTktI2lE1Qp4Y3oFRLRE1yH0KH_O3AbJw"
tenant_id = "8ffdd271-09c3-46c5-b82b-8ff463ac7a61"
user_email = "Piano@tsd06.onmicrosoft.com"
#============================================================================

#============================================================================
# CHỌN CHẾ ĐỘ GỬI MAIL, bật tắt bằng cách comment/uncomment
# SEND_MODE = "manual"  # danh sách tự chọn
# SEND_MODE = "organization"  # gửi toàn bộ tổ chức
#============================================================================

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

status_messages = {
    200: "OK - Đã xử lý xong",
    201: "Created - Đã xử lý xong và tạo mới",
    202: "Accepted - Đã nhận, đang xử lý",
    400: "Bad Request - Yêu cầu không hợp lệ",
    401: "Unauthorized - Không có quyền truy cập",
    500: "Server Error - Lỗi máy chủ"
}

def safe_get(url, label):
    try:
        res = requests.get(url, headers=headers)
        print(f"{label} → Status:", res.status_code, res.status_code in status_messages and status_messages[res.status_code] or "")
        return res
    except Exception as e:
        print(f"{label} → Lỗi:", e)

# Step 2 - Gửi mail tới nhiều người
## > Danh sách email thủ công nếu chọn SEND_MODE là "manual"
manual_recipients = [
    "AdeleV@tsd06.onmicrosoft.com", 
    "alt.jl-0d5gewa@yopmail.com",
    "pocequegoisa-5899@yopmail.com", 
    "nguyenlethuong1309@tsd06.onmicrosoft.com",
]

## > Lấy danh sách email toàn tổ chức nếu chọn SEND_MODE là "organization"
if SEND_MODE == "organization":
    print("🔎 Đang lấy danh sách toàn bộ email trong tổ chức ...")
    users_url = "https://graph.microsoft.com/v1.0/users?$select=userPrincipalName"  # SỬA: dùng userPrincipalName thay vì mail
    all_emails = []
    while users_url:
        res = requests.get(users_url, headers=headers)
        data = res.json()
        # SỬA: Lọc email hợp lệ và loại bỏ guest accounts
        for user in data.get("value", []):
            email = user.get("userPrincipalName", "")
            if email and "@" in email and not email.startswith("#EXT#"):
                all_emails.append(email)
        users_url = data.get("@odata.nextLink")  # Phân trang nếu có nhiều user
    recipients = all_emails
else:
    print("🔎 Đang lấy danh sách email bên ngoài tổ chức...")
    recipients = manual_recipients

mail_payload = {
    "message": {
        "subject": (
            "Mail khen thưởng nội bộ" if SEND_MODE == "organization"
            else "Mail khen thưởng ngoài hệ thống"
        ),
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
                "Ban Quản Lý"
            )
        },
        # SỬA: Dùng BCC để bảo vệ privacy, TO là chính mình để kiểm tra
        "toRecipients": [{"emailAddress": {"address": user_email}}],
        "bccRecipients": [{"emailAddress": {"address": email}} for email in recipients],
        "from": {
            "emailAddress": {
                "address": user_email,
                "name": "Hệ Thống Thông Báo"
            }
        }
    }
}

### Hiển thị danh sách email sẽ gửi
if SEND_MODE == "manual":
    print(f"📧 Danh sách gửi mail thủ công ({len(recipients)} email):")
    for email in recipients:
        print(f"  📨 {email}")
else:
    print(f"📧 Danh sách gửi mail toàn tổ chức ({len(recipients)} email):")
    for email in recipients:
        print(f"  📨 {email}")

res = requests.post(
    f"https://graph.microsoft.com/v1.0/users/{user_email}/sendMail",
    headers=headers,
    json=mail_payload
)
print("📤 Trạng thái gửi mail:", res.status_code, res.status_code in status_messages and status_messages[res.status_code] or "")
if res.status_code != 202:
    print("❌ Chi tiết lỗi:", res.text)

# Step 3 - Ping Graph API nhiều dịch vụ
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}", "👤 User info")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/drive", "📁 OneDrive")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/mailFolders", "📨 MailFolders")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/mailFolders/inbox/messages?$top=1", "📥 Inbox latest")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/joinedTeams", "💬 Teams")
safe_get(f"https://graph.microsoft.com/v1.0/users/{user_email}/calendars", "📅 Calendar list")

# Step 4 - SỬA: Xóa nội dung bằng Graph API thay vì rclone
def delete_folder_contents(folder_name):
    print(f"🧹 Xóa nội dung thư mục {folder_name} bằng Graph API...")
    try:
        list_url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/root:/{folder_name}:/children"
        res = requests.get(list_url, headers=headers)
        
        if res.status_code == 200:
            items = res.json().get("value", [])
            print(f"   Tìm thấy {len(items)} file/folder cần xóa")
            
            for item in items:
                delete_url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/items/{item['id']}"
                del_res = requests.delete(delete_url, headers=headers)
                status = "✅" if del_res.status_code in [200, 204] else "❌"
                print(f"   {status} Xóa {item['name']}: {del_res.status_code}")
        elif res.status_code == 404:
            print(f"   📁 Thư mục {folder_name} không tồn tại, sẽ tự tạo khi upload file")
        else:
            print(f"   ❌ Lỗi truy cập thư mục: {res.status_code}")
    except Exception as e:
        print(f"   ❌ Lỗi xóa thư mục: {e}")

# SỬA: Dùng Graph API thay vì rclone delete
delete_folder_contents("PingE5")

print("📄 Tạo ngẫu nhiên 3-4 file giả trực tiếp trên OneDrive...")
for i in range(random.randint(3, 4)):
    filename = f"note_{random.randint(1000, 9999)}.txt"
    content = f"Đây là file giả số {i+1} để giữ OneDrive hoạt động."
    upload_url = f"https://graph.microsoft.com/v1.0/users/{user_email}/drive/root:/PingE5/{filename}:/content"
    res = requests.put(upload_url, headers=headers, data=content.encode("utf-8"))
    print(f"📎 Upload {filename} → Status:", res.status_code, res.status_code in status_messages and status_messages[res.status_code] or "")

# Step 5 - Upload ảnh từ thư mục local lên OneDrive
print("🖼️ Upload ảnh từ local lên OneDrive...")
local_folder = r"C:\Users\haola\Downloads\PingE5"
remote_folder = "e5renew:PingE5/PingE5Images"

# SỬA: Dùng sync với đường dẫn chính xác
rclone_cmd = f'rclone sync "{local_folder}" {remote_folder} --progress --transfers=4 --checkers=8 --fast-list'
result = os.system(rclone_cmd)

if result != 0:
    print("❌ Rclone sync thất bại!")
else:
    print("✅ Rclone sync thành công!")

print("\n🎉 Script ping E5 hoàn tất!")