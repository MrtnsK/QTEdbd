from cx_Freeze import setup, Executable


setup(
    name = "qte",
    version = "0.1",
    description = "Skill check from dbd training",
    executables = [Executable("qte.pyw")],
)