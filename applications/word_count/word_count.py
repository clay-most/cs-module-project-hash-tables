def word_count(string):
    tempStore = {}
    ignored = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()

    splitString = "".join(word.lower()
                          for word in string if not word in ignored).split()
    print(splitString)
    
    for word in splitString:
        if word in tempStore:
            tempStore[word] += 1
        else:
            tempStore[word] = 1

    return tempStore


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
