from openai import OpenAI
import user_config
import time

client = OpenAI(api_key=user_config.apiKey)
def send_request(query) :
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": query}]
        )
        return (completion.choices[0].message.content)
    except Exception as e:
        print(f"an error occured : {e}")
        time.sleep(10)

response = send_request("two lines about India")
print(response)