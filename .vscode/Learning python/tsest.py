def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

txt=input("enter text: ")
tst=txt.join("")
print(count_char(txt,"s"))