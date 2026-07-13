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

## Contributing a change

All changes to JetBot are made through pull requests on GitHub.  These pull requests should be made directly
to the master branch.  The procedure, in general, is as follows

### Keep it minimal

Try to make the scope of a change as small as possible while still accomplishing something valuable.  Changes that accomplish more than one thing at a time are more difficult to validate.  There could be an amazing contribution in a large pull request, but if it's associated with many other unrelated changes, it's very difficult to integrate safely.  If it's short and sweet, we're better able to assess the purpose and impact of the change and integrate quickly.
If theres more you want to contribute, simply create multiple pull requests :).

### Update the changelog

If a change is worth other developers and users knowing about, it should include an entry in the ``CHANGELOG.md`` file.  For this, we follow the guidance of  [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) for
best practices in maintaining a chronological human-readable CHANGELOG.md file.  Because *all* changes are directly made to master, this entry should *always and only* come under the *Master* section. 

## Versioning

> This section is not relevant for most developers, but included for reference.  

NVIDIA is responsible for versioning of the JetBot software.  However, if you feel the state of the software is in a position that you might want to back reference, a version increment may be necessary.  The general procedure we follow for versioning is as follows

1. A new version name is decided.  This depends on the scope of changes since the previous version
2. The CHANGELOG is updated.  A new section for the new version is created.  Items in the master section are moved under this section.  No new changes should be added in the versioning process, the content should merely be shifted.  
3. The setup.py is updated to reflect the new version.
4. A pull request is made for the new version.  The changes are squashed so the version increment happens atomically.
5. The commit is tagged with the version number.

Please note, versioning is related to the state of the JetBot repository.  It occurs *independently* from SD card and docker container generation.  

## SD Cards and Containers

> This section is not relevant for most developers, but included for reference.  

When deemed necessary, new JetBot SD card images and/or docker containers may be released.  All publicly released SD card images and containers are based on an existing state of software.  These images and containers depend on more than just the version of JetBot software, such as system configuration and operating system versions.  That said, they will always depend on JetBot software in some way, and it is important to note the version of software used.

1. The JetBot git commit hash
2. The JetBot version tag associated with a git hash

For public releases (2) is preferred.  Though in some instances, a release tag may not be associated, such as if we want to release an experimental SD card image based on master.  In this instance, the commit hash is used.  In some instances, it may be possible that multiple SD cards exist for the same JetBot version, for example if they are configured for a specific system (ie: Jetson 2GB vs 4GB, JetPack 4.3 vs 4.4, etc.).  The relevant information should be appended to the SD card name.

In summary,

```
jetbot-<jetbot commit hash or version>-<other information>
```

This file may be shared in multiple ways.  Typically, this is through the JetBot documentation. 

> Please note, because SD card images, docker containers depend on the state of the JetBot software, references to these are not included before the git version tag, since this would create a circular dependency.  Consider SD card images, docker containers, and documentation as separate projects, which *depend* on JetBot software.