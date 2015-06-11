import unittest
from forward_viterbi import ForwardViterbi
from backward_viterbi import BackwardViterbi


class TestSeaquenceFunction(unittest.TestCase):

    def test_wc(self):
        modelName = 'data/unigram_model'
        fileName = 'data/04-input.txt'
        fviterbi = ForwardViterbi(modelName, fileName)
        fviterbi.forward_process()

        print('=' * 30)

        bviterbi = BackwardViterbi(modelName, fileName)
        bviterbi.backward_process()

if __name__ == '__main__':
    unittest.main()
