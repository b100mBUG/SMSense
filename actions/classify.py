
def classify_message(body: str) -> str:
    text = body.lower()
    if any(k in text for k in OTP_KEYWORDS):
        return "OTP"
    elif any(k in text for k in SPAM_KEYWORDS):
        return "SPAM"
    elif any(k in text for k in PROMOTTED_KEYWORDS):
        return "PROMOTED"
    elif any(k in text for k in FOCUSED_KEYWORDS):
        return "FOCUSED"
    else:
        return "UNKNOWN"


def group_messages(messages: list) -> dict:
    """
    Classify messages and return a dict of lists by category.
    """
    grouped = {
        "OTP": [],
        "SPAM": [],
        "PROMOTED": [],
        "FOCUSED": [],
        "UNKNOWN": []
    }

    for m in messages:
        label = classify_message(m["body"])
        grouped[label].append(m)

    return grouped


"""# Example usage in another module
if __name__ == "__main__":
    messages = fetch_new_sms()
    grouped = group_messages(messages)

    print("OTP:", len(grouped["OTP"]))
    print("Spam:", len(grouped["SPAM"]))
    print("Promoted:", len(grouped["PROMOTED"]))
    print("Focused:", len(grouped["FOCUSED"]))
    print("Unknown:", len(grouped["UNKNOWN"]))"""
