
def load_material(filename):
    mtl_contents = {}
    mtl_file = None
    for line in open(filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'newmtl':
            mtl_file = mtl_contents[values[1]] = {}
        elif mtl_file is None:
            raise ValueError("mtl file not found")
        else:
            mtl_file[values[0]] = list(map(float, values[1:]))
        print("Parsing mtl...")
    return mtl_contents