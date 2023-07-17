biggest=0
with open('data/day1') as f:
  current=0
  for line in f:
    line=line.strip()
    if(line.isdecimal()):
      current+=int(line)
      if(current>biggest):
        biggest=current
    else:
      current=0
      print(f'Biggest so far: {biggest}')
