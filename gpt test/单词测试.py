import re
def analyze_text(text:str) -> dict:
    res=text.lower()
    char_count = len(res)
    # text1 = "Python,python! hello-world"
    # text=text1.lower()
    words = re.findall(r"[a-z]+",res)
    print(words)

    # word_list = res.split()
    # word_list_clean = []
    #
    # for word in word_list:
    #     word = word.strip(",.!? ")
    #     if word:
    #         word_list_clean.append(word)
    word_count = len(words)

    counts = {}
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1

    unique_words = len(counts)

    sorted_words = sorted(counts.items(),key=lambda items:(-items[1],items[0]))
    top_words = sorted_words[:3]

    return {"char_count":char_count,"word_count":word_count,"unique_words":unique_words,"counts":counts,"top_words":top_words}
print(analyze_text( "hello-world,hello"))