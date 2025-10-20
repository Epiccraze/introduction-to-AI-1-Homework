import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import random
init(autoreset=True)

def load_data(file_path='imdb_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        exit()

movies_df = load_data()
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def list_genres(df):
    return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(', ') for genre in sublist))

genres = list_genres(movies_df)

def display_movie_details(row, polarity):
    sentiment = "Positive 😊" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
    print(f"\n{Fore.CYAN}🎬 Title: {row['Series_Title']}")
    print(f"{Fore.GREEN}🎭 Genre: {row['Genre']}")
    print(f"{Fore.MAGENTA}📝 Overview: {row['Overview']}")
    print(f"{Fore.BLUE}⭐ IMDB Rating: {row['IMDB_Rating']}")
    print(f"{Fore.YELLOW}📊 Sentiment Analysis: {sentiment} (Polarity: {polarity:.2f})\n")

def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_df = movies_df
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= rating]

    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)
    recommendations = []

    for _, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0)) or not mood:
            recommendations.append((row, polarity))
        if len(recommendations) == top_n:
            break

    return recommendations if recommendations else "No suitable movie recommendations found."

def random_recommendation():
    movie = movies_df.sample(1).iloc[0]
    polarity = TextBlob(str(movie['Overview'])).sentiment.polarity
    return movie, polarity

def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

def handle_ai(name):
    print(Fore.BLUE + "\n🔍 Let's find the perfect movie for you!\n")
    print(Fore.GREEN + "Available Genres: ", end="")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}{idx}. {genre}")
    print()

    while True:
        genre_input = input(Fore.YELLOW + "Enter genre number or name: ").strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input) - 1]
            break
        elif genre_input.title() in genres:
            genre = genre_input.title()
            break
        print(Fore.RED + "Invalid input. Try again.\n")

    mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()
    print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
    processing_animation()
    polarity = TextBlob(mood).sentiment.polarity
    mood_desc = "Positive 😊" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
    print(f"\n{Fore.GREEN}Your mood is {mood_desc} (Polarity: {polarity:.2f}).\n")

    while True:
        rating_input = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6 - 9.3) or 'skip': ").strip()
        if rating_input.lower() == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

    print(Fore.BLUE + f"\nFinding movies for {name}", end="", flush=True)
    processing_animation()
    recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)
    if isinstance(recs, str):
        print(Fore.RED + recs + "\n")
    else:
        for row, polarity in recs:
            display_movie_details(row, polarity)

def handle_random(name):
    print(Fore.BLUE + "\n🎲 Picking a random movie for you!", end="", flush=True)
    processing_animation()
    movie, polarity = random_recommendation()
    display_movie_details(movie, polarity)

def main():
    print(Fore.BLUE + "🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")
    name = input(Fore.CYAN + "What's your name? ").strip()
    print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")

    while True:
        print(Fore.YELLOW + "\nChoose Recommendation Type:")
        print(f"{Fore.CYAN}1. AI-Based Recommendation")
        print(f"{Fore.CYAN}2. Random Recommendation")
        choice = input(Fore.YELLOW + "Enter 1 or 2: ").strip()

        if choice == '1':
            handle_ai(name)
        elif choice == '2':
            handle_random(name)
        else:
            print(Fore.RED + "Invalid choice. Please enter 1 or 2.\n")
            continue

        again = input(Fore.YELLOW + "\nWould you like another recommendation? (yes/no): ").strip().lower()
        if again != 'yes':
            print(Fore.GREEN + f"\nThanks for using the Movie Assistant, {name}! 🎬🍿\n")
            break

if __name__ == "__main__":
    main()