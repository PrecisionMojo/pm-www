"""Tasks that deal with publishing assets and data."""

import os
from fabric.api import cd, hide, local, task
from django.core.management import call_command

from settings import PROJECT_ROOT, SITE_NAME, STATIC_ROOT

# File that has a list of ignore patterns to pass to collectstatic().
IGNORE_FILE = os.path.join(PROJECT_ROOT, 'static_ignore_patterns.txt')


@task
def update_staticfiles(static_cache='static_cache'):
    """Collect and process static files."""
    with cd(PROJECT_ROOT), hide('running'):
        local('rm -rf %s' % static_cache)
        collectstatic(interactive=False,
                      ignore_patterns=get_ignore_patterns())
        local('git add %s' % static_cache)
        local('git commit %s -m "Update static files cache directory."' % static_cache)


@task
def upload_staticfiles(static_root=STATIC_ROOT, bucket=None):
    """Upload static files to Amazon S3."""
    if bucket is None:
        bucket = os.environ.get('AWS_STORAGE_BUCKET_NAME', SITE_NAME)
    with cd(PROJECT_ROOT), hide('running'):
        local('s3cmd sync %s s3://%s -v -P' % (static_root, bucket))


def collectstatic(*args, **options):
    return call_command('collectstatic', *args, **options)


def get_ignore_patterns():
    ignore_patterns = []
    if os.path.exists(IGNORE_FILE):
        for line in open(IGNORE_FILE, 'r').readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                ignore_patterns.append(line)
    return ignore_patterns