from setuptools import setup

setup(name='sonic_api',
      version='0.0',
      description='Python adapter for chatsonic api',
      packages=['chatai'],
      author_email='weirdoo145@gmail.com',
      zip_safe=False,
      requires=["requests"],
      long_description="./readme.md")