"""Test qr_codes.cli."""
from click.testing import CliRunner

from qr_codes.cli import cli


class TestQrCodes:
    """Test qr_codes.cli."""

    def test_cli_no_argument(self) -> None:
        """Should return exit code 0."""
        runner = CliRunner()
        result = runner.invoke(
            cli,
        )
        assert result.exit_code == 0

    def test_cli_decode(self) -> None:
        """Should return exit code 0."""
        runner = CliRunner()
        result = runner.invoke(cli, ["decode", "tests/test.png"])
        assert result.exit_code == 0
        assert len(result.output) > 0

    def test_cli_encode(self) -> None:
        """Should return exit code 0."""
        runner = CliRunner()
        result = runner.invoke(cli, ["encode", "tests/test.txt"])
        assert result.exit_code == 0
        assert len(result.output) == 0

    def test_cli_decode_file_not_found(self) -> None:
        """Should return exit code 0."""
        runner = CliRunner()
        result = runner.invoke(cli, ["decode", "tests/test_not_found.png"])
        assert result.exit_code == 2
        assert len(result.output) > 0

    def test_cli_decode_image_error(self) -> None:
        """Should return exit code 0."""
        runner = CliRunner()
        result = runner.invoke(cli, ["decode", "tests/image-error.png"])
        assert result.exit_code == 2
        assert len(result.output) > 0
