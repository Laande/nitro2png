import sys
import os
import src.nitro2png as n2png


def main():
    if not sys.argv[1:]:
        file_name = os.path.basename(__file__)
        print(f"Usage: python {file_name} <file> [output]")
        exit(1)

    file = sys.argv[1]

    for name, data in n2png.nitro2png(file):
        n2png.save(name, data)
        
        
if __name__ == '__main__':
    main()