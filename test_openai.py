# Save as test_openai.py
import openai
import os

api_key = os.getenv('OPENAI_API_KEY')
print(f"Key found: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"Key starts with: {api_key[:10]}...")
    
openai.api_key = api_key

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say 'Hello World'"}],
        max_tokens=10
    )
    print("✅ Success! Response:", response.choices[0].message.content)
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")