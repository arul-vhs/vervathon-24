import requests
from youtube_transcript_api import YouTubeTranscriptApi
import os

# Function to summarize text using Hugging Face API
def summarize_text(text):
    headers = {
        "Authorization": "Bearer hf_mKxuruoFIhVYkSJBPrRreBhcpegpPbtqtnEY"  # Replace with your actual API key
    }
    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
            headers=headers,
            json={"inputs": text}
        )
        response.raise_for_status()  # Raises an error for bad responses
        return response.json()[0]['summary_text']
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return "Error summarizing text."

# Function to get transcript from YouTube video
def get_youtube_transcript(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split('v=')[-1].split('&')[0]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Combine the transcript text into one string
        combined_text = " ".join([entry['text'] for entry in transcript])
        return combined_text
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def main():
    print("Choose the input method:")
    print("1. PDF")
    print("2. PPT")
    print("3. YouTube link")
    
    choice = input("Enter your choice (1/2/3): ")
    combined_text = ""

    if choice == '1':
        pdf_file_path = input("Enter PDF file path: ")
        combined_text = extract_text_from_pdf(pdf_file_path)  # Your existing PDF extraction function
    elif choice == '2':
        ppt_file_path = input("Enter PPT file path: ")
        combined_text = extract_text_from_ppt(ppt_file_path)  # Your existing PPT extraction function
    elif choice == '3':
        youtube_link = input("Enter YouTube video link: ")
        combined_text = get_youtube_transcript(youtube_link)

    if combined_text:
        simplified_text = summarize_text(combined_text)
        print("Simplified Text:")
        print(simplified_text)
    else:
        print("No content available to summarize.")

if __name__ == "__main__":
    main()
