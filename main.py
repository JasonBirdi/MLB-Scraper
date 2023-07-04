from scraper.twitter_scraper import TwitterScraper
from scraper.image_processor import ImageProcessor
from scraper.data_analyzer import DataAnalyzer
from credentials import consumer_key, consumer_secret, access_token, access_token_secret

# Initialize your classes
twitter_scraper = TwitterScraper(consumer_key, consumer_secret, access_token, access_token_secret)
image_processor = ImageProcessor()
data_analyzer = DataAnalyzer()

# List of users you want to scrape
user_list = ['hollywood_picks', 'MJCLocks', 'TheProfessor305', 'CodyBrownBets', 'TheParlayPlug']

# Loop over each user
for user in user_list:
    print(f"Processing user {user}...")

    # Get user's tweets
    tweets = twitter_scraper.get_tweets(user)

    # Loop over each tweet
    for tweet in tweets:
        # If tweet has an image
        if twitter_scraper.has_image(tweet):
            # Get the image
            image = twitter_scraper.get_image(tweet)
            
            # Process the image to extract text
            text = image_processor.extract_text(image)

            # Analyze the extracted text
            data_analyzer.analyze(text)

# After all analysis is done, compile the bets
bets = data_analyzer.compile_bets()
print(f"Compiled Bets: {bets}")
