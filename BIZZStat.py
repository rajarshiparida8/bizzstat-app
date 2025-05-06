from GoogleNews import GoogleNews
import json
from datetime import datetime

# Convert datetime objects to ISO format strings
def convert_dates_to_string(articles):
    for article in articles:
        for key, value in article.items():
            if isinstance(value, datetime):
                article[key] = value.isoformat()
    return articles

# Fetch business news from India and the world
def fetch_news():
    googlenews = GoogleNews(lang='en', region='IN')

    # Search India Business news
    googlenews.search('India Business')
    india_results = googlenews.result()

    # Search World Business news
    googlenews.clear()
    googlenews.search('World Business')
    world_results = googlenews.result()

    # Combine and limit to 100 articles
    combined_results = india_results + world_results
    limited_results = combined_results[:100]

    # Convert any datetime objects to string format
    cleaned_results = convert_dates_to_string(limited_results)

    filename = 'news_output.json'
    with open(filename, 'w') as f:
        json.dump(cleaned_results, f, indent=2)

    return filename

# MAIN
if __name__ == "__main__":
    json_file = fetch_news()
    print(f"✅ News saved to {json_file}")