import os

scan_paths = "rubb\\sequences"
scan_names = [os.path.join(dp, f) for dp, dn, fn in os.walk(  # pointclouds' name
    os.path.expanduser(scan_paths)) for f in fn]
scan_names.sort()
print("--------------------------------------------------")