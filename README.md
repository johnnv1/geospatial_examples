# geospatial_examples
Just some scripts/examples in python for geospatial data. Also a repo for testing some news features at Python 3.10


## Repo organization

* At [example_module](./example_module/) has a package to test something as a package.
* At [examples](./examples) has scripts to test different things using the example_module and also some scripts tests.
* At [annotations](./annotations/) has annotations (why and how it was done) for different scripts and modules at the package.

## Some things used to `organize` the codes

- [Black](https://github.com/psf/black) as code formatter. Configs at [./.config/pyproject_black.toml](./.config/pyproject_black.toml)
- [Flake8](https://github.com/PyCQA/flake8) as code style enforcement. Configs at [./.config/flake8.cfg](./.config/flake8.cfg)
- [Pylint](https://github.com/PyCQA/pylint) as a linter.
- [Numpy Docstrings](https://numpydoc.readthedocs.io/en/latest/format.html) as the pattern to write the documentations of the code. These documentations are used to auto-generate the docs available at [gh-pages](https://johnnv1.github.io/geospatial_examples/) of this repo.
- Docs generation, to generate the docs in a local environment see [./annotations/generating_docs.md](./annotations/generating_docs.md)
  - [Sphinx](https://www.sphinx-doc.org/en/master/) to generate/setup the docs
  - [sphinx-action](https://github.com/ammaraskar/sphinx-action) to automate with gh actions the generation and deploy of the docs to gh pages

### The [./.vscode/](./.vscode/)
I know the setup (and also IDE) is a personal choice, so, this [./.vscode/settings.json](./.vscode/settings.json) is just a suggestion that works well for me.

Also, at [./annotations/setup/vscode.md](./annotations/setup/vscode.md) have some explains about these configs and some extensions for vscode that can help someone.