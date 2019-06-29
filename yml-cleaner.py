from __future__ import print_function

def extract_name(this):
    this = this.strip().replace('-route:', '')
    this = this.replace('app-np.example.com', '')
    this = this.replace('.', '')

    return this

def orderedSet(this):
    encountered = []
    for _ in this:
        if _ not in encountered:
            encountered.append(_)

    return encountered
    
with open('app-dev.yml', 'r') as f:
    content = f.readlines()

f.close()

idx = 0
for _ in content:
    if 'app-np.example.com' in _:
        if 'qa-dev' in _:
            pass
        elif 'qa' in _:
            _ = _.replace('qa', 'qa-dev')
        else:
            this = extract_name(_)
            _ = _.replace(this, this + '-qa-dev')

        content[idx] = _
    idx += 1

content = orderedSet(content)

with open('app-dev.yml', 'w') as f:
    for _ in content:
        f.write(_)

f.close()
