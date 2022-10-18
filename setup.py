from setuptools import setup, find_packages

setup(name='word2text_ru',
      version='0.1',
      url='https://github.com/AAYKK/word2text_ru',
      author='Ayk Akopyan',
      author_email='ayk.work@mail.ru',
      description='Перевод чисел в текст по-русски',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)