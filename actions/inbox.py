"""
actions/inbox.py

Cross-platform SMS fetching utility.
On Android, uses PyJNIus to fetch SMS from inbox.
On non-Android (Linux, Windows, macOS), returns empty lists.
"""

def _get_android_resolver():
    """
    Initialize and return Android resolver and SMS URI.
    Raises Exception if not on Android.
    """
    from jnius import autoclass

    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Uri = autoclass('android.net.Uri')

    activity = PythonActivity.mActivity
    resolver = activity.getContentResolver()
    sms_uri = Uri.parse("content://sms/inbox")

    return resolver, sms_uri


def fetch_all_sms():
    """
    Fetch all SMS from inbox.
    Returns a list of dicts: {sender, body, timestamp}.
    Returns empty list if not on Android.
    """
    try:
        resolver, sms_uri = _get_android_resolver()
    except Exception:
        return []

    messages = []

    cursor = resolver.query(sms_uri, None, None, None, "date DESC")
    if cursor and cursor.moveToFirst():
        while True:
            body = cursor.getString(cursor.getColumnIndex("body"))
            sender = cursor.getString(cursor.getColumnIndex("address"))
            timestamp = cursor.getLong(cursor.getColumnIndex("date"))

            messages.append({
                "sender": sender,
                "body": body,
                "timestamp": timestamp
            })

            if not cursor.moveToNext():
                break

    if cursor:
        cursor.close()

    return messages


def fetch_new_sms(last_timestamp):
    """
    Fetch SMS that arrived after last_timestamp.
    last_timestamp: int, milliseconds since epoch.
    Returns a list of dicts. Empty list if not on Android.
    """
    all_messages = fetch_all_sms()
    new_messages = [m for m in all_messages if m["timestamp"] > last_timestamp]
    return new_messages


def get_latest_sms_timestamp():
    """
    Returns the timestamp of the newest SMS in inbox.
    Returns None if inbox is empty or not on Android.
    """
    try:
        resolver, sms_uri = _get_android_resolver()
    except Exception:
        return None

    cursor = resolver.query(sms_uri, None, None, None, "date DESC")
    latest = None

    if cursor and cursor.moveToFirst():
        latest = cursor.getLong(cursor.getColumnIndex("date"))

    if cursor:
        cursor.close()

    return latest
