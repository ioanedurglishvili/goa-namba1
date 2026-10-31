# 1. შექმენით ცვლადი word = "Python". ინდექსების გამოყენებით ეკრანზე გამოიტანეთ ამ სიტყვის პირველი და ბოლო ასოები.

# 2. მოცემულია სიტყვა text = "apple". ინდექსირებით ეკრანზე გამოიტანეთ მისი შუა ასო.

# 3. მოცემულია word = "orange". for ციკლის მეშვეობით დაბეჭდეთ ამ სიტყვის თითოეული ასო ახალ-ახალ ხაზზე.

# 4. for loop = ის გამოყენებით დაბეჭდეთ რიცხვები 0 - დან 20 - მდე, მხოლოდ ლუწები.

# 5. for loop - ის გამოყენებით დაბეჭდეთ რიცხვები 20 - დან 0 - მდე, მხოლოდ ლუწები.

# 6. მოცემულია word = "developer". სლაისინგის  მეშვეობით ეკრანზე გამოიტანეთ სიტყვის მხოლოდ პირველი 3 ასო.

# 7. მოცემულია word = "computer". უარყოფითი სლაისინგით ამოჭერით და დაბეჭდეთ სიტყვის ბოლო 2 ასო.

# 8. მოცემულია text = "welcome". სლაისინგის ნაბიჯის მეშვეობით  შებრუნებული სახით გამოიტანეთ ეს სიტყვა ეკრანზე.

word = "Python"

print(word[0])
print(word[5])

text = "apple"
print(text[2])

word = "orange"

for i in "orange":
    print(i)


for i in range(0,20,2):
    print(i)


for i in range(20,0):
   print(i)


text = "developer"
print(text[0:3])

word = "computer"
print(word[6:7])

text = "welcome"
print(text[6])
print(text[5])
print(text[4])
print(text[3])
print(text[2])
print(text[1])
print(text[0])
















