pkgname=soletta
pkgver=1_beta6
pkgrel=1
checkdepends=()
conflicts=('soletta-git')
source=("https://github.com/solettaproject/soletta/archive/v$pkgver.tar.gz")
md5sums=('8ef846a1e9def168ec90d4dfaa5b2c68')

prepare() {
    cd "$pkgname-$pkgver"
    git submodule init && git submodule update
}

build() {
	cd "$pkgname-$pkgver"
    make alldefconfig
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
