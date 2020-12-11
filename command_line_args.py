import sys
import getopt

def usage():
    print("Usage:")
    print("  app_name -h | --help")
    print("  app_name -i <input_file_path> -o <output_file_path>")
    print()
    print("Options:")
    print(f"  {'-h --help':13} Show this screen.")
    print(f"  {'-i --input':13} Input file.")
    print(f"  {'-o --output':13} Output file.")

def main():
    try:
        # ':' after a short argument means that a value is needed after
        # '=' after a long argument means that a value is needed after
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input=", "output="])
        arguments = { key:value for key,value in opts  }

        if "-h" in arguments or "--help" in arguments:
            usage()
            sys.exit()

        for key,value in arguments.items():
            if key in ("-i", "--input"):
                print(f"Input file: '{value}'")
            elif key in ("-o", "--output"):
                print(f"Output file: '{value}''")

    except getopt.GetoptError as err:
        print("Error:", err)
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()