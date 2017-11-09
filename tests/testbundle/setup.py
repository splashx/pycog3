from distutils.core import setup

setup (
    name = "testbundle",
    version = "0.1.0",
    description = "Cog testbundle for pycog3",
    author = "Diogenes Santos de Jesus",
    author_email = "diogenes.jesus@telekom.com",
    packages = ["testbundle",
                "testbundle.commands",
                "testbundle.commands.level1",
                "testbundle.commands.level1.level2a",
                "testbundle.commands.level1.level2b.level3"],
    keywords = ["cog", "otp", "bot", "devops", "chatops", "automation"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License"
    ]
)
