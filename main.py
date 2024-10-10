import os
from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Bot Framework Adapter with Azure credentials
APP_ID = os.getenv('MICROSOFT_APP_ID')
APP_PASSWORD = os.getenv('MICROSOFT_APP_PASSWORD')

adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

async def on_message(turn_context: TurnContext):
    # Echo back the user's message
    await turn_context.send_activity(f"You said: {turn_context.activity.text}")

async def messages(req):
    body = await req.json()
    activity = Activity().deserialize(body)
    auth_header = req.headers.get('Authorization', '')
    response = await adapter.process_activity(activity, auth_header, on_message)
    return web.Response(status=200)

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, port=3978)
