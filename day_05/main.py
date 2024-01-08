def main():
    with open("input.txt", "r") as f:
        content = f.read().split("\n")
    seeds = content.pop(0)
    seeds = seeds.split(":")[1].split(" ")
    seeds.pop(0)
    num = seeds[0]
    content_new = []
    content_temp = []
    for line in content:
        if line != "":
            if line[0].isdigit():
                content_temp.append(line)
            else:
                content_new.append(content_temp.copy())
                content_temp.clear()
    content_new.append(content_temp.copy())
    locations = []
    for seed in seeds:
        num = int(seed)
        for line in content_new:
            for map in line:
                num, mapped = mapper2(num, map)
                if mapped:
                    break
        locations.append(num)
    print(f"the min is {min(locations)}")
            
def test():
    print(mapper2(55, "52 50 48"))

def mapper2(input: int, map: str) -> tuple[int, bool]:
    map_int: int = [int(num) for num in map.split(" ")]
    dest = map_int[1]
    if input < map_int[1]:
        return (input, False)
    if input > map_int[1] + map_int[2]:
        return (input, False)
    offset = input - map_int[1] 
    return (map_int[0] + offset, True)
   
if __name__ == "__main__":
    main()
