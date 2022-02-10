import random

import googletrans
from googletrans import Translator


def jumble_text(text, iters):
  trans = Translator()
  prev_lang = trans.detect(text).lang
  for i in range(iters):
    lang = random.choice(list(googletrans.LANGUAGES.keys()))
    if random.choice([True, False, False, False, False]):
      # This will use the trick to corrupt text by first translating
      # to arabic and then changing the source language to malay,
      # then translating the text to a random language. This feature
      # is disabled for the time being.
      backup_text = text
      try:
        print("iteration {} : translating mysteriously".format(i + 1))
        text = trans.translate(text, dest="ar").text
        text = trans.translate(text, src="ms", dest=lang).text
      except TypeError:
        print("translation failed")
        text = backup_text
    else:
      print(
        "iteration {} : translating {} to {}".format(
          i + 1, 
          googletrans.LANGUAGES[prev_lang], 
          googletrans.LANGUAGES[lang]
        )
      )
      text = trans.translate(text, dest=lang).text
    prev_lang = lang
  return trans.translate(text).text


def main(*args, **kwargs):
  text = \
    """
    The 1920's were characterized by a new revival in culture and 
    optimism, however the time period also allowed for the buildup 
    to the Great Depression by the 1930s. As a new credit system was 
    formed, many common people began using credit for the purchase of
    expensive items such as houses, however since the credit was not 
    backed by gold, this caused great debts. Additionally, a dust 
    bowl in the midwest caused shortage in food supply and left many 
    starving and our economy was falling apart. Also, a protective 
    tariff called the Smoot Hawley tariff raised import duties into 
    the United States, with retaliation by other countries being their
    own increase in import duties, causing a dislocation of trade. 
    President Herbert Hoover's reluctance to involve the federal 
    government into the matters of the economic depression caused a 
    loss in his popularity and set up Franklin D. Roosevelt to win 
    the 1932 election, where he implemented the New Deal policy to 
    help America out of the depression. Despite its shortcomings, 
    FDR's first New Deal mostly had an effective impact on recovering 
    the United States from the Great Depression and restructuring the 
    government due to its massive focus on reducing unemployment, 
    restricting businesses and improving worker rights, and expanding 
    the role of the government to serve as a better foundation for the 
    country.
    """
  text = jumble_text(text, 20)
  with open("text.txt", "w") as file:
    file.write(text)


if __name__ == "__main__":
  main()
