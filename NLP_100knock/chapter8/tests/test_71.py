import unittest


class StopWordTest(unittest.TestCase):

    def setUp(self):
        self.content_list = ['+1',
                             'this',
                             'illuminating',
                             'documentary',
                             'transcends',
                             'our',
                             'preconceived',
                             'vision',
                             'of',
                             'the',
                             'holy',
                             'land',
                             'and',
                             'its',
                             'inhabitants',
                             ',',
                             'revealing',
                             'the',
                             'human',
                             'complexities',
                             'beneath',
                             '.']
        self.stop_word_list = ['+1',
                               'this',
                               'of',
                               'the',
                               'and',
                               'its',
                               ',',
                               '.']
        self.sentence_list = ['illuminating',
                              'documentary',
                              'transcends',
                              'our',
                              'preconceived',
                              'vision',
                              'holy',
                              'land',
                              'inhabitants',
                              'human',
                              'complexities',
                              'beneath',
                              'revealing']

    def test_stop_word(self):
        stop_list = []
        word_list = []
        for word in self.content_list:
            if word in self.stop_word_list:
                stop_list.append(word)
            else:
                word_list.append(word)

        self.assertTrue(stop_list, self.stop_word_list)
        self.assertTrue(word_list, self.sentence_list)

if __name__ == '__main__':
    unittest.main()
