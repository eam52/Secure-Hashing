import pytest
import os
import hashlib
from antivirus import hashfile, compared_hash

## i have to create a temporary file to test
## better than usuing the real file, for isolation reasons


def test_hashfile():
    expected_hash = haslib.sha256(b'Hello, world').hexdigest()
    assert hashfile(temp_file) == expected_hash