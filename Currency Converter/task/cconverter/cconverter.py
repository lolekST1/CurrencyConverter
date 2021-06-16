import json
import requests

cache_dir = {}

end = False


def currency_check(c):
    global cache_dir
    try:
        with open("cache.json", "r") as cache:
            cache_dir = json.load(cache)
            check = cache_dir[c]
    except:
        with open("cache.json", "w") as cache:
            d = {}
            d[c] = {}
            json.dump(d, cache)
    with open("cache.json", "r") as cache:
        cache_dir = json.load(cache)

    r = requests.get(f"http://www.floatrates.com/daily/{c}.json")
    r_dir = json.loads(r.text)
    if c != 'usd':
        cache_dir[c]['usd'] = r_dir['usd']['rate']
    if c != 'eur':
        cache_dir[c]['eur'] = r_dir['eur']['rate']
    with open("cache.json", "w") as cache:
        json.dump(cache_dir, cache)


def change(c):
    global cache_dir, end
    with open("cache.json", "r") as cache:
        cache_dir = json.load(cache)
    to = input().lower()
    if not to:
        end = True
        return
    how_much = float(input())
    print("Checking the cache...")
    try:
        rate = cache_dir[c][to]
        print("Oh! It is in the cache!")
    except:
        r = requests.get(f"http://www.floatrates.com/daily/{c}.json")
        output = json.loads(r.text)
        rate = output[to]['rate']
        print('Sorry, but it is not in the cache!')
    # print(rate)
    print(f"You received {round(rate * how_much, 2)} {to.upper()}")
    cache_dir[c][to] = rate
    with open("cache.json", "w") as cache:
        json.dump(cache_dir, cache)


c = input().lower()
currency_check(c)
while not end:
    change(c)
