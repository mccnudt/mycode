from sys import argv
script, uer_name = argv
prompt = '>'
print(f'Hi {uer_name}!,i am the {script} script.')
print("i'd like to ask you some quesetions")
print(f"do you like me {uer_name}?")
likes = input(prompt)
print(f'where do you live {uer_name}?')
lives = input(prompt)

print(f"""so you said {likes} about me.
you live in {lives}.""")
