# Contributing

## Documenting

We use [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
to easily generate documentation from markdown.  

### Installing Dependencies

```bash
sudo apt-get update
sudo apt-get -y install python3-pip
sudo apt-get -y install mkdocs
pip3 install mkdocs-material mike
```


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

Mkdocs looks for documentation under the ``docs`` folder.  To add a new documentation page, you will need to first add the file
either directly to the ``docs`` folder, or to a different folder with a symbolic link to the ``docs`` folder.  For example, say we wanted to add a page named ``MAINTAINERS.md`` to the root of the project

First, we create the file at the root of the project
    
```bash
touch MAINTAINERS.md
```

Next, we add a symbolic link to the docs folder

```bash
cd docs/reference
ln -s ../../MAINTAINERS.md .
```
    
Finally, we add the file to our navigation in ``mkdocs.yml``

```yaml
- nav:
    - Reference:
        - 'Maintainers': reference/MAINTAINERS.md
```

Now, when you build the documentation you should see the page that
we've added in the "Reference" section with the title "Maintainers".

### Updating the Changelog

We follow the guidance of  [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) for
best practices in maintaining a chronological human-readable CHANGELOG.md file.  If
the change is worth developers and users knowing about, consider adding an entry 
to the change log.
