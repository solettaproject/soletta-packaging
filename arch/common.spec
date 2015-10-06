# Maintainer: Anselmo L. S. Melo <anselmo.melo@intel.com>
pkgdesc="Soletta project is a framework for making IoT devices."
arch=('i686' 'x86_64')
url="http://github.com/solettaproject/soletta"
license=('custom:BSD3')
depends=('python>=3.4' 'python-jsonschema' 'icu' 'curl' 'systemd' 'pcre')
makedepends=('git' 'python>=3.4' 'python-jsonschema')
optdepends=('gtk3' 'libmicrohttpd' 'mosquitto')
