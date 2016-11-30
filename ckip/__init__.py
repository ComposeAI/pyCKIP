# Copyright (c) 2016 Compose.ai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
import select
import socket
import xml.etree.cElementTree as ET


DEFAULT_SERVER_ADDR = ('140.109.19.104', 1501)

_BUFSIZE = 8192


class CKIP(object):
    def __init__(self, username, password, server_addr=None):
        self._username = username
        self._password = password
        self._server_addr = server_addr or DEFAULT_SERVER_ADDR

        if username is None or password is None:
            raise RuntimeError('login credential must be set')

    def Segment(self, text):
        """Segment text with CKIP API.

        Args:
            text: Chinese in utf-8 or unicode

        Return:
            a list of list of tuples, where each list item represents a
            sentence and each tuple having the format of (term, POS).
        """
        if not isinstance(text, unicode):
            text = unicode(text, 'utf8')

        root = ET.Element('wordsegmentation', version='1.0')
        ET.SubElement(root, 'option', version='1.0')
        ET.SubElement(root, 'authentication',
                      username=self._username, password=self._password)
        text_node = ET.SubElement(root, 'text')
        text_node.text = text

        request = ET.tostring(root, encoding='cp950')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(self._server_addr)
        s.send(request)
        response = s.recv(len(text) * 10 + _BUFSIZE)

        response = response.decode('cp950').encode('utf8')
        root = ET.fromstring(response)

        status = root.find('./processstatus')
        if status.attrib['code'] == '3':
            raise RuntimeError(status.text)
        elif status.attrib['code'] != '0':
            raise RuntimeError('unknown error: code %s: %s' %
                               (status.attrib['code'], status.text))

        result = []
        for sentence in root.findall('./result/sentence'):
            sen = []
            for pair in sentence.text.split(u'\u3000'):
                if pair:
                    m = re.match(r'(.*)\((.*)\)', pair)
                    term, pos = m.groups()
                    sen.append((term, str(pos)))
            result.append(sen)

        return result
