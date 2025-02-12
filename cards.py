# https://chatgpt.com/share/67ad075d-26c0-8013-8b92-09632147acb7

# Define the suits and their Unicode ranges
suits = {
    "Hearts": (0x1F0A1, 0x1F0AD),   # U+1F0A1 to U+1F0AD
    "Diamonds": (0x1F0B1, 0x1F0BD), # U+1F0B1 to U+1F0BD
    "Clubs": (0x1F0C1, 0x1F0CD),    # U+1F0C1 to U+1F0CD
    "Spades": (0x1F0D1, 0x1F0DD)    # U+1F0D1 to U+1F0DD
}

# Define ranks as range
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Loop through each suit and rank, printing the cards
for suit, (start_code, end_code) in suits.items():
    print(f"\n{ suit } Cards:")
    for i, rank in enumerate(ranks):
        card_code = chr(start_code + i)
        print(f"{rank} of {suit}: {card_code}")
