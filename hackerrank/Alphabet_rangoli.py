def print_rangoli(size: int):
    pattern = '-'.join(chr(ch) for ch in reversed(range(ord('a'), ord('a') + size)))
    layers = []
    for limit in range(1, size * 2, 2):
        layer = f'{pattern[:limit]}{pattern[:limit - 1][::-1]}'
        layers.append(f'{layer:-^{size * 4 - 3}}')
        print(layers[-1])
    print('\n'.join(reversed(layers[:-1])))
 
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)