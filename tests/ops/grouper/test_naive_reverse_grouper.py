import unittest

from data_juicer.core.data import NestedDataset as Dataset
from data_juicer.ops.grouper.naive_reverse_grouper import NaiveReverseGrouper
from data_juicer.utils.unittest_utils import DataJuicerTestCaseBase


class NaiveReverseGrouperTest(DataJuicerTestCaseBase):

    def _run_helper(self, op, samples, target):
        dataset = Dataset.from_list(samples)
        new_dataset = op.run(dataset)

        for d, t in zip(new_dataset, target):
            self.assertEqual(d['text'], t['text'])

    def test_one_batched_sample(self):

        source = [
            {
                'text':[
                    "Today is Sunday and it's a happy day!",
                    "Sur la plateforme MT4, plusieurs manières d'accéder à \n"
                    'ces fonctionnalités sont conçues simultanément.',
                    '欢迎来到阿里巴巴！'
                ]
            }
        ]

        target = [
            {
                'text': "Today is Sunday and it's a happy day!"
            },
            {
                'text':
                "Sur la plateforme MT4, plusieurs manières d'accéder à \n"
                'ces fonctionnalités sont conçues simultanément.'
            },
            {
                'text': '欢迎来到阿里巴巴！'
            },
        ]

        op = NaiveReverseGrouper()
        self._run_helper(op, source, target)


    def test_two_batch_sample(self):

        source = [
            {
                'text':[
                    "Today is Sunday and it's a happy day!",
                    "Sur la plateforme MT4, plusieurs manières d'accéder à \n"
                    'ces fonctionnalités sont conçues simultanément.'
                ]
            },
            {
                'text':[
                    '欢迎来到阿里巴巴！'
                ]
            }
        ]

        target = [
            {
                'text': "Today is Sunday and it's a happy day!"
            },
            {
                'text':
                "Sur la plateforme MT4, plusieurs manières d'accéder à \n"
                'ces fonctionnalités sont conçues simultanément.'
            },
            {
                'text': '欢迎来到阿里巴巴！'
            },
        ]

        op = NaiveReverseGrouper()
        self._run_helper(op, source, target)

if __name__ == '__main__':
    unittest.main()