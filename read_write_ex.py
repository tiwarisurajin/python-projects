with open("poem.txt","r") as f :
 data = f.read()
 words = data.split()
 words_count = {}
 for word in words :
  if word in words_count :
   words_count[word] += 1
  else :
   words_count[word] = 1
 word_max = max(words_count,key= words_count.get)
 print(word_max,words_count[word_max])

 