"""Check the 'wikipedia philosophy law'."""


from contextlib import closing
from html.parser import HTMLParser
import time
from urllib.request import urlopen
from urllib.parse import quote, unquote
import re

import lxml.html


BASE_PATH = u'http://ru.wikipedia.org/wiki/'


class LinkSearchError(Exception):
    pass


def is_article_on_philosophy(html):
    categories = (re.search(r'\"wgCategories\":\[.*?\]', html)).group(0)
    if 'философ' in categories.lower():
        return True
    else:
        return False


def is_link_valid(attributes):
    href = attributes['href']
    if not href.startswith('/wiki/'):
        return False
    elif '(страница отсутствует)' in attributes['title']:
        return False
    else:
        return True


class MainTextLinksGetter(HTMLParser):
    GARBAGE_CLASSES = set([
        "infobox",
        "noprint",
        "image",
        "internal",
        "toc",
        "reference",
        "dablink",
        "thumbinner",
    ])

    GARBAGE_TAGS = set([
        "table",

    ])

    def __init__(self):
        HTMLParser.__init__(self)
        self.main_text = False
        self.brackets_depth = 0
        self.garbage_class_depth = 0
        self.links = []

    def check_garbage_depth(self, tag, attrs):
        if self.garbage_class_depth > 0:
            self.garbage_class_depth += 1
        else:
            tag_classes = set(attrs.get("class", "").split())

            if (self.GARBAGE_CLASSES.intersection(tag_classes) or
                    tag in self.GARBAGE_TAGS):
                self.garbage_class_depth = 1

        return self.garbage_class_depth

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.check_garbage_depth(tag, attrs_dict)
        try:
            if attrs_dict['id'] == 'mw-content-text':
                assert not self.main_text, "There can be only one main block."
                self.main_text = True
        except KeyError:
            pass
        if (tag == 'a' and self.brackets_depth == 0
                and self.garbage_class_depth == 0):
            try:
                if attrs_dict['class'] == 'mw-redirect':
                    if is_link_valid(attrs_dict):
                        self.links.append(attrs_dict['title'])
            except KeyError:
                pass

    def handle_endtag(self, tag):
        if self.garbage_class_depth > 0:
            self.garbage_class_depth -= 1

    def handle_data(self, data):
        for symbol in data:
            if symbol == u'(':
                self.brackets_depth += 1
            elif symbol == u')':
                    self.brackets_depth -= 1


def find_first_link(html):
    parser = MainTextLinksGetter()
    parser.feed(html)

    if not parser.links:
        raise LinkSearchError("Valid links not found")

    return str(parser.links[0])


def philosophy_chain(base_name, max_iters=100):
    visited = set([base_name])
    next_name = base_name
    print(base_name)
    for _ in range(max_iters):
        time.sleep(0.2)
        url = BASE_PATH + quote(next_name)
        print(url)
        with closing(urlopen(url)) as conn:
            html = (conn.read()).decode('utf-8')
        if is_article_on_philosophy(html) is True:
            return True
        try:
            next_name = find_first_link(html)
        except LinkSearchError:
            break

        name = unquote(str(next_name))
        print(name)
        if name in visited:
            return False
        visited.add(name)
    return False


def main():
    start = input()
    res = philosophy_chain(start)
    print("Philosophy found:" + str(res))


if __name__ == '__main__':
    main()
