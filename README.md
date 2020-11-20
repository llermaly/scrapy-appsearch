Description
===========
Scrapy pipeline which allows you to store scrapy items in  AppSearch.
Using as base the [Elastic Search pipeline](https://github.com/jayzeng/scrapy-elasticsearch).

Install
=======

```
pip install ScrapyAppSearch
```

Usage (Configure settings.py:)
------------------------------
```
   ITEM_PIPELINES = {
       'scrapyappsearch.scrapyappsearch.AppSearchPipeline': 500
   }

   APP_SEARCH_URL = 'https://<...>.ent-search.us-central1.gcp.cloud.es.io'
   APP_SEARCH_KEY = 'private-xxxxxxxxxxxxxxxxx'
   APP_SEARCH_ENGINE = 'my_engine'
```


Available parameters (in settings.py)
-------------------------------------
```
   APP_SEARCH_URL - Url of your App search instance
   APP_SEARCH_KEY - API Key, starting with private-
   APP_SEARCH_ENGINE = Name of the search engine
```

Dependencies
============
See requirements.txt

Changelog
=========
* 0.1.0: Initial release

Coming Up
=========
* More authentication methods

Issues
=============
If you find any bugs or have any questions, please report them to "issues" (https://github.com/llermaly/scrapy-appsearch/issues)

Contributors
=============
* Gustavo Llermaly (Maintainer) (https://github.com/llermaly)


License
=======
Copyright 2020 Gustavo Llermaly

Expanded on the work by Julien Duponchelle and Michael Malocha

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.