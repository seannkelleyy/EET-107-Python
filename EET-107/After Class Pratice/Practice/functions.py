from guizero import App, Text, Box, TextBox, PushButton


app = App(title='Greeting Generator')

def greetings(name1, greeting1):
    return f'Hello {name1}, {greeting1}'


name = input('What is the persons name?: ')
greeting = input(f'What would you like to tell {name}?: ')

your_greeting = greetings(name, greeting)

print(your_greeting)

app.display()
