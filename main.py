from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import openai

openai.api_key = str(input("Enter your openai key: "))

while True:
    link = str(input("Enter link: "))
    try:
        video_id = link.split("v=")[1].split("&")[0]
        srt = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([line['text'] for line in srt])
    except:
        print("Invalid link.")
        continue
    sum_len = str(input("How long should the summary be: "))
    try:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are transcript summarizer"},
        {"role": "user", "content": f"Summarize this: {transcript} in {sum_len}"}])
        summary = response["choices"][0]["message"]["content"]
        print(f"\n{summary}")
    except:
        print("Invalid Key.")
        openai.api_key = str(input("Enter your openai key: "))
        continue
    while True:
        cont = input("\nWould you like to continue (y/n): ").strip().lower()
        if cont == "y":
            break
        elif cont == "n":
            exit(0)
        else:
            print("\nPlease enter 'y' or 'n'.")
