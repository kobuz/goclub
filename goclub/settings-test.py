# coding: utf-8
from goclub.settings import *

SOUTH_TESTS_MIGRATE = False
TEST_RUN = True

TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = PROJECT_ROOT
TEST_DISCOVER_PATTERN = "test_*"
