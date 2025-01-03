import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("num1", help = "first_argument")
    parser.add_argument("num2", help="second argument")
    
    args = parser.parse_args()

    n1 = int(args.num1)
    n2 = int(args.num2)

    print(n1+n2)