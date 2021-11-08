punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]


def calculate_frequencies(file_contents):
    new_dict = {}
    
        
    for line in file_contents:
        print(line)
        if line.isalpha() and line.lower() not in uninteresting_words and  line not in punctuations:
          if line in new_dict:
            new_dict[line] += 1
          else:
            new_dict[line] = 1
    print(new_dict)

if __name__ == '__main__':
  file_contents = 'shak.txt' 
  with open(file_contents) as f_hdl:
        f_text = f_hdl.read()
  file_text = f_text.split()
  print(file_text)

  myimage = calculate_frequencies(file_text)
