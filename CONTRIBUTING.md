# Contributing

## Documenting

We use [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
to easily generate documentation from markdown.  This simplifies the relationship between our documentation and raw github files.  Mkdocs generates documentation from the ``docs`` folder.  We prefer that the
repository has inline documentation right next to the code.  This makes the documentation readable in it's raw format on github.  To accomplish this, we add symbolic links from the ``docs`` directory to folders and files from the repository that we wish to include in the documentation.

### Testing

To quickly test the version of the documentation you're using, without commiting
anything to the ``gh-pages`` branch, run the following command.

```bash
mkdocs serve --dev-addr=0.0.0.0:8000
```

### Deploying

We use [mike](https://github.com/jimporter/mike) to maintain multiple versions
of the documentation.  To build the documentation with mike, call

```bash
mike deploy <tag>
```

This will build the documentation, and add a static version of the site under the
``gh-pages`` branch.  For example, to deploy the master documentation we do

```bash
mike deploy master
```

To set the default documentation version to master we would do.

```bash
mike set-default master
```

To push the documentation to Github Pages.

```bash
mike deploy master --push
```

### Adding a new page

To add a new documentation page, you will need to first add the file
either directly to the ``docs`` folder, or to a different folder with a symbolic link to the ``docs`` folder.  For example, say we wanted to add a page named ``MAINTAINERS.md`` to the root of the project

First, create the file at the root of the project
    
```bash
touch MAINTAINERS.md
```

Next, add a symbolic link to the docs folder

```bash
cd docs
ln -s ../MAINTAINERS.md .
```
    
Finally, add the file to our navigation in ``mkdocs.yml``

```yaml
- nav:
    - Reference:
        - 'Maintainers': MAINTAINERS.md
```

Now, when you build the documentation you should see the page that
we've added in the "Reference" section with the title "Maintainers".