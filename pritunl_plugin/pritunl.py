"""Pritunl plugin for Let's Encrypt client"""
import pymongo
from pymongo import MongoClient
import json
import re
import os
import subprocess
import logging
import zope.component
import zope.interface
from letsencrypt import interfaces
from letsencrypt.plugins import common

logger = logging.getLogger(__name__)


class PritunlInstaller(common.Plugin):
    zope.interface.implements(interfaces.IInstaller)
    zope.interface.classProvides(interfaces.IPluginFactory)

    description = "Pritunl plugin for Let's Encrypt client"

    @classmethod
    def add_parser_arguments(cls, add):
        add("conf-path", default="/etc/pritunl.conf", help="Pritunl configuration file. E.g. /etc/pritunl.conf. If not specified the plugin will hope on /etc/pritunl.conf as path is correct.")

    def prepare(self):
        pass  # pragma: no cover

    def more_info(self):
        return "Automatically deploy SSL certificate to Pritunl."

    def get_all_names(self):
        return []

    def deploy_cert(self, domain, cert_path, key_path, chain_path=None, fullchain_path=None):
        logger.info("Read certificate")
        f_cert = open(cert_path, 'r')
        f_key = open(key_path, 'r')

        with open(self.conf("conf_path")) as data_file:
            printul_setting = json.load(data_file)

        logger.info("Connect to databse %s" % printul_setting['mongodb_uri'])
        client = MongoClient(printul_setting['mongodb_uri'])

        db = client[re.search('(?<=/)\w+(?:\s|$)', printul_setting['mongodb_uri']).group(0)]

        result = db.settings.update_one(
            {"_id": "app"},
            {"$set": {"server_cert": f_cert.read(), "server_key": f_key.read()}}
        )

        f_cert.close()
        f_key.close()
        client.close()

    def enhance(self, domain, enhancement, options=None):
        pass  # pragma: no cover

    def supported_enhancements(self):
        return []

    def get_all_certs_keys(self):
        return []

    def save(self, title=None, temporary=False):
        pass  # pragma: no cover

    def rollback_checkpoints(self, rollback=1):
        pass  # pragma: no cover

    def recovery_routine(self):
        pass  # pragma: no cover

    def view_config_changes(self):
        pass  # pragma: no cover

    def config_test(self):
        pass  # pragma: no cover

    def restart(self):
        def is_pid_1_systemd():
            try:
                cmdline = open('/proc/1/cmdline', 'rb').read(7)
                return cmdline.startswith('systemd')
            except IOError:
                return false

        def execute_command(command):
            logger.info("Executing command: %s" % command)
            try:
                proc = subprocess.Popen(command)
                proc.wait()

                if proc.returncode != 0:
                    logger.error("Pritunl restart command returned an error")

            except (OSError, ValueError) as e:
                logger.error("Failed to execute the restart pritunl command")

        if is_pid_1_systemd():
            logger.info("Using systemd to restart Pritunl")
            unit_script_locations = ['/usr/lib/systemd/system/', '/etc/systemd/system/']
            pritunl_service_names = ['pritunl.service']
            for path in unit_script_locations:
                for name in pritunl_service_names:
                    full_path = os.path.join(path, name)
                    if os.path.isfile(full_path):
                        logger.info("Found the Pritunl service file at %s" % full_path)
                        execute_command(['systemctl', 'restart', name])
                    return
            logger.error("Found systemd but not the Pritunl service so it could not be restarted")
        else:
            logger.info("Using init  scripts and the service command to restart Pritunl")
            init_script_names = ['pritunl']
            for path in init_script_names:
                if os.path.isfile(os.path.join('/etc/init.d/', path)):
                    logger.info("Found the Pritunl init script at %s" % path)
                    execute_command(['service', path, 'restart'])
                    return
            logging.error("Did not find the Pritunl service so it could not be restarted")
