from django.shortcuts import render
from nltk.chat.util import Chat, reflections
from .models import *
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you.', 'I\'m doing well, thanks.']),
    (r'what is your name?', ['My name is Chatbot.', 'I am Chatbot.']),
    (r'what can you do?', ['I can answer your questions and engage in conversation.', 
                           'I am here to assist you with any queries you may have.']),
    (r'who created you?', ['I was created by a team of developers.', 
                          'My developers prefer to remain anonymous.']),
    (r'where are you from?', ['I exist in the digital realm.', 
                             'I don\'t have a physical location.']),
    (r'what is the time?', ['I don\'t have access to real-time information.', 
                            'You can check the time on your device.']),
    (r'what is the weather like today?', ['I don\'t have access to weather information.', 
                                         'You can check the weather forecast online.']),
    (r'how old are you?', ['I am forever young.', 
                           'Age is just a number for me.']),
    (r'bye|goodbye', ['Goodbye!', 'Farewell!', 'Have a great day!']),
    (r'quit|exit', ['Goodbye!', 'See you later!', 'Take care!']),
]

chatbot = Chat(patterns, reflections)

def home(request):
    return render(request, 'home.html')

def chat(request):
    user_input = request.GET.get('user_input', '')
    response = chatbot.respond(user_input)   
    
    return render(request, 'chat.html', {'user_input': user_input,"response":response})
