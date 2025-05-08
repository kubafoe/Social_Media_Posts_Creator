from flask import session, request, render_template, app
from ollama import chat
from dotenv import load_dotenv
# from sqlite3 import connect in future
import os


# Wczytaj sekretny klucz
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

class data_form:
    def __init__(self, topic, goal, platform, details, more_information, option_html):
        self.topic = topic
        self.goal = goal
        self.platform = platform
        self.details = details
        self.more_information = more_information
        self.option_html = option_html
        self.data = [topic, goal, platform, details, more_information, option_html,]

    def to_dict(self):
        return {
        "topic": self.topic,
        "goal": self.goal,
        "platform": self.platform,
        "details": self.details,
        "more_information": self.more_information,
        "option_html": self.option_html,
        }

# Define rules on each SM platform.
def platform_requier(platform):
        if platform == "instagram":
            platform_requier = "Instagram - Keep short, add line breaks, include emojis."
            return platform_requier            
        elif platform == "facebook":
            platform_requier = "Facebook - Start strong, ask questions, use casual tone."
            return platform_requier            
        elif platform == "linkedin":
            platform_requier = "Linkedin - Be professional, add value, include a call-to-action."
            return platform_requier            
        elif platform == "X":
            platform_requier = "X/Twitter - Be concise, use hashtags, spark curiosity.Max 280 characters."
            return platform_requier            


# Wczytaj dane z formularza -> wyślij dane do AI -> wprowadź na stronie index.html
def send_bot(): 
    # Wczytaj dane z formularza
    form = data_form (
    request.form.get('topic'),
    request.form.get('goal'),
    request.form.get('platform'),
    request.form.get('details'),
    request.form.get('more_information'),
    request.form.get('option_html')
    )
    print(form.to_dict())
    print(form)
    print(form.topic)
    

    if not form.topic.strip() or not form.details.strip():
        error = "Complete the required fields!"
        print(error)
        return render_template('index.html',error=error)
    else:
        respond = send_data(form.topic,form.goal,form.platform,form.details,form.more_information,form.option_html)
        session['respond'] = respond
        session['forms'] = form.to_dict()
        print("send_BOT + send_data Success")
        return render_template("index.html", respond=respond)
   
# Wyślij dane do AI ze wczytanimi informacje z funkcji send_ bot()
def send_data(topic,goal,platform,details,more_information,option_html):

    print("Wyslij dane uruchomione" )
    prompt_requier = platform_requier(platform)

    prompt = f"Create a social media post for {prompt_requier} about {topic} in goal {goal} in context {details}, optionaly {more_information}"

    print(prompt)

    if option_html == '1':
        prompt += " Important use html for decoration."

    response = chat(model="gemma3", messages=[{"role": "user", "content": prompt}])

    print(prompt)
    respond = response.message.content
    return respond

def send_data_custom():
    prompt = request.form.get('custom_prompt')
    print(f"prompt = {prompt}")
    if prompt == None or prompt == "":
        error = "Complete the required fields!"
        print(error)
        return  render_template("custom.html", error=error)
    else:
        response = chat(model="gemma3", messages=[{"role": "user", "content": prompt}])
        custom_respond = response.message.content
        print(f"response: {response}")
        session['custom_respond'] = custom_respond
        print(custom_respond)
        return render_template("custom.html", custom_respond=custom_respond)
    




 