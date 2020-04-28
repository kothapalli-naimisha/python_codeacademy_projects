def ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight > 2 and weight <= 6:
    price_per_pound =3.00
  elif weight >6 and weight <=10:
    price_per_pound =4.00
  else:
    price_per_pound =4.75
  return 20+(weight*price_per_pound) 
print(ground_shipping(8.4))

premium_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight > 2 and weight <= 6:
    price_per_pound =9.00
  elif weight >6 and weight <=10:
    price_per_pound =12.00
  else:
    price_per_pound =14.25
  return (weight*price_per_pound)
print(drone_shipping(1.5))