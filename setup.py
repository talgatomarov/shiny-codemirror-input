from setuptools import setup, find_packages

setup(
    name='shiny_codemirror_input',
    version='0.1.0',
    author='Talgat Omarov',
    author_email='contact@talgatomarov.com',
    description='A module that provides SQL CodeMirror bindings for Shiny',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/talgatomarov/shiny-codemirror-input',  # or other repository
    packages=find_packages(),  # Automatically find packages in your project
    python_requires='>=3.6',
    package_data={
        'shiny_codemirror_input': ['distjs/*.js'],  # Adjust this path as needed
    },
    install_requires=[
        # list your module dependencies here, e.g. 'requests', 'numpy'
        "shiny"
    ],
)
