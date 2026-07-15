quantity = int(input("จำนวนปืนที่รับมาขาย : "))
cost_price = int(input("ต้นทุนของปืนที่รับมา : "))
sell_price = int(input("ราคาที่จะนำไปขายต่อ : "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน : "))

cost = cost_price * quantity

income = sell_price * quantity

Net = income - cost

Boss = (Net * 20) / 100

prep = (Net-Boss) / team_members

print("ต้นทุน",cost,"THB")
print("รายรับทั้งหมด",income,"THB")
print("กำไรสุทธิ",Net,"THB")
print("จำนวนเงินที่หักไปให้บอส",Boss,"THB")
print("จำนวนเงินที่ลูกน้องแต่ละคนได้",prep,"THB")