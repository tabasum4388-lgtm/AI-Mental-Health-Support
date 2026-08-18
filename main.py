from transformers import pipeline

print("AI Student Support System")
print("--------------------------")

# Load AI sentiment model
sentiment_analyzer = pipeline("sentiment-analysis")

name = input("Enter your name: ")
message = input("How are you feeling today? ")

# AI sentiment analysis
result = sentiment_analyzer(message)

sentiment = result[0]["label"]
confidence = result[0]["score"]

# Routing
message_lower = message.lower()

if any(word in message_lower for word in [
    "exam", "study", "marks", "assignment", "college"
]):
    route = "Academic Support"

elif any(word in message_lower for word in [
    "friend", "friends", "family", "alone", "lonely"
]):
    route = "Social Support"

elif any(word in message_lower for word in [
    "sad", "stress", "stressed", "anxious", "worried"
]):
    route = "Counselor Support"

else:
    route = "General Support"

print("\n--------------------------")
print("Hello,", name)
print("Your message:", message)
print("AI Sentiment:", sentiment)
print("Confidence:", round(confidence * 100, 2), "%")
print("Recommended Route:", route)