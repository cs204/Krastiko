def replace_emoticons(text):

    text = text.replace(":)", '🙂')


    text = text.replace(":(", '🙁')

    return text


input_text = input("")

output_text = replace_emoticons(input_text)
print(output_text)
