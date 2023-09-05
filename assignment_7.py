def count_vowels(text):
    count = 0
    for character in text :
      if (character in "aAeEiIoOuU "):
         count += 1

    return count
    
text = 'Kewin is a data scientist'
count = count_vowels(text)
print("count:",count)
        
