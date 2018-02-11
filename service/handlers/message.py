from misc.handlers import TemplateHandler

from aiohttp_security import authorized_userid

from aiohttp import web
from . import BaseHandler
from ..storages.users import Storage

from datetime import datetime as dt
import json
import os


class Handler(
    BaseHandler,
    TemplateHandler,
):
    path = 'service/storages/log.json'

    message_counter = 0
    max_message_counter = 1000

    messages = []

    init_file = True

    def __init__(self, app):
        self.storage = Storage(app)
        self.loop = app['loop']
        self.loop.run_until_complete(self.pre_setup_json_file())

    async def pre_setup_json_file(self):
        await self._flush()
        if os.stat(self.path).st_size == 0:
            with open(self.path, 'w') as outfile:
                outfile.write('[\n]')

    async def message(self, request):
        data = await request.json()
        username = await authorized_userid(request)
        now = dt.now().time()
        resp = {
            'time': str(now),
            'name': username,
            'message': data['message'],
        }

        self.messages.append(resp)
        await self._save_message_to_log(resp)

        return web.Response(
            status=web.HTTPOk.status_code,
            content_type='text/html',
            charset='utf-8',
            body=json.dumps(resp),
            reason=None,
        )

    async def _save_message_to_log(self, data):
        self.message_counter += 1
        if self.message_counter >= self.max_message_counter:
            await self._flush()
            self.message_counter = 0
        await self._save(data)

    async def _save(self, data):
        with open(self.path, 'rb+') as outfile:
            outfile.seek(-1, os.SEEK_END)
            outfile.truncate()

        with open(self.path, 'a') as outfile:
            if not self.init_file:
                outfile.write(',\n')
            json.dump(data, outfile, sort_keys=True)
            outfile.write(']')
            self.init_file = False

    async def _flush(self):
        open(self.path, 'w').close()

    async def get_cached_messages(self, request):
        with open(self.path) as json_data:
            data = json.load(json_data)

        return web.Response(
            status=web.HTTPOk.status_code,
            content_type='text/html',
            charset='utf-8',
            body=json.dumps(data),
            reason=None,
        )

    async def get_current_messages(self, request):
        username = await authorized_userid(request)
        messages_send = [
            message for message in self.messages
            if message['name'] != username
        ]
        self.messages = [
            message for message in self.messages
            if message['name'] == username
        ]
        print('=' * 20)
        print('flushed')
        print('=' * 20)

        return web.Response(
            status=web.HTTPOk.status_code,
            content_type='text/html',
            charset='utf-8',
            body=json.dumps({
                'user': username,
                'messages': messages_send,
            }),
            reason=None,
        )

    async def _flush_current_messages(self):
        self.messages.clear()
