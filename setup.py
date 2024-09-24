#Convert python file into executable file which we can share with anyone
# and they can simply install the application in their system
# without installing python into their system
from cx_Freeze import setup, Executable,sys

includefiles=['icon.ico']
excludes=[]
packages=[]
base=None

if sys.platform=="win32":
    base="win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "Billing_System",
     "TARGETDIR",
     "[TARGETDIR]\main.exe",
     None,
     None,
     None,
     None,
     "TARGETDIR",
    )
]
msi_data={"Shortcut":shortcut_table}
bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="Billing System",
    author="Rashmi Kumari",
    name="Billing System",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon='icon.ico',
        )
    ]
)

