def signal(candle):
    o = candle["open"]
    c = candle["close"]
    h = candle["high"]
    l = candle["low"]

    body = abs(c - o)
    upper_wick = h - max(o, c)
    lower_wick = min(o, c) - l

    if lower_wick > body and c > o:
        return "BUY"

    if upper_wick > body and c < o:
        return "SELL"

    return None


# TEST
candle = {
    "open": 100,
    "close": 95,
    "high": 110,
    "low": 90
}

print(signal(candle))
