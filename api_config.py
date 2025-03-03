import os
import openai
from dotenv import load_dotenv

load_dotenv()

zhipu_base = os.getenv('ZHIPU_BASE')
zhipu_api_key = os.getenv('ZHIPU_API_KEY')
openai_base = os.getenv('OPENAI_BASE')
openai_api_key = os.getenv('OPENAI_API_KEY')


def openai_setter(model):
    if model == 'glm-4-plus':
        openai.api_key = zhipu_api_key
        openai.api_base = zhipu_base
    elif model == 'gpt-4o':
        openai.api_key = openai_api_key
        openai.api_base = openai_base
    else:
        raise ValueError('Invalid model')


def run_llm(system_prompt, message, model='glm-4-plus', temperature=0.7):
    openai_setter(model)
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system",
             "content": system_prompt},
            {"role": "user",
             "content": message}
        ],
        temperature=temperature
    )
    print(model + ' output:\n', completion.choices[0].message['content'].strip())
    return completion.choices[0].message['content'].strip()


def run_llm_with_customized_messages(messages, model='glm-4-plus', temperature=0.7):
    openai_setter(model)
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    print(model + ' output:\n', completion.choices[0].message['content'].strip())
    return completion.choices[0].message['content'].strip()