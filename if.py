import sys
instance_Type = sys.argv[1]
if instance_Type == "t2.micro":
    print("Only 1 cpu and 1 GB RAM")
elif instance_Type == "t2.small":
    print("Only 2 cpu and 2 GB RAM")
elif instance_Type == "t2.medium":
    print("Only 4 cpu and 4 GB RAM")
elif instance_Type == "t2.xlarge":
    print("Only 8 cpu and 8 GB RAM")
else:
    print("Provide a valide instance type")
