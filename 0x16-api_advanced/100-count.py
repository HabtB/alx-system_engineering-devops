#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    headers = {'User-Agent': 'MyBot/1.0'}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            posts = data['data']['children']

            for post in posts:
                title = post['data']['title'].lower()
                words = title.split()

                for word in words:
                    word = word.strip('.,!_')

                    if word in word_list:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1

            if 'after' in data['data']:
                after = data['data']['after']

                return count_words(subreddit, word_list, after=after, word_count=word_count)

            else:
                sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

                for word, count in sorted_counts:
                    print(f'{word}: {count}')

        except KeyError:
            return None

    else:
        return None
