pyCKIP - 中研院中文斷詞系統 Python API
======================================

提供 `中研院中文斷詞系統 <http://ckipsvr.iis.sinica.edu.tw/>`_ 的 Python API 綁定

安裝
----
.. code-block:: bash

    $ pip install ckip

使用方式
--------
.. code-block:: python

    from ckip import CKIP
    
    client = CKIP('username', 'password')

    # Return list of list of tuples, where each list item represents a sentence
    # and each tuple having the format of (term, POS).
    client.Segment('台新金控12月3日將召開股東臨時會進行董監改選。')

Contributing
------------
1. Fork it
2. Create your feature branch (``git checkout -b my-new-feature``)
3. Commit your changes (``git commit -am 'Add some feature'``)
4. Push to the branch (``git push origin my-new-feature``)
5. Create new Pull Request
