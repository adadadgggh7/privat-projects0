# import random
import requests
# def generaot():
#     quotes = ["So many books, so little time",
#               "Two things are infinite the universe and human stupidity and I'm not sure about the universe.",
#               "A room without books is like a body without a soul.",
#               "To live is the rarest thing in the world. Most people exist, that is all",
#               ]
#     start = set()
#     while len(start) < len(quotes):
#         quote = random.choice(quotes)
#         if quote not in start:
#             start.add(quote)
#             yield quote
#     yield '\t no more quotes '
#
#
# ctr = generaot()
# for _ in range(5):
#     print(next(ctr))

# def getquote():
#     url = 'https://api.adviceslip.com/advice'
#     try:
#         respon = requests.get(url)
#         if respon.status_code == 200:
#             data = respon.json()
#             return data['slip']['advice']
#         else:
#             return 'cand get quote'
#     except Exception as error :
#         return f'{error}'
#
# for _ in range(5):
#     print(getquote())
#
