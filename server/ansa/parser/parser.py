
import arrow

from superdesk.io.feed_parsers.newsml_2_0 import NewsMLTwoFeedParser
from superdesk.etree import get_word_count


class ANSAParser(NewsMLTwoFeedParser):

    cat_map = {
        'ACE': 'Entertainment',
        'CLJ': 'Chronicle',
        'DIS': 'Chronicle',
        'FIN': 'Business',
        'EDU': 'Chronicle',
        'ENV': 'Chronicle',
        'HTH': 'Chronicle',
        'HUM': 'Chronicle',
        'LAB': 'Chronicle',
        'LIF': 'Entertainment',
        'REL': 'Chronicle',
        'SCI': 'Chronicle',
        'SOI': 'Chronicle',
        'WAR': 'Chronicle',
        'WEA': 'Chronicle',
        'SPR': 'Sport',
        'SPO': 'Sport',
        'POL': 'Politics',
        'CRO': 'Chronicle',
        'SPE': 'Entertainment',
        'EST': 'WORLD',
        'ECO': 'Business',
        'PEC': 'Business',
    }

    def parse_content_meta(self, tree, item):
        super().parse_content_meta(tree, item)
        meta = tree.find(self.qname('contentMeta'))

        headlines = meta.findall(self.qname('headline'))
        for headline in headlines:
            if headline.get('role') == 'hld:subHeadline':
                item['abstract'] = headline.text

        subjects = meta.findall(self.qname('subject'))
        for subject in subjects:
            if subject.get('type') == 'cptype:cat':
                name = self.cat_map.get(subject.get('literal'))
                if name:
                    item['anpa_category'] = [{'name': name, 'qcode': name.lower()}]

    def parse_item(self, tree):
        item = super().parse_item(tree)
        if item.get('word_count') == 0 and item.get('type') == 'text':
            item['word_count'] = get_word_count(item.get('body_html', '<p></p>'))
        return item

    def datetime(self, string):
        return arrow.get(string).datetime
