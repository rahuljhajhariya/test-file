"""
Calculate electricity bill based on unit slabs
slabs: 0-100 units @ Rs 1.5, 101-200 @ Rs 2.5, 201-300 @ Rs 4, above 300 @ Rs 5.
"""

unit=50
rs=0
if(unit>300):
    rem=unit-300
    rs=rem*5
    unit=unit - rem
    rem=0
if(unit>200 and unit<=300):
    rem=unit-200
    rs=rs+ rem*4
    unit=unit - rem
    rem=0
if(unit>100 and unit<=200):
    rem=unit-100
    rs=rs+ rem*2.5
    unit=unit - rem
    rem=0
if(unit>0 and unit<=100):
    rem=unit
    rs=rs+ rem*1.5
    
print(rs)