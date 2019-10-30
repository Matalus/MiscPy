
province = "Yukon"

def can_tax_rate(province):
   province = province.lower()
   if province in('alberta','nunavat','yukon'):
         tax = 0.05
   elif province == 'ontario':
      tax = 0.13
   else:
      tax = 0.15
   return tax

print("Tax rate is: {}".format(str(can_tax_rate(province))))


