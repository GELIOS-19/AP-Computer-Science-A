from collections import defaultdict
import string
import json

from bs4 import Tag

from spellmic.spellmic.apps.words.app.utils.formats import Formats
from spellmic.spellmic.apps.words.app.utils.utils import BeautifulSoupUtils


class WordSense:
  """
    Single sense or meaning of a word

    Attributes:
        _word_soup : BeautifulSoup
            the soup object of all the code
        _word_sense_soup : BeautifulSoup
            the soup object of the code relating to the word sense

    Properties:
        spelling : str
            the spelling of the word sense
        func : str
            the function of the word sense
        meanings : Dict
            the meanings of the word sense
        language : str
            the language of the word sense
        examples : Dict
            the examples of the word sense

    Helpers:
        _SpellingHelper : cls
            the helper class for the spelling property
        _FunctionHelper : cls
            the helper class for the function property
        _MeaningsHelper : cls
            the helper class for the meanings property
        _LanguageHelper : cls
            the helper class for the language property
        _ExamplesHelper : cls
            the helper class for the examples property
    """

  class _SpellingHelper:
    """
        The helper class for the spelling property

        Attributes:
            _word_sense : WordSense
                the instance of the word sense object, the parent class

        Properties:
            spelling : str
                the spelling property, export of this helper class
        """

    def __init__(self, word_sense):
      self._word_sense = word_sense

    @property
    def spelling(self):
      """Export property of this class"""
      spelling_text_tag = self._word_sense._word_sense_soup.find(
          attrs={"class": "hword"})
      return Formats.SpellingFormats.spelling_format(
          spelling_text_tag.text) if spelling_text_tag is not None else ""

  class _FunctionHelper:
    """
        The helper class for the function property

        Attributes:
            _word_sense : WordSense
                the instance of the word sense object, the parent class

        Properties:
            func : str
                the function property, export of this helper class
        """

    def __init__(self, word_sense):
      self._word_sense = word_sense

    @property
    def func(self):
      """Export property of this helper class"""
      func_text_tag = self._word_sense._word_sense_soup.find(
          attrs={"class": "fl"})
      return Formats.FunctionFormats.func_format(
          func_text_tag.text) if func_text_tag is not None else ""

  class _MeaningsHelper:
    """
        The helper class for the meanings property

        Attributes:
            _word_sense : WordSense
                the instance of the word sense object, the parent class

        Properties:
            meanings : Dict
                the meanings property, export of this helper class

        Helpers:
            _GetMeaningTagAndCrossLinkTagHelper : static cls
                the helper class for getting the meaning tag and the cross link tag
            _DivideMeaningTagHelper : static cls
                the helper class for dividing the meaning tag
            _GetMeaningTextAndCrossLinkTextHelper : static cls
                the helper class for getting meaning texts and cross link texts
            _GetMeaningTreesAndCrossLinkTreesHelper : static cls
                the helper class for getting meaning trees and cross link trees
        """

    def __init__(self, word_sense):
      self._word_sense = word_sense

    @property
    def meanings(self):
      """Export of this helper class"""
      meaning_tag = self._GetMeaningTagAndCrossLinkTagHelper.get_meaning_tag(
          self._word_sense)
      cross_link_tag = self._GetMeaningTagAndCrossLinkTagHelper.get_cross_link_tag(
          self._word_sense)

      collegiate_source = (
          "words-entry" in meaning_tag["id"] and
          cross_link_tag is None) if meaning_tag.has_attr("id") else False
      learners_source = ("learners-def" in meaning_tag["class"]
                        ) if meaning_tag.has_attr("class") else False
      elementary_source = ("elementary-entry" in meaning_tag["id"]
                          ) if meaning_tag.has_attr("id") else False
      medical_source = ("medical-entry" in meaning_tag["id"]
                       ) if meaning_tag.has_attr("id") else False
      legal_source = ("legal-entry" in meaning_tag["id"]
                     ) if meaning_tag.has_attr("id") else False
      cross_link_source = ("words-entry" in meaning_tag["id"] and cross_link_tag
                           is not None) if meaning_tag.has_attr("id") else False

      meanings = {
          "Main":
              self._GetMeaningTreesAndCrossLinkTreesHelper.get_meaning_tree(
                  self._DivideMeaningTagHelper,
                  self._GetMeaningTextAndCrossLinkTextHelper, meaning_tag)
              if collegiate_source else None,
          "Learners":
              self._GetMeaningTreesAndCrossLinkTreesHelper.get_meaning_tree(
                  self._DivideMeaningTagHelper,
                  self._GetMeaningTextAndCrossLinkTextHelper, meaning_tag)
              if learners_source else None,
          "Elementary":
              self._GetMeaningTreesAndCrossLinkTreesHelper.get_meaning_tree(
                  self._DivideMeaningTagHelper,
                  self._GetMeaningTextAndCrossLinkTextHelper, meaning_tag)
              if elementary_source else None,
          "Medical":
              self._GetMeaningTreesAndCrossLinkTreesHelper.get_meaning_tree(
                  self._DivideMeaningTagHelper,
                  self._GetMeaningTextAndCrossLinkTextHelper, meaning_tag)
              if medical_source else None,
          "Legal":
              self._GetMeaningTreesAndCrossLinkTreesHelper.get_meaning_tree(
                  self._DivideMeaningTagHelper,
                  self._GetMeaningTextAndCrossLinkTextHelper, meaning_tag)
              if legal_source else None,
          "Cross Link":
              self._GetMeaningTreesAndCrossLinkTreesHelper.get_meaning_tree(
                  self._DivideMeaningTagHelper,
                  self._GetMeaningTextAndCrossLinkTextHelper, cross_link_tag)
              if cross_link_source else None
      }

      return meanings

    class _GetMeaningTagAndCrossLinkTagHelper:
      """The helper class for getting the meaning tag and cross link tag"""

      @staticmethod
      def get_meaning_tag(word_sense):

        def tag_filter(tag):
          tag_classes = []
          tag_id = ""
          try:
            tag_classes = tag["class"]
          except KeyError:
            pass
          try:
            tag_id = tag["id"]
          except KeyError:
            pass
          return ("words-entry" in tag_id or "elementary-entry" in tag_id or
                  "learners-def" in tag_classes or "medical-entry" in tag_id or
                  "legal-entry" in tag_id)

        meaning_tags = [
            tag for tag in filter(tag_filter,
                                  word_sense._word_sense_soup.find_all())
        ]
        return meaning_tags[0] if len(meaning_tags) > 0 else Tag(name="None")

      @staticmethod
      def get_cross_link_tag(word_sense):

        def tag_filter(tag):
          tag_classes = []
          tag_id = ""
          try:
            tag_classes = tag["class"]
          except KeyError:
            pass
          try:
            tag_id = tag["id"]
          except KeyError:
            pass
          return ("words-entry" in tag_id or "elementary-entry" in tag_id or
                  "learners-def" in tag_classes or "medical-entry" in tag_id or
                  "legal-entry" in tag_id)

        meaning_tags = [
            tag for tag in filter(tag_filter,
                                  word_sense._word_sense_soup.find_all())
        ]
        meaning_tag = meaning_tags[0] if len(meaning_tags) > 0 else Tag(
            name="None")
        return meaning_tag.find(attrs={"class": "cxl-ref"})

    class _DivideMeaningTagHelper:
      """The helper class for dividing the meaning tag"""

      @staticmethod
      def divide_meaning_tag_by_category_tags(meaning_tag):
        category = meaning_tag.find_all(attrs={"class": "vg"})
        for i, category_tag in enumerate(category):
          category_text_tag = category_tag.find(attrs={"class": "vd"})
          phrase_category_text_tag = category_tag.find_previous_sibling(
              attrs={"class": "drp"})
          category_placeholder = Formats.MeaningFormats.meaning_category_format(
              str(i + 1))
          category = category_placeholder
          if category_text_tag is not None:
            category = Formats.MeaningFormats.meaning_category_format(
                category_text_tag.text)
          elif phrase_category_text_tag is not None:
            category = Formats.MeaningFormats.meaning_category_format(
                phrase_category_text_tag.text)
          yield category_tag, category

      @staticmethod
      def divide_category_tag_by_number_tags(category_tag):
        number_tags = category_tag.find_all(attrs={"class": "sb"})
        for j, number_tag in enumerate(number_tags):
          number_text_tag = number_tag.find(attrs={"class": "num"})
          number_placeholder = Formats.MeaningFormats.meaning_number_format(
              str(j + 1))
          number = Formats.MeaningFormats.meaning_number_format(
              number_text_tag.text
          ) if number_text_tag is not None else number_placeholder
          yield number_tag, number

      @staticmethod
      def divide_number_tag_by_letter_tags(number_tag):
        letter_tags = number_tag.find_all(recursive=False)
        for k, letter_tag in enumerate(letter_tags):
          letter_text_tag = letter_tag.find(attrs={"class": "letter"})
          letter_placeholder = Formats.MeaningFormats.meaning_letter_format(
              string.ascii_uppercase[k])
          letter = Formats.MeaningFormats.meaning_letter_format(
              letter_text_tag.text
          ) if letter_text_tag is not None else letter_placeholder
          yield letter_tag, letter

      @staticmethod
      def divide_letter_tag_by_sub_number_tags(letter_tag):
        sub_number_tags = letter_tag.find_all(attrs={"class": "sense"})
        for l, sub_number_tag in enumerate(sub_number_tags):
          sub_number_text_tag = sub_number_tag.find(attrs={"class": "sub-num"})
          sub_number_placeholder = Formats.MeaningFormats.meaning_sub_number_format(
              str(l + 1))
          sub_number = Formats.MeaningFormats.meaning_sub_number_format(
              sub_number_text_tag.text
          ) if sub_number_text_tag is not None else sub_number_placeholder
          yield sub_number_tag, sub_number

    class _GetMeaningTextAndCrossLinkTextHelper:
      """The helper class for getting meaning texts and cross link texts"""

      @staticmethod
      def get_meaning_text(tag):
        meaning_text_tag = tag.find(attrs={"class": "dtText"})
        note_text_tag = tag.find(attrs={"class": "unText"})
        meaning_placeholder = "Meaning"
        meaning = meaning_placeholder
        if meaning_text_tag is not None:
          meaning = meaning_text_tag.text
        elif note_text_tag is not None:
          meaning = note_text_tag.text
        return Formats.MeaningFormats.meaning_and_cross_link_format(meaning)

      @staticmethod
      def get_cross_link_text(tag):
        cross_link_placeholder = "Cross Link"
        cross_link = tag.text if tag is not None else cross_link_placeholder
        return Formats.MeaningFormats.meaning_and_cross_link_format(cross_link)

    class _GetMeaningTreesAndCrossLinkTreesHelper:
      """The helper class for getting the meaning trees and cross link trees"""

      @staticmethod
      def get_meaning_tree(divide_tag_helper,
                           get_meaning_text_and_cross_link_text_helper, tag):
        meaning_tree = defaultdict(lambda: defaultdict(lambda: defaultdict(
            lambda: defaultdict(lambda: defaultdict(lambda: "")))))
        categories = divide_tag_helper.divide_meaning_tag_by_category_tags(tag)
        for category_tag, category in categories:
          numbers = divide_tag_helper.divide_category_tag_by_number_tags(
              category_tag)
          for number_tag, number in numbers:
            letters = divide_tag_helper.divide_number_tag_by_letter_tags(
                number_tag)
            for letter_tag, letter in letters:
              sub_numbers = divide_tag_helper.divide_letter_tag_by_sub_number_tags(
                  letter_tag)
              for sub_number_tag, sub_number in sub_numbers:
                meaning = get_meaning_text_and_cross_link_text_helper.get_meaning_text(
                    sub_number_tag)
                meaning_tree[category][number][letter][sub_number][
                    "Meaning"] = meaning
        return eval(json.dumps(meaning_tree))

      @staticmethod
      def get_cross_link_tree(divide_tag_helper,
                              get_meaning_text_and_cross_link_text_helper, tag):
        cross_link_tree = defaultdict(lambda: defaultdict(lambda: defaultdict(
            lambda: defaultdict(lambda: defaultdict(lambda: "")))))
        cross_link = get_meaning_text_and_cross_link_text_helper.get_cross_link_text(
            tag)
        cross_link_tree["Category: 1"]["Number: 1"]["Letter: A"][
            "Sub Number: 1"]["Cross Link"] = cross_link
        return eval(json.dumps(cross_link_tree))

  class _LanguageHelper:
    """
        The helper class for the language property

        Attributes:
            _word_sense : WordSense
                the instance of the word sense object, the parent class

        Properties:
            language : str
                the language property, export of this helper class
        """

    def __init__(self, word_sense):
      self._word_sense = word_sense

    @property
    def language(self):
      """Export of this helper class"""
      etymology = self._get_etymology(self._word_sense)
      return self._get_language(etymology)

    @staticmethod
    def _get_etymology(word_sense):
      etymology_tag = word_sense._word_soup.find(
          attrs={"id": "etymology-anchor"})
      if etymology_tag is not None:
        etymology_func_text_tags = etymology_tag.find_all(
            attrs={"class": "function-label"})
        etymology_text_tag = None
        if len(etymology_func_text_tags) > 0:
          for etymology_func_text_tag in etymology_func_text_tags:
            etymology_func = Formats.FunctionFormats.compare_func_format(
                etymology_func_text_tag.text)
            func = Formats.FunctionFormats.compare_func_format(word_sense.func)
            if func in etymology_func:
              etymology_text_tag = etymology_func_text_tag.find_next_sibling()
        else:
          etymology_text_tag = etymology_tag.find(attrs={"class": "et"})
        etymology = "".join(
            BeautifulSoupUtils.get_near_texts(
                etymology_text_tag)) if etymology_text_tag is not None else ""
        return Formats.LanguageFormats.compare_etymology_format(etymology)
      else:
        return ""

    @staticmethod
    def _get_language(etymology):

      def capital_word(word):
        return word[0].isupper() if len(word) > 0 else False

      language = ""
      try:
        etymology = etymology.split("\u0020")
        etymology_iterator = iter(etymology)
        while True:
          text = next(etymology_iterator)
          if capital_word(text) and len(text) > 1:
            language += text + "\u0020"
            next_text = next(etymology_iterator)
            while capital_word(next_text):
              language += next_text + "\u0020"
              next_text = next(etymology_iterator)
            return Formats.LanguageFormats.language_format(language)
      except StopIteration:
        return None

  class _ExamplesHelper:
    """
         The helper class for the examples property

         Attributes:
             _word_sense : WordSense
                 the instance of the word sense object, the parent class

         Properties:
             examples : Dict
                 the examples property, export of this helper class

        Helpers:
            _GetExampleTextTagAndAdditionalExamplesTextTagHelper : static cls
                The helper class for getting example text tag and additional examples text tag
            _GetExamplesAndAdditionalExamplesHelper : static cls
                The helper class for getting examples and additional examples
        """

    def __init__(self, word_sense):
      self._word_sense = word_sense

    @property
    def examples(self):
      """Export of this helper class"""
      example_text_tag = self._GetExampleTextTagAndAdditionalExamplesTextTagHelper.get_examples_text_tag(
          self._word_sense)
      additional_examples_text_tag = self._GetExampleTextTagAndAdditionalExamplesTextTagHelper.get_additional_examples_text_tag(
          self._word_sense)
      return {
          "Examples":
              self._GetExamplesAndAdditionalExamplesHelper.get_examples(
                  example_text_tag),
          "Additional Examples":
              self._GetExamplesAndAdditionalExamplesHelper
              .get_additional_examples(additional_examples_text_tag)
      }

    class _GetExampleTextTagAndAdditionalExamplesTextTagHelper:
      """The helper class for getting example text tag and additional examples text tag"""

      @staticmethod
      def get_examples_text_tag(word_sense):
        this_examples_text_tag = None
        try:
          examples_text_tags = word_sense._word_soup.find(attrs={
              "class": "in-examples"
          }).find_all()
        except AttributeError:
          return None
        for examples_text_tag in examples_text_tags:
          if "function-label" in examples_text_tag["class"]:
            examples_func = Formats.FunctionFormats.compare_func_format(
                examples_text_tag.text)
            func = Formats.FunctionFormats.compare_func_format(word_sense.func)
            if examples_func == func:
              this_examples_text_tag = examples_text_tag
        if this_examples_text_tag is None:
          this_examples_text_tag = examples_text_tags[0]
        return this_examples_text_tag

      @staticmethod
      def get_additional_examples_text_tag(word_sense):
        additional_examples_url = f"https://www.wordhippo.com/what-is/examples-with-the-word/{word_sense.spelling}.html"
        additional_examples_soup = BeautifulSoupUtils.get_soup_from_request(
            additional_examples_url)
        return additional_examples_soup.find(attrs={"id": "mainsentencestable"})

    class _GetExamplesAndAdditionalExamplesHelper:
      """The helper class for getting examples and additional examples"""

      @staticmethod
      def get_examples(example_text_tag):
        examples = []
        if example_text_tag is not None:
          if "function-label" in example_text_tag["class"]:
            next_example_text_tag = example_text_tag.find_next_sibling()
          else:
            next_example_text_tag = example_text_tag
          while next_example_text_tag is not None and "ex-sent" in next_example_text_tag.attrs[
              "class"]:
            example = Formats.ExampleFormats.example_format(
                next_example_text_tag.text)
            examples.append(example)
            next_example_text_tag = next_example_text_tag.find_next_sibling()
          return examples

      @staticmethod
      def get_additional_examples(additional_examples_text_tag):
        additional_examples = []
        if additional_examples_text_tag is not None:
          for additional_example_text_tag in additional_examples_text_tag.find_all(
              recursive=False):
            additional_example = Formats.ExampleFormats.additional_example_format(
                additional_example_text_tag.text)
            additional_examples.append(additional_example)
        return additional_examples[0:5] if len(
            additional_examples) > 0 else None

  def __init__(self, word_soup, word_sense_soup):
    self._word_soup = word_soup
    self._word_sense_soup = word_sense_soup

  @property
  def spelling(self):
    """The spelling of the word sense"""
    spelling_helper = self._SpellingHelper(self)
    return spelling_helper.spelling

  @property
  def func(self):
    """The function of the word sense"""
    func_helper = self._FunctionHelper(self)
    return func_helper.func

  @property
  def meanings(self):
    """The meanings of the word sense"""
    meanings_helper = self._MeaningsHelper(self)
    return meanings_helper.meanings

  @property
  def language(self):
    """The language of the word sense"""
    language_helper = self._LanguageHelper(self)
    return language_helper.language

  @property
  def __dict__(self):
    return {
        "Spelling": self.spelling,
        "Function": self.func,
        "Meanings": self.meanings,
        "Language": self.language,
        "Examples": self.examples
    }     
