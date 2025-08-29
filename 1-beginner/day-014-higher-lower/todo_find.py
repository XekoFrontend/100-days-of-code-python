# Tìm release giống nhau và chỉnh sửa nếu cần.


data = [
    {
        "name": "Mafalda",
        "release": 30000000,
        "description": "Câu chuyện về một cô bé thông minh và những quan điểm xã hội của cô.",
        "country": "Argentina"
    },
    {
        "name": "Cavaleiros do Zodíaco (Saint Seiya)",
        "release": 25000000,
        "description": "Câu chuyện về những chiến binh bảo vệ Athena và cuộc chiến chống lại các vị thần.",
        "country": "Brazil"
    },
    {
        "name": "El Eternauta",
        "release": 20000000,
        "description": "Câu chuyện về một người đàn ông chiến đấu chống lại những kẻ xâm lược ngoài hành tinh.",
        "country": "Argentina"
    },
    {
        "name": "Lobo",
        "release": 15000000,
        "description": "Câu chuyện về một kẻ sát thủ ngoài hành tinh với tính cách nổi loạn.",
        "country": "Mexico"
    },
    {
        "name": "The Adventures of Tintin: The Crab with the Golden Claws",
        "release": 10000000,
        "description": "Cuộc phiêu lưu của Tintin trong cuộc điều tra về một vụ buôn lậu.",
        "country": "Belgium"
    },
    {
        "name": "Vicky the Viking",
        "release": 8000000,
        "description": "Câu chuyện về một cậu bé Viking thông minh và những cuộc phiêu lưu của cậu.",
        "country": "Thụy Điển"
    },
    {
        "name": "The Little Vampire",
        "release": 6000000,
        "description": "Câu chuyện về một cậu bé ma cà rồng và những cuộc phiêu lưu của cậu.",
        "country": "Đức"
    },
    {
        "name": "Moomin",
        "release": 5000000,
        "description": "Câu chuyện về những sinh vật Moomin và cuộc sống của họ trong một thế giới huyền diệu.",
        "country": "Phần Lan"
    },
    {
        "name": "Corto Maltese: The Celestial Tombstone",
        "release": 4000000,
        "description": "Cuộc phiêu lưu của Corto Maltese trong một thế giới kỳ diệu.",
        "country": "Ý"
    },
    {
        "name": "Nemi",
        "release": 3000000,
        "description": "Câu chuyện về một cô gái trẻ và những suy nghĩ của cô về cuộc sống hiện đại.",
        "country": "Na Uy"
    },
    {
        "name": "The Beano",
        "release": 2000000,
        "description": "Tạp chí truyện tranh nổi tiếng của Anh với những nhân vật hài hước.",
        "country": "England"
    },
    {
        "name": "The Phoenix",
        "release": 1500000,
        "description": "Tạp chí truyện tranh dành cho trẻ em với nhiều câu chuyện thú vị và giáo dục.",
        "country": "England"
    },
    {
        "name": "Boule et Bill",
        "release": 1000000,
        "description": "Câu chuyện về một cậu bé và chú chó của mình với những tình huống hài hước.",
        "country": "France"
    },
    {
        "name": "César, le petit roi",
        "release": 800000,
        "description": "Câu chuyện về một cậu bé vua và những cuộc phiêu lưu của cậu.",
        "country": "France"
    },
    {
        "name": "Popeye",
        "release": 600000,
        "description": "Câu chuyện về một người đàn ông ăn rau cải và những cuộc phiêu lưu của anh.",
        "country": "US"
    },
    {
        "name": "Garfield",
        "release": 500000,
        "description": "Câu chuyện về một chú mèo lười biếng và những tình huống hài hước trong cuộc sống hàng ngày.",
        "country": "US"
    },
    {
        "name": "Peanuts",
        "release": 400000,
        "description": "Câu chuyện về những nhân vật trẻ em và những suy nghĩ ngây thơ của họ.",
        "country": "US"
    },
    {
        "name": "Tintin in America",
        "release": 200000,
        "description": "Cuộc phiêu lưu của Tintin khi anh đến US và đối mặt với những kẻ xấu.",
        "country": "Belgium"
    },
    {
        "name": "Lucky Luke: The Daltons' Escape",
        "release": 150000,
        "description": "Cuộc phiêu lưu của Lucky Luke khi anh phải ngăn chặn những tên tội phạm Daltons.",
        "country": "France"
    },
    {
        "name": "One Piece",
        "release": 49000000,
        "description": "Một cuộc phiêu lưu của Luffy và băng hải tặc của anh ấy trong hành trình tìm kiếm kho báu.",
        "country": "Japan"
    },
    {
        "name": "Naruto",
        "release": 25000000,
        "description": "Câu chuyện về một ninja trẻ tuổi với ước mơ trở thành Hokage.",
        "country": "Japan"
    },
    {
        "name": "Batman",
        "release": 65000000,
        "description": "Hành trình của Bruce Wayne, một người đàn ông chiến đấu chống lại tội phạm trong thành phố Gotham.",
        "country": "US"
    },
    {
        "name": "Spider-Man",
        "release": 50000000,
        "description": "Câu chuyện về Peter Parker, một thanh niên có sức mạnh siêu nhiên và trách nhiệm lớn.",
        "country": "US"
    },
    {
        "name": "Attack on Titan",
        "release": 10000000,
        "description": "Cuộc chiến giữa nhân loại và những sinh vật khổng lồ ăn thịt người.",
        "country": "Japan"
    },
    {
        "name": "Dragon Ball",
        "release": 30000000,
        "description": "Cuộc phiêu lưu của Goku trong việc tìm kiếm các viên ngọc rồng.",
        "country": "Japan"
    },
    {
        "name": "X-Men",
        "release": 40000000,
        "description": "Những người đột biến với khả năng đặc biệt chiến đấu cho hòa bình giữa con người và đột biến.",
        "country": "US"
    },
    {
        "name": "Superman",
        "release": 60000000,
        "description": "Câu chuyện về một siêu anh hùng đến từ hành tinh Krypton.",
        "country": "US"
    },
    {
        "name": "Death Note",
        "release": 30000000,
        "description": "Một cuộc chiến trí tuệ giữa một học sinh và một thám tử.",
        "country": "Japan"
    },
    {
        "name": "My Hero Academia",
        "release": 20000000,
        "description": "Câu chuyện về một thế giới nơi mọi người có siêu năng lực và một cậu bé không có năng lực.",
        "country": "Japan"
    },
    {
        "name": "Tintin",
        "release": 35000000,
        "description": "Cuộc phiêu lưu của một nhà báo trẻ và chú chó của anh ấy.",
        "country": "Belgium"
    },
    {
        "name": "Asterix",
        "release": 30000000,
        "description": "Câu chuyện về một người Gaul nhỏ bé và những cuộc phiêu lưu của anh ấy.",
        "country": "France"
    },
    {
        "name": "Sailor Moon",
        "release": 25000000,
        "description": "Câu chuyện về một cô gái trẻ trở thành chiến binh bảo vệ hòa bình.",
        "country": "Japan"
    },
    {
        "name": "Wonder Woman",
        "release": 40000000,
        "description": "Câu chuyện về một nữ siêu anh hùng với sức mạnh phi thường.",
        "country": "US"
    },
    {
        "name": "Maus",
        "release": 20000000,
        "description": "Một tác phẩm đồ họa về Holocaust, sử dụng động vật để kể câu chuyện.",
        "country": "US"
    },
    {
        "name": "The Walking Dead",
        "release": 30000000,
        "description": "Cuộc sống của những người sống sót trong một thế giới bị xâm chiếm bởi zombie.",
        "country": "US"
    },
    {
        "name": "Bleach",
        "release": 15000000,
        "description": "Câu chuyện về một thiếu niên có khả năng nhìn thấy linh hồn và chiến đấu với các linh hồn xấu.",
        "country": "Japan"
    },
    {
        "name": "Fullmetal Alchemist",
        "release": 30000000,
        "description": "Câu chuyện về hai anh em sử dụng giả kim thuật để tìm kiếm viên đá huyền bí.",
        "country": "Japan"
    },
    {
        "name": "V for Vendetta",
        "release": 25000000,
        "description": "Một câu chuyện về sự nổi dậy chống lại chế độ độc tài.",
        "country": "England"
    },
    {
        "name": "Saga",
        "release": 15000000,
        "description": "Một câu chuyện không gian về tình yêu và chiến tranh giữa hai chủng tộc.",
        "country": "US"
    },
    {
        "name": "Naruto Shippuden",
        "release": 20000000,
        "description": "Tiếp nối cuộc phiêu lưu của Naruto khi anh trưởng thành và đối mặt với những kẻ thù mạnh mẽ.",
        "country": "Japan"
    },
    {
        "name": "One Punch Man",
        "release": 18000000,
        "description": "Câu chuyện về một siêu anh hùng có thể đánh bại bất kỳ kẻ thù nào chỉ bằng một cú đấm.",
        "country": "Japan"
    },
    {
        "name": "The Sandman",
        "release": 12000000,
        "description": "Một câu chuyện kỳ diệu về giấc mơ và những sinh vật trong thế giới giấc mơ.",
        "country": "US"
    },
    {
        "name": "Akira",
        "release": 10000000,
        "description": "Một câu chuyện khoa học viễn tưởng về một Tokyo tương lai hỗn loạn.",
        "country": "Japan"
    },
    {
        "name": "Bone",
        "release": 8000000,
        "description": "Cuộc phiêu lưu của ba anh em Bone trong một thế giới kỳ diệu.",
        "country": "US"
    },
    {
        "name": "Scott Pilgrim",
        "release": 7000000,
        "description": "Câu chuyện về một chàng trai trẻ phải đánh bại bảy người yêu cũ của bạn gái mình.",
        "country": "Canada"
    },
    {
        "name": "Hellboy",
        "release": 6000000,
        "description": "Câu chuyện về một sinh vật siêu nhiên chiến đấu chống lại các thế lực ác quỷ.",
        "country": "US"
    },
    {
        "name": "Daredevil",
        "release": 5000000,
        "description": "Câu chuyện về một luật sư mù với khả năng siêu nhiên chiến đấu chống lại tội phạm.",
        "country": "US"
    },
    {
        "name": "Death Note: Another Note",
        "release": 4000000,
        "description": "Một câu chuyện phụ của Death Note, khám phá thêm về các nhân vật.",
        "country": "Japan"
    },
    {
        "name": "GTO: Great Teacher Onizuka",
        "release": 3000000,
        "description": "Câu chuyện về một cựu băng nhóm trở thành giáo viên và những thử thách trong nghề.",
        "country": "Japan"
    },
    {
        "name": "Fairy Tail",
        "release": 2000000,
        "description": "Cuộc phiêu lưu của một nhóm pháp sư trong một thế giới phép thuật.",
        "country": "Japan"
    },
    {
        "name": "One Piece: Stampede",
        "release": 1500000,
        "description": "Một bộ phim hoạt hình dựa trên manga One Piece, với những cuộc phiêu lưu mới.",
        "country": "Japan"
    },
    {
        "name": "The Adventures of Tintin",
        "release": 1200000,
        "description": "Cuộc phiêu lưu của Tintin và những người bạn trong các chuyến đi khắp thế giới.",
        "country": "Belgium"
    },
    {
        "name": "The League of Extraordinary Gentlemen",
        "release": 1000000,
        "description": "Một nhóm nhân vật văn học nổi tiếng hợp tác để chống lại các thế lực xấu.",
        "country": "England"
    },
    {
        "name": "Locke & Key",
        "release": 800000,
        "description": "Câu chuyện về một gia đình khám phá những chiếc chìa khóa kỳ diệu trong ngôi nhà của họ, dẫn đến những bí mật và mối nguy hiểm.",
        "country": "US"
    },
    {
        "name": "The Umbrella Academy",
        "release": 700000,
        "description": "Một nhóm anh hùng siêu nhiên phải hợp tác để ngăn chặn một thảm họa toàn cầu.",
        "country": "US"
    },
    {
        "name": "Sandman Mystery Theatre",
        "release": 600000,
        "description": "Câu chuyện về một siêu anh hùng trong những năm 1930, giải quyết các vụ án bí ẩn.",
        "country": "US"
    },
    {
        "name": "Yona of the Dawn",
        "release": 500000,
        "description": "Câu chuyện về một công chúa bị phản bội và hành trình tìm kiếm sức mạnh.",
        "country": "Japan"
    },
    {
        "name": "Tokyo Ghoul",
        "release": 400000,
        "description": "Câu chuyện về một sinh viên đại học trở thành nửa người nửa quái vật.",
        "country": "Japan"
    },
    {
        "name": "One Punch Man: Road to Hero",
        "release": 300000,
        "description": "Một câu chuyện phụ về hành trình của Saitama trước khi trở thành One Punch Man.",
        "country": "Japan"
    },
    {
        "name": "The Boys",
        "release": 200000,
        "description": "Một câu chuyện về một nhóm người bình thường chống lại các siêu anh hùng tham lam.",
        "country": "US"
    },
    {
        "name": "Saga of Tanya the Evil",
        "release": 150000,
        "description": "Câu chuyện về một người đàn ông tái sinh thành một cô bé trong một thế giới chiến tranh.",
        "country": "Japan"
    },
    {
        "name": "Berserk",
        "release": 100000,
        "description": "Cuộc phiêu lưu của Guts, một chiến binh trong một thế giới tăm tối và đầy quái vật.",
        "country": "Japan"
    },
    {
        "name": "Fables",
        "release": 80000,
        "description": "Câu chuyện về các nhân vật cổ tích sống trong thế giới hiện đại.",
        "country": "US"
    },
    {
        "name": "Locke & Key: Welcome to Lovecraft",
        "release": 60000,
        "description": "Phần đầu tiên của loạt truyện về những chiếc chìa khóa kỳ diệu và những bí mật của gia đình Locke.",
        "country": "US"
    },
    {
        "name": "Death Note: The Last Name",
        "release": 50000,
        "description": "Phần tiếp theo của Death Note, tiếp tục cuộc chiến giữa Light và L.",
        "country": "Japan"
    },
    {
        "name": "Kaguya-sama: Love Is War",
        "release": 40000,
        "description": "Câu chuyện hài hước về hai học sinh xuất sắc trong cuộc chiến tình yêu.",
        "country": "Japan"
    },
    {
        "name": "Blue Exorcist",
        "release": 30000,
        "description": "Câu chuyện về một cậu bé phát hiện ra mình là con trai của quỷ và quyết định trở thành một exorcist.",
        "country": "Japan"
    },
    {
        "name": "Dorohedoro",
        "release": 20000,
        "description": "Câu chuyện kỳ quái về một người đàn ông bị biến thành thằn lằn và cuộc tìm kiếm kẻ đã làm điều đó.",
        "country": "Japan"
    },
    {
        "name": "The Promised Neverland",
        "release": 15000,
        "description": "Câu chuyện về những đứa trẻ trong một trại trẻ mồ côi phát hiện ra sự thật kinh hoàng.",
        "country": "Japan"
    },
    {
        "name": "Mob Psycho 100",
        "release": 10000,
        "description": "Câu chuyện về một cậu bé có sức mạnh tâm linh và hành trình tìm kiếm bản thân.",
        "country": "Japan"
    },
    {
        "name": "Your Lie in April",
        "release": 8000,
        "description": "Câu chuyện về một nhạc sĩ trẻ phải đối mặt với quá khứ và tìm lại niềm đam mê âm nhạc.",
        "country": "Japan"
    },
    {
        "name": "Haikyuu!!",
        "release": 7000,
        "description": "Câu chuyện về một đội bóng chuyền trung học và những ước mơ của các thành viên.",
        "country": "Japan"
    },
    {
        "name": "Kimi ni Todoke",
        "release": 6000,
        "description": "Câu chuyện về một cô gái nhút nhát và hành trình tìm kiếm tình bạn và tình yêu.",
        "country": "Japan"
    },
    {
        "name": "March Comes in Like a Lion",
        "release": 5000,
        "description": "Câu chuyện về một kỳ thủ shogi trẻ tuổi và cuộc sống của anh ta.",
        "country": "Japan"
    },
    {
        "name": "Yuri!!! on ICE",
        "release": 4000,
        "description": "Câu chuyện về một vận động viên trượt băng nghệ thuật và hành trình tìm kiếm bản thân.",
        "country": "Japan"
    },
    {
        "name": "The Ancient Magus' Bride",
        "release": 3000,
        "description": "Câu chuyện về một cô gái trẻ và mối quan hệ của cô với một pháp sư cổ đại.",
        "country": "Japan"
    },
    {
        "name": "Black Clover",
        "release": 2000,
        "description": "Câu chuyện về một cậu bé không có phép thuật nhưng vẫn mơ ước trở thành Wizard King.",
        "country": "Japan"
    },
    {
        "name": "Danganronpa: The Animation",
        "release": 1500,
        "description": "Câu chuyện về một nhóm học sinh bị mắc kẹt trong một trò chơi sinh tồn.",
        "country": "Japan"
    },
    {
        "name": "Re:Zero - Starting Life in Another World",
        "release": 1000,
        "description": "Câu chuyện về một chàng trai bị đưa đến một thế giới khác và khả năng quay ngược thời gian.",
        "country": "Japan"
    },
    {
        "name": "The Seven Deadly Sins",
        "release": 800,
        "description": "Câu chuyện về một nhóm hiệp sĩ bị cáo buộc phản bội và hành trình tìm kiếm sự trong sạch.",
        "country": "Japan"
    },
    {
        "name": "The King's Avatar",
        "release": 20000000,
        "description": "Câu chuyện về một game thủ chuyên nghiệp trong thế giới game online.",
        "country": "China"
    },
    {
        "name": "Mo Dao Zu Shi",
        "release": 15000000,
        "description": "Câu chuyện về một pháp sư bị lưu đày và hành trình tìm kiếm sự thật.",
        "country": "China"
    },
    {
        "name": "Noblesse",
        "release": 10000000,
        "description": "Câu chuyện về một quý tộc bất tử và cuộc chiến chống lại các thế lực xấu.",
        "country": "Korea"
    },
    {
        "name": "Tower of God",
        "release": 12000000,
        "description": "Cuộc phiêu lưu của một cậu bé trong một tháp bí ẩn với nhiều thử thách.",
        "country": "Korea"
    },
    {
        "name": "Doraemon (Vietnamese version)",
        "release": 5000000,
        "description": "Phiên bản tiếng Việt của câu chuyện về chú mèo máy đến từ tương lai.",
        "country": "Việt Nam"
    },
    {
        "name": "Thần Đồng Đất Việt",
        "release": 3000000,
        "description": "Câu chuyện hài hước về những nhân vật lịch sử trong bối cảnh hiện đại.",
        "country": "Việt Nam"
    },
    {
        "name": "Bong Bóng Duyệt",
        "release": 2000000,
        "description": "Câu chuyện về những cuộc phiêu lưu của một nhóm bạn trẻ.",
        "country": "Việt Nam"
    },
    {
        "name": "Les Aventures de Tintin",
        "release": 35000000,
        "description": "Cuộc phiêu lưu của Tintin và chú chó Milou trong các chuyến đi khắp thế giới.",
        "country": "Belgium"
    },
    {
        "name": "Astérix",
        "release": 30000000,
        "description": "Câu chuyện về một người Gaul nhỏ bé và những cuộc phiêu lưu của anh ấy.",
        "country": "France"
    },
    {
        "name": "Blueberry",
        "release": 25000000,
        "description": "Câu chuyện về một sĩ quan quân đội trong thời kỳ miền Tây hoang dã.",
        "country": "France"
    },
    {
        "name": "Lucky Luke",
        "release": 20000000,
        "description": "Cuộc phiêu lưu của một cao bồi nhanh nhất miền Tây.",
        "country": "France"
    },
    {
        "name": "Les Schtroumpfs (The Smurfs)",
        "release": 15000000,
        "description": "Câu chuyện về những sinh vật nhỏ bé màu xanh và cuộc sống của họ trong rừng.",
        "country": "Belgium"
    },
    {
        "name": "Corto Maltese",
        "release": 12000000,
        "description": "Cuộc phiêu lưu của một thuyền trưởng trong những năm đầu thế kỷ 20.",
        "country": "Ý"
    },
    {
        "name": "Valérian and Laureline",
        "release": 10000000,
        "description": "Câu chuyện khoa học viễn tưởng về hai đặc vụ không gian.",
        "country": "France"
    },
    {
        "name": "Les Petits Hommes",
        "release": 8000000,
        "description": "Câu chuyện về những người nhỏ bé sống trong một thế giới lớn.",
        "country": "Belgium"
    },
    {
        "name": "Titeuf",
        "release": 6000000,
        "description": "Câu chuyện hài hước về cuộc sống của một cậu bé tiểu học.",
        "country": "France"
    },
    {
        "name": "Gaston Lagaffe",
        "release": 5000000,
        "description": "Câu chuyện về một nhân viên văn phòng vụng về và những rắc rối của anh ta.",
        "country": "France"
    },
    {
        "name": "Les Aventures de Spirou et Fantasio",
        "release": 4000000,
        "description": "Cuộc phiêu lưu của hai nhân vật Spirou và Fantasio trong thế giới kỳ diệu.",
        "country": "Belgium"
    },
    {
        "name": "Lucky Luke: Daisy Town",
        "release": 3000000,
        "description": "Cuộc phiêu lưu của Lucky Luke trong thị trấn Daisy, nơi có nhiều rắc rối.",
        "country": "France"
    },
    {
        "name": "Asterix and Obelix",
        "release": 2500000,
        "description": "Câu chuyện về hai người bạn Gaul trong cuộc chiến chống lại người La Mã.",
        "country": "France"
    },
    {
        "name": "Les Schtroumpfs: The Smurfs",
        "release": 2000000,
        "description": "Cuộc sống hàng ngày của những sinh vật nhỏ bé màu xanh trong rừng.",
        "country": "Belgium"
    },
    {
        "name": "Cédric",
        "release": 1500000,
        "description": "Câu chuyện hài hước về một cậu bé và những tình huống dở khóc dở cười trong cuộc sống.",
        "country": "France"
    },
    {
        "name": "Titeuf: The Adventures",
        "release": 1000000,
        "description": "Cuộc phiêu lưu hài hước của một cậu bé tiểu học và những người bạn của mình.",
        "country": "France"
    }
]