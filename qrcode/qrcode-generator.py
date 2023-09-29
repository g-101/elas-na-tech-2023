import qrcode
import argparse

color = (0, 0, 0)
bg_color = (255,255,255)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Python Qrcode generator")
    
    parser.add_argument("-u", "--url", type=str, required=True, help="site url")
    parser.add_argument("-n", "--name", type=str, required=True, help="nome do arquivo")
    parser.add_argument("-c", "--color", type=int, nargs='+',  help="cor primaria do qrcode")
    parser.add_argument("-bg", "--bgcolor", type=int, nargs='+', help="cor do background do qrcode")

    args = parser.parse_args()
    url = args.url
    if args.color != None: 
        color = tuple(args.color)         
    if args.bgcolor != None:   
        bg_color = tuple(args.bgcolor) 
    
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,)
    qr.add_data(url)
    image = qr.make_image(fill_color=color, back_color=bg_color)
    image.save(f"images/{args.name}.png")
    image.show()