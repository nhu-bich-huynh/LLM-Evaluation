from google import genai

client = genai.Client(api_key="AIzaSyBEx6cNuDD9XgrV0oO10TZ7ZQzzddCr_r8")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="""Compare the similarity between sentence 1 and 2 on a scale from 0 (totally different) to 1 (totally identical). Return ONLY that number.

Sentence 1:
He is rather surprisingly in his house near Malaga in Spain.

Sentence 2:
He rather is surprisingly in his house near Malaga in Spain."""
)
print(response.text)