import random

def get_random_quote():
    # 1. Store quotes in a list
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "In the middle of every difficulty lies opportunity. - Albert Einstein"
    ]
    
    # 2. Use the random module to select a quote
    selected_quote = random.choice(quotes)
    
    # 3. Display the randomly selected quote
    print("\n--- Random Quote ---")
    print(selected_quote)
    print("---------------------\n")

# Run the function
if __name__ == "__main__":
    get_random_quote()
