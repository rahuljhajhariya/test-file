"""
Determine the season based on the month number
Dec-Feb = Winter, Mar-May = Spring, Jun-Aug = Summer, Sep-Nov = Autumn.

"""

season="may"
if(season=="dec" or season=="jan" or season=="feb"):
    print("winter")
elif(season=="march" or season=="april" or season=="may"):
    print("spring")
elif(season=="june" or season=="july" or season=="aug"):
    print("summer")
else:
    print("autumn")
