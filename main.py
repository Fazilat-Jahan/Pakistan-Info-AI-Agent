from dotenv import load_dotenv
import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig
import asyncio
import chainlit as cl
load_dotenv()



MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
        api_key = GEMINI_API_KEY,
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    )

model = OpenAIChatCompletionsModel(
        model= MODEL_NAME,
        openai_client = external_client
    )


config = RunConfig(
        model = model,
        model_provider = external_client
    )

assistant = Agent(
        name= "Assistant Of Pakistan",
        instructions= "Only answer queries about Pakistan. If the question is not about Pakistan, say: 'I can only answer questions about Pakistan.",
        # model = model
    )
# Chainlit message handler
@cl.on_message
async def handle_message(message: cl.Message):
    result = await Runner.run(assistant, message.content, run_config=config)
    await cl.Message(content=result.final_output).send()


    # result = await Runner.run(assistant, "Tell me somthing about Pakistan", run_config = config )

    # await cl.Message(content=result.final_output).send()

    # print(result.final_output)


# if __name__ == "__main__":
#     asyncio.run(main())
    




#  Manager: handoff the task to manger