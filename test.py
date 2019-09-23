import os

if __name__ == '__main__':
    dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    print_pretty_table(f"************: {dir_path}")