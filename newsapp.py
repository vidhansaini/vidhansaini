from newsapi import NewsApiClient
import pycountry
from assitant import speak

# Initialize the NewsApiClient with your API key
newsapi = NewsApiClient(api_key='5975c8377e2d4bf3aed1edef6deae45b')

# def get_country_code(country_name): Defines a function that takes the name of a country as input.
# try...except LookupError: Attempts to look up the country using pycountry. If the country name is invalid, it catches the LookupError and returns None.
# pycountry.countries.lookup(country_name).alpha_2: Retrieves the 2-letter country code (ISO 3166-1 alpha-2) for the given country name.

def get_country_code(country_name):
    try:
        return pycountry.countries.lookup(country_name).alpha_2
    except LookupError:
        return None
# def fetch_news(country_code, category): Defines a function to fetch news headlines based on the country code and category.
# newsapi.get_top_headlines(...): Calls the get_top_headlines method from the News API client, specifying the news category, language ('en' for English), and country code.
# return top_headlines['articles']: Returns the list of news articles fetched from the API.

def fetch_news(country_code, category):
    top_headlines = newsapi.get_top_headlines(
        category=category.lower(),
        language='en',
        country=country_code.lower()
    )
    return top_headlines['articles']

# def display_headlines(headlines): Defines a function to display the fetched news headlines.
# if headlines: Checks if there are any headlines to display.
# for article in headlines: Iterates through each news article.
# b = article['title'][::-1].index("-"): Finds the position of the last hyphen in the title, used to separate the source from the headline.
# if "news" in (article['title'][-b+1:]).lower(): Checks if the word "news" is in the source part of the title.
# print(...): Formats and prints the title and source of each article for better readability.

def display_headlines(headlines):
    if headlines:
        for article in headlines:
            b = article['title'][::-1].index("-")
            if "news" in (article['title'][-b+1:]).lower():
                print(f"{article['title'][-b+1:]}: {article['title'][:-b-2]}.")
                speak(f"{article['title'][-b+1:]}: {article['title'][:-b-2]}.")
            else:
                print(f"{article['title'][-b+1:]} News: {article['title'][:-b-2]}.")
                speak(f"{article['title'][-b+1:]} News: {article['title'][:-b-2]}.")
    else:
        print("Sorry, no articles found. Something went wrong!")
        speak("Sorry, no articles found. Something went wrong!")


# def main(): Defines the main function where the user interaction happens.
# while True: Starts an infinite loop to keep asking for user input until they choose to exit.
# input_country = input("Country: ").strip(): Prompts the user to enter a country name and strips any leading/trailing whitespace.
# country_code = get_country_code(input_country): Gets the country code for the entered country name.
# if not country_code: Checks if the entered country name is invalid.
# print(f"Invalid country name: {input_country}. Please try again."): Informs the user of the invalid country name.
# continue: Skips to the next iteration of the loop.
# category_options = {...}: Defines a dictionary of category options.
# print("Which category are you interested in?"): Prompts the user to choose a news category.
# for key, value in category_options.items(): Displays the category options.
# option = input("Enter the number corresponding to your category: ").strip(): Prompts the user to enter the number corresponding to their chosen category.
# category = category_options.get(option): Gets the category name from the dictionary based on the user's input.
# if not category: Checks if the user entered an invalid option.
# print(f"Invalid option: {option}. Please try again."): Informs the user of the invalid option.
# continue: Skips to the next iteration of the loop.
# headlines = fetch_news(country_code, category): Fetches the news headlines based on the country code and category.
# display_headlines(headlines): Displays the fetched headlines.
# repeat = input("Do you want to search again [Yes/No]? ").strip().lower(): Asks the user if they want to search again.
# if repeat != 'yes': Breaks the loop if the user does not want to search again.


def main():
    while True:
        input_country = input("Country: ").strip()
        country_code = get_country_code(input_country)
        
        if not country_code:
            print(f"Invalid country name: {input_country}. Please try again.")
            continue

        category_options = {
            "1": "Business",
            "2": "Entertainment",
            "3": "General",
            "4": "Health",
            "5": "Science",
            "6": "Technology"
        }

        print("Which category are you interested in?")
        for key, value in category_options.items():
            print(f"{key}. {value}")
        
        option = input("Enter the number corresponding to your category: ").strip()
        category = category_options.get(option)

        if not category:
            print(f"Invalid option: {option}. Please try again.")
            continue

        headlines = fetch_news(country_code, category)
        display_headlines(headlines)
        
        repeat = input("Do you want to search again [Yes/No]? ").strip().lower()
        if repeat != 'yes':
            break


# This ensures that the main() function runs only if the script is executed directly, not if it is imported as a module in another script.

if __name__ == "__main__":
    main()