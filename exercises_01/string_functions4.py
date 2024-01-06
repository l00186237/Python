text_with_brackets = "(John Doherty was here)"
text_without_brackets = text_with_brackets.strip('(')
text_without_brackets = text_without_brackets.strip(')')
print(text_without_brackets)