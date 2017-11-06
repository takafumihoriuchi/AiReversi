def censor_ans(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result


def censor(text, word):
  ans = ""
  counter = 0
  
  for i in range(len(text)):
    
    if text[i] == word[0]:
      for j in range(len(word)):
        if text[i+j] == word[j]:
          counter += 1
      if counter == len(word):
        for k in len(word):
          ans += "*"
        i += len(word)
        counter = 0
        continue
    
    ans += text[i]
  
  return ans
    
print(censor("this hack is wack hack", "hack"))
print(censor_ans("this hack is wack hack", "hack"))