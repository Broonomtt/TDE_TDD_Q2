def mult (n1, n2):
  
  if num_true(n1) and num_true(n2):
     return float(n1) * float(n2)
  else:
     return None

    
def num_true(s):
  try:
    float(s)
    return True
  except ValueError:
    return False
