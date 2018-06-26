import cx_Freeze



executables = [cx_Freeze.Executable("pygame_car.py")]

cx_Freeze.setup(

    name="Fast&curious",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )


# shift and right click
# C:/Python34/python setup.py build

# You can also do something like
# python setup.py bdist_msi

# If you're on a mac, then you would do
# python setup.py bdist_dmg