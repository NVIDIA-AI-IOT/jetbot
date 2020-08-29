import argparse
import getpass
import os

STATS_SERVICE_TEMPLATE = """
[Unit]
Description=JetBot container auto-start service

[Service]
Type=simple
User=%s
ExecStart=/bin/sh -c "%s/docker_autostart.sh" 
WorkingDirectory=%s
Restart=always

[Install]
WantedBy=multi-user.target
"""

STATS_SERVICE_NAME = 'jetbot_container_autostart'


def get_stats_service(script_dir):
    return STATS_SERVICE_TEMPLATE % (getpass.getuser(), script_dir, os.environ['HOME'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='jetbot_container_autostart.service')
    parser.add_argument('--script_dir')
    args = parser.parse_args()

    with open(args.output, 'w') as f:
        f.write(get_stats_service(args.script_dir))
