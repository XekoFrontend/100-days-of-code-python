my_hobbies = {  
  "coding": "python",
  "computer": True,
  "game": 12,
  "music": ["ballad", "instrumental", "rock"]
}

print(f"\n  I. Print full dictionary with all keys and values\n{my_hobbies}\n")
all_items = my_hobbies.items()
print(f"  Print all items\n{all_items}\n")
info_keys = my_hobbies.keys()
info_values = my_hobbies.values()
print(f"  Get all keys\n{info_keys}\n---\n  Get all values\n{info_values}\n")

music_type = my_hobbies["music"][2]
print(f"Your music style is: {music_type} 🤘\n")

print(f"Access values\n{my_hobbies["coding"]}")
# Update a dictionary
my_hobbies["coding"] = "html"
my_hobbies.update({
                    "Game": 32,
                    "book": "minimalism"
                  })
print(f"Update:\n{my_hobbies}")
# Remove the item
my_hobbies.pop("game")
print(f"Remove item 'game'\n{my_hobbies}")
# Checking keys or items occurs in a dictionary
print(f"Checking a key occurs in a dictionary\n{"music" in my_hobbies}")
print(f"Checking a value occurs in a dictionary\n{"minimalism" in my_hobbies.values()}")

print("Print keys with the for loop")
index_key = 0
for key in my_hobbies:
  index_key += 1  
  print(str(index_key) + ". " + key)
  # print(my_hobbies[key]) # Values of keys

print("Print values with the for loop")
index_value = 0
for value in my_hobbies.values():
  index_value += 1  
  print(str(index_value) + ". " + f"{value}")


# Trick wipe an existing dictionary
my_hobbies = {}  # empty_dictionary
print(f"Clean all items in a dictionary: {my_hobbies}\n")

# Adding nesting dictionary
my_hobbies["VietNam"] = {
                          "city": ["Ha Noi", "Da nang", "Ho CHi minh"],
                          "Popular": 90000000,
                          
                          "China":{
                          "city": ["Bejing", "NewYork"],
                          "Popular": 150000000000,
                                    }
                        }
print(f"New nesting list: {my_hobbies}")
hochiminh = my_hobbies["VietNam"]["city"][2]
newyork = my_hobbies["VietNam"]["China"]["city"][1]
print(f"Print Vietnam city: {hochiminh}\nPrint China city: {newyork}\n")