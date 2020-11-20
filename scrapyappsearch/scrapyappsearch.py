# Copyright 2020 Gustavo Llermaly <gllermaly@gmail.com>
#
# Expanded from the work by Julien Duponchelle <julien@duponchelle.info> and Michael Malocha <michael@knockrentals.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""App Search Pipeline for scrappy expanded with support for multiple items"""

from elastic_enterprise_search import AppSearch

import logging

class InvalidSettingsException(Exception):
    pass

class AppSearchPipeline(object):
    settings = None
    app_search = None
    items_buffer = []

    @classmethod
    def validate_settings(cls, settings):
        def validate_setting(setting_key):
            if settings[setting_key] is None:
                raise InvalidSettingsException('%s is not defined in settings.py' % setting_key)

        required_settings = {'APPSEARCH_URL', 'APPSEARCH_KEY', 'APPSEARCH_ENGINE'}

        for required_setting in required_settings:
            validate_setting(required_setting)

    @classmethod
    def init_app_search_client(cls, crawler_settings):
        app_search = AppSearch(
            crawler_settings.get('APPSEARCH_URL'),
            http_auth=crawler_settings.get('APPSEARCH_KEY')
        )
        return app_search

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        ext.settings = crawler.settings

        cls.validate_settings(ext.settings)
        ext.app_search = cls.init_app_search_client(crawler.settings)
        return ext

    def send_items(self):
        self.app_search.index_documents(
            engine_name= self.settings['APPSEARCH_ENGINE'],
            body=self.items_buffer
        )

    def process_item(self, item, spider):
        logging.debug('Item sent to AppSearch %s' % self.settings['APPSEARCH_ENGINE'])
        self.items_buffer.append(dict(item))
        if len(self.items_buffer) == 100:
            self.send_items()
            self.items_buffer = []

    def close_spider(self, spider):
        if len(self.items_buffer):
            self.send_items()
