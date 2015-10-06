# Soletta Project's distro packaging

**Soletta Project** is a framework for making IoT devices.
With Soletta Project's libraries developers can easily write software
for devices that control actuators/sensors and communicate using
standard technologies. It enables adding smartness even on the
smallest edge devices.

Portable and scalable, it abstracts details of hardware and OS,
enabling developers to reuse their code and knowledge on different
targets.

## TOC ##

 * [General Information](#general-information)
 * [RPM](#rpm)
 * [DEB](#deb)
 * [ARCH](#arch)
 * [Contributing](#contributing)


## General Information

This repository aggregates all recipes to build Soletta packages
to various distributions.

## RPM

Under the rpm folder, one will find the .spec file to build all
soletta rpm files.

## DEB

Under the deb folder, one will find the debian recipes to build all
soletta deb files.

## ARCH

Under the arch folder, one will find a script and spec files to generate
PKGBUILDs for soletta and soletta-git packages for Arch Linux.

## Contributing

When submitting code to this project, please indicate that you certify
you are able to contribute the code by adding a signed-off-by line at
the end of your commit message (using your real name) such as:

Signed-off-by: Random J Developer <random@developer.example.org>

This indicates that your contribution abides to the following rules:

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
660 York Street, Suite 102,
San Francisco, CA 94110 USA

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```
