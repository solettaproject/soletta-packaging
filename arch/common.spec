# Maintainer: Anselmo L. S. Melo <anselmo.melo@intel.com>
pkgdesc="Soletta project is a framework for making IoT devices."
arch=('i686' 'x86_64')
url="http://github.com/solettaproject/soletta"
license=('apache')
depends=('python>=3.4' 'python-jsonschema' 'icu' 'curl' 'systemd' 'pcre' 'libmicrohttpd>=0.9.43')
makedepends=('git' 'python>=3.4' 'python-jsonschema')
optdepends=('gtk3' 'mosquitto')
