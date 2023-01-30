import click

from pyzbar.pyzbar import decode as zbar_decode, PyZbarError
from PIL import Image
import qrcode


@click.group()
def cli():
    pass


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
def decode(filename):
    """Decode QR code from FILENAME

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
    except FileNotFoundError:
        print("File not found")
    except PyZbarError as e:
        print(f"Error reading QR code: {e}")
    except Exception as e:
        print(f"Error: {e}")


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
def encode(filename):
    """Encode QR code from FILENAME

    FILENAME: path to text file"""
    try:
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

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    cli()
