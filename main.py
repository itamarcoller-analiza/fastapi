import random
from fastapi import FastAPI
from routes import user_route


app = FastAPI()

app.include_router(user_route.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/chat")
async def chat():
    chat_response = ['Hello! How can I assist you today?','Sure! What would you like to know?','I am here to help you with any questions you have.','Feel free to ask me anything!',
                     'What topic are you interested in discussing?','I can provide information on a wide range of subjects.','Let me know how I can assist you further.','Is there something specific you would like to talk about?',
                     'I am ready to help you with your inquiries.','Thank you for reaching out! How can I assist you?']
    return {"responses": chat_response.index(chat_response[random.randint(0, len(chat_response)-1)])}



