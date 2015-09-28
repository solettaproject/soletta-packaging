pkgname=soletta
pkgver=1_beta4
pkgrel=1
checkdepends=()
conflicts=('soletta-git')
source=("https://github.com/solettaproject/soletta/archive/v$pkgver.tar.gz")
md5sums=('26ce6240441f8cefba538c59f645b5c5')

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
