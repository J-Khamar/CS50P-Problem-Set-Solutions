def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)

def main():
    text = input("")
    convert(text)

main()