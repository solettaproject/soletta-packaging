Summary: A framework for making IoT devices
Name: soletta
Version: 0.0.1
Release: 1%{?dist}
License: BSD 3-Clause
Group: System Environment/Libraries
URL: http://github.com/solettaproject/soletta

Source0: https://github.com/solettaproject/soletta/archive/v1_beta3.tar.gz

BuildRequires: python3 >= 3.4
BuildRequires: python3-jsonschema
BuildRequires: chrpath
BuildRequires: pcre-devel
BuildRequires: libicu-devel
BuildRequires: libcurl-devel
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel

%description
Soletta project is a framework for making IoT devices. With Soletta
library developers can easily write software for devices that control
actuators/sensors and communicate using standard technologies. It
enables adding smartness even on the smallest edge devices.

%package -n lib%{name}
Summary: A framework for making IoT devices
Group: System Environment/Libraries

%description -n lib%{name}
Soletta library allows developers to easily write software for devices
that control actuators/sensors and communicate using standard
technologies. It enables adding smartness even on the smallest edge
devices.

%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%package -n lib%{name}-modules
Summary: Flow, linux-micro and pin multiplexing modules for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-modules
This package contains all the dynamic modules for %{name}.

%package -n lib%{name}-devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n lib%{name}-doc
Summary: Development documentation for %{name}
Group: Documentation

%description -n lib%{name}-doc
This package contains the development documentation for %{name}.

%prep
%setup -n %{name}

%build
export LIBDIR=%{_libdir}/
make alldefconfig
%{__make} %{?_smp_mflags}

# TODO: should we generate man pages from doxygen tags?
# %{__make} doc || :

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install

%clean
%{__rm} -rf %{buildroot}

%files -n lib%{name}
%defattr(-, root, root, 0755)
%{_bindir}/sol-fbp-runner
%{_libdir}/*.so*
%{_datadir}/soletta/board_detect.json
%{_datadir}/soletta/flow/descriptions/*.json

%files -n lib%{name}-devel
%defattr(-, root, root, 0755)
%{_bindir}/sol-fbp-generator
%{_bindir}/sol-fbp-to-dot
%{_bindir}/sol-flow-node-type-gen.py
%{_bindir}/sol-flow-node-types
%{_bindir}/sol-flow-node-type-validate.py
%{_includedir}/soletta/*
%{_datadir}/gdb/auto-load/*
%{_libdir}/pkgconfig/soletta.pc
%{_datadir}/soletta/flow/schemas/node-type-genspec.schema

%files -n lib%{name}-modules
%defattr(-, root, root, 0755)
%{_libdir}/soletta/modules/*

# TODO: should we generate man pages from doxygen tags?
# %files -n lib%{name}-doc
# %defattr(-, root, root, 0755)
# %doc %{_mandir}/man3/*

%license COPYING

%changelog
* Wed Sep  9 2015 Gustavo Lima Chaves
-
