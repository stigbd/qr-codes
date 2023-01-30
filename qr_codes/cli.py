"""Command line interface for QR code encoder/decoder."""
import click
from PIL import Image, UnidentifiedImageError
from pyzbar.pyzbar import decode as zbar_decode, PyZbarError
import qrcode


@click.group()
def cli() -> None:
    """QR code encoder/decoder."""
    pass


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
def decode(filename) -> None:
    """Decode QR code from FILENAME.

    FILENAME: path to image file
    """
    try:
        codes = zbar_decode(Image.open(filename))
        print(f"number of codes in image: {len(codes)}")
        for code in codes:
            data = code.data.decode("utf-8")
            print(f"data(decoded): >{data}<")
            print(f"type: {code.type}")
            print()
    except PyZbarError as e:  # pragma: no cover
        print(f"Error: Error decoding QR code: {e}")
        exit(2)
    except UnidentifiedImageError as e:
        print(f"Error: Error opening image file: {e}")
        exit(2)


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
def encode(filename) -> None:
    """Encode QR code from FILENAME.

    FILENAME: path to text file
    """
    with open(filename, "r") as f:
        data = f.read()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data.strip())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f'{filename.split(".")[0]}.png')


if __name__ == "__main__":  # pragma: no cover
    cli()
