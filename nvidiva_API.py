import os
from dotenv import load_dotenv 
# from openai import OpenAI
from google import genai

load_dotenv()


client = genai.Client( 
  api_key = os.getenv("GOOGLE_API_KEY")
)


def structured_generator(prompt):

    response = client.models.generate_content(
        # model="nvidia/gliner-pii",
        #  model="gemini-1.5-flash",
        model="gemini-3.5-flash"  ,
        contents=prompt
    )

    return response.text






# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(
#     base_url="https://integrate.api.nvidia.com/v1",
#     api_key=os.getenv("NVIDIA_API-KEY")
# )

# def structured_generator(prompt):

#     completion = client.chat.completions.create(
#         model="minimaxai/minimax-m2.7",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ],
#         temperature=1,
#         top_p=0.95,
#         max_tokens=8192,
#         stream=False
#     )

#     return completion.choices[0].message.content
#     # return completion.text
