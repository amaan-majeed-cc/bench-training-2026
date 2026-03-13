# exercise_1.py — Word frequency counter

# Write a function word_frequency(text) that takes a string, splits it into words, and returns a dict with {word: count}.
# Then: load a paragraph of text (hardcode something a few sentences long), call your
# function, and print the top 5 most common words.
# Ignore punctuation. Lowercase everything before counting. Use sorted() with a key.

def word_frequency(text):
  word_dict = {}
  for word in text.split():
    word = word.lower().strip(".,")
    if word in word_dict:
      word_dict[word] += 1
    else:
      word_dict[word] = 1
  print(dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:5]))

  # # Also found this to work
  # from collections import Counter
  # print(dict(Counter(word_dict).most_common(5)))

word_frequency("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")