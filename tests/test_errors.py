"""Test picorun classes."""

__author__ = "Dave Hall <skwashd@gmail.com>"
__copyright__ = "Copyright 2023 - 2026, Dave Hall https://proactiveops.io"
__license__ = "MIT"

import picorun.errors


def test_api_error() -> None:
    """Test ApiError."""
    error = picorun.errors.ApiError("message", 404)
    assert str(error) == "Error 404: message"
    assert error.status_code == 404
