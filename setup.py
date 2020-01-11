from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jellyfin-mpv-shim',
    version='0.0.1',
    author="Ian Walton",
    author_email="iwalton3@gmail.com",
    description="Cast media from Jellyfin Mobile and Web apps to MPV. (Unofficial)",
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iwalton3/jellyfin-mpv-shim",
    packages=['plex_mpv_shim'],
    entry_points={
        'console_scripts': [
            'plex-mpv-shim=jellyfin_mpv_shim.mpv_shim:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['python-mpv', 'requests']
)
