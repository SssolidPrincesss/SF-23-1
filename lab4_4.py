def main(X, *args):
    one = X 
    two = sum(args)  
    three = float(len(args)) 
    print(f"one={one}\ntwo={two}\nthree={three}")
    return X + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\nresult={result}")