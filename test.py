#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import ckip


class CKIPUnittest(unittest.TestCase):
    def test_Segment(self):
        c = ckip.CKIP('iis', 'iis')
        res = c.Segment('台新金控12月3日將召開股東臨時會進行董監改選。'
                        '這是一個中文句子。')
        self.assertEquals(len(res), 2)

    def test_Invalid_Credential(self):
        c = ckip.CKIP('abc', '123')
        with self.assertRaisesRegexp(RuntimeError, 'Authentication failed'):
            res = c.Segment('台新金控12月3日將召開股東臨時會進行董監改選。'
                            '這是一個中文句子。')


if __name__ == '__main__':
    unittest.main()
