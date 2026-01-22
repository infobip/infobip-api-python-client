import pytest

from infobip_api_client import Configuration


class TestHostHttpsEnforcement:
    """Tests for Configuration host URL HTTPS enforcement."""

    def test_http_scheme_raises_error(self):
        """HTTP scheme should raise ValueError."""
        with pytest.raises(ValueError, match="HTTP is not supported"):
            Configuration(host="http://api.infobip.com", api_key="test-key")

    def test_https_scheme_preserved(self):
        """HTTPS scheme should remain unchanged."""
        config = Configuration(host="https://api.infobip.com", api_key="test-key")
        assert config.host == "https://api.infobip.com"

    def test_no_scheme_adds_https(self):
        """Missing scheme should default to HTTPS."""
        config = Configuration(host="api.infobip.com", api_key="test-key")
        assert config.host == "https://api.infobip.com"

    def test_http_uppercase_raises_error(self):
        """HTTP scheme (uppercase) should raise ValueError."""
        with pytest.raises(ValueError, match="HTTP is not supported"):
            Configuration(host="HTTP://api.infobip.com", api_key="test-key")

    def test_http_mixed_case_raises_error(self):
        """HTTP scheme (mixed case) should raise ValueError."""
        with pytest.raises(ValueError, match="HTTP is not supported"):
            Configuration(host="Http://api.infobip.com", api_key="test-key")

    def test_host_setter_http_raises_error(self):
        """Setting host with HTTP via property should raise ValueError."""
        config = Configuration(api_key="test-key")
        with pytest.raises(ValueError, match="HTTP is not supported"):
            config.host = "http://example.com"

    def test_host_setter_no_scheme_adds_https(self):
        """Setting host without scheme via property should add HTTPS."""
        config = Configuration(api_key="test-key")
        config.host = "example.com"
        assert config.host == "https://example.com"

    def test_https_host_with_port_preserved(self):
        """Port number should be preserved with HTTPS."""
        config = Configuration(host="https://api.infobip.com:8080", api_key="test-key")
        assert config.host == "https://api.infobip.com:8080"

    def test_https_host_with_path_preserved(self):
        """Path should be preserved with HTTPS."""
        config = Configuration(host="https://api.infobip.com/v1", api_key="test-key")
        assert config.host == "https://api.infobip.com/v1"

    def test_https_host_with_subdomain_preserved(self):
        """Subdomain should be preserved with HTTPS."""
        config = Configuration(host="https://xyz123.api.infobip.com", api_key="test-key")
        assert config.host == "https://xyz123.api.infobip.com"

    def test_empty_string_host_unchanged(self):
        """Empty string should remain unchanged."""
        config = Configuration(api_key="test-key")
        config.host = ""
        assert config.host == ""

    def test_whitespace_host_with_https_trimmed(self):
        """Whitespace around host should be trimmed."""
        config = Configuration(host="  https://api.infobip.com  ", api_key="test-key")
        assert config.host == "https://api.infobip.com"

    def test_localhost_http_allowed(self):
        """HTTP localhost should be allowed (for testing)."""
        config = Configuration(host="http://localhost:8080", api_key="test-key")
        assert config.host == "http://localhost:8080"

    def test_localhost_https_preserved(self):
        """HTTPS localhost should be preserved."""
        config = Configuration(host="https://localhost:8080", api_key="test-key")
        assert config.host == "https://localhost:8080"

    def test_127_0_0_1_http_allowed(self):
        """HTTP 127.0.0.1 should be allowed (for testing)."""
        config = Configuration(host="http://127.0.0.1:8080", api_key="test-key")
        assert config.host == "http://127.0.0.1:8080"


class TestEnsureHttpsMethod:
    """Tests for the _ensure_https static method directly."""

    def test_none_returns_none(self):
        """None input should return None."""
        assert Configuration._ensure_https(None) is None

    def test_empty_string_returns_empty(self):
        """Empty string should return empty string."""
        assert Configuration._ensure_https("") == ""

    def test_whitespace_only_returns_empty(self):
        """Whitespace-only string should return empty string."""
        assert Configuration._ensure_https("   ") == ""

    def test_http_raises_error(self):
        """HTTP should raise ValueError."""
        with pytest.raises(ValueError, match="HTTP is not supported"):
            Configuration._ensure_https("http://example.com")

    def test_https_unchanged(self):
        """HTTPS should remain unchanged."""
        assert Configuration._ensure_https("https://example.com") == "https://example.com"

    def test_no_scheme_adds_https(self):
        """No scheme should add HTTPS."""
        assert Configuration._ensure_https("example.com") == "https://example.com"

    def test_localhost_http_allowed(self):
        """Localhost URLs with HTTP should be allowed."""
        assert Configuration._ensure_https("http://localhost:8080") == "http://localhost:8080"

    def test_127_0_0_1_http_allowed(self):
        """127.0.0.1 URLs with HTTP should be allowed."""
        assert Configuration._ensure_https("http://127.0.0.1:8080") == "http://127.0.0.1:8080"
