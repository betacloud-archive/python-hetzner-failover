#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_config import cfg
from oslo_log import log
import requests
from tabulate import tabulate

CONF = cfg.CONF
LOG = log.getLogger('hetzner-failover')

opts = [
    cfg.StrOpt('username',
               help='Hetzner robot webservice login username'),
    cfg.StrOpt('password',
               help='Hetzner robot webservice login username')
]
CONF.register_opts(opts)


def error(result):
    LOG.error('something failed')


def output(o):
    print(o)


def route():
    pass


def list():
    result = requests.get('https://robot-ws.your-server.de/failover',
                          auth=(CONF.username, CONF.password))
    if result.status_code == 404:
        LOG.error('no failover IP addresses are available')
    elif result.status_code == 200:
        table = []
        for entry in result.json():
            table.append(entry.get('failover', []))
        t = tabulate(table, headers='keys', tablefmt='grid')
        output(t)
    else:
        error(result)


def show():
    result = requests.get('https://robot-ws.your-server.de/failover/%s' %
                          CONF.command.failover_address,
                          auth=(CONF.username, CONF.password))
    if result.status_code == 404:
        LOG.error('failover IP address %s not found' %
                  CONF.command.failover_address)
    elif result.status_code == 200:
        t = tabulate([result.json().get('failover', [])],
                     headers='keys', tablefmt='grid')
        output(t)
    else:
        error(result)


def add_command_parsers(subparsers):
    parser = subparsers.add_parser('list')
    parser.set_defaults(func=list)

    parser = subparsers.add_parser('show')
    parser.add_argument('failover_address', default=None,
                        help='')
    parser.set_defaults(func=show)

commands = cfg.SubCommandOpt('command', title='Commands',
                             help='Show available commands.',
                             handler=add_command_parsers)
CONF.register_cli_opts([commands])

if __name__ == '__main__':
    log.register_options(CONF)
    log.set_defaults()
    log.setup(CONF, 'hetzner-failover')
    CONF(project='hetzner-failover')
    CONF.command.func()
