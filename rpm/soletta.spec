%define soletta_release 1_beta4
%define soletta_duktape_release 1_beta2

Summary: A framework for making IoT devices
Name: soletta
Version: 0.0.1
Release: v%{soletta_release}%{?dist}
License: BSD 3-Clause
Group: System Environment/Libraries
URL: http://github.com/solettaproject/soletta
Source0: https://github.com/solettaproject/soletta/archive/v%{soletta_release}.tar.gz
Source1: https://github.com/solettaproject/duktape-release/archive/v%{soletta_duktape_release}.tar.gz
Source2: config
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: pcre-devel
BuildRequires: python3 >= 3.4
BuildRequires: python3-jsonschema

%description
Soletta project is a framework for making IoT devices. With Soletta
library developers can easily write software for devices that control
actuators/sensors and communicate using standard technologies. It
enables adding smartness even on the smallest edge devices.

%package -n lib%{name}
Summary: A framework for making IoT devices
Group: System Environment/Libraries
Requires: pcre
Requires: libicu
Requires: libcurl

%description -n lib%{name}
Soletta library allows developers to easily write software for devices
that control actuators/sensors and communicate using standard
technologies. It enables adding smartness even on the smallest edge
devices.

%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%package -n lib%{name}-flow-module-accelerometer
Summary: Accelerometer flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-accelerometer
This package contains the accelerometer flow module for %{name}. The
module provides flow nodes for accelerometers such as ADXL345 and
LSM303DLHC.

%package -n lib%{name}-flow-module-am2315
Summary: AM2315 flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-am2315
This package contains the AM2315 flow module for %{name}. The module
provides flow nodes that output AM2315 sensor readings (temperature
and humidity).

%package -n lib%{name}-flow-module-calamari
Summary: Calamari flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-calamari
This package contains the calamari flow module for %{name}. The module
provides flow nodes for doing I/O on the Calamari board
(http://elinux.org/Calamari_Lure) components.

%package -n lib%{name}-flow-module-compass
Summary: Compass flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-compass
This package contains the compass flow module for %{name}. The module
provides a compass node that takes direction-vectors of given
accelerometer and a magnetometer nodes and outputs heading towards
Magnetic North Pole, in degrees.

%package -n lib%{name}-flow-module-evdev
Summary: Evdev flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-evdev
This package contains the evdev flow module for %{name}. The module
provides an evdev node that outputs boolean packets after evdev events
(being listened) occur.

%package -n lib%{name}-flow-module-file
Summary: File flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-file
This package contains the file flow module for %{name}. The module
provides a file node meant to read and write data to files
(asynchronously).

%package -n lib%{name}-flow-module-flower-power
Summary: Flower-power flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: libcurl

%description -n lib%{name}-flow-module-flower-power
This package contains the flower-power flow module for %{name}. The
module interfaces with Parrot Flower Power
(http://www.parrot.com/usa/products/flower-power/), measuring and
analysing the four elements crucial the health of plants: sunlight,
temperature, soil moisture and fertilizer. It fetches plant data via
HTTP, using a web service.

%package -n lib%{name}-flow-module-grove
Summary: Grove flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-grove
This package contains the grove flow module for %{name}. The module
provides flow nodes for doing I/O and package conversions for the
Grove Starter Kit
(http://www.seeedstudio.com/wiki/Grove_-_Starter_Kit_v3) components.

%package -n lib%{name}-flow-module-gtk
Summary: Gtk flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: gtk3

%description -n lib%{name}-flow-module-gtk
This package contains the Gtk flow module for %{name}. The module
provides flow nodes for doing I/O of various Soletta basic packet
types, for simulation purposes. Both input and output nodes will be
Gtk UI elements.

%package -n lib%{name}-flow-module-gyroscope
Summary: Gyroscope flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-gyroscope
This package contains the gyroscope flow module for %{name}. The
module provides a flow node for the L3G4200D gyroscope.

%package -n lib%{name}-flow-module-iio
Summary: IIO flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-iio
This package contains the iio flow module for %{name}. The module
provides an IIO-based gyroscope input flow node. As any IIO device, it
can use a buffer to get the readings.

%package -n lib%{name}-flow-module-keyboard
Summary: Keyboard flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-keyboard
This package contains the keyboard flow module for %{name}. The module
provides flow nodes for keyboard input.

%package -n lib%{name}-flow-module-led-strip
Summary: Led-Strip flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-led-strip
This package contains the led-strip flow module for %{name}. The
module provides a flow node for the LPD8806 led strip controller.

%package -n lib%{name}-flow-module-location
Summary: Location flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: libcurl

%description -n lib%{name}-flow-module-location
This package contains the location flow module for %{name}. The module
provides flow nodes interfacing with the free FreeGeoip service, to
obtain the location of either a given IP address or the originating
address.

%package -n lib%{name}-flow-module-magnetometer
Summary: Magnetometer flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-magnetometer
This package contains the magnetometer flow module for %{name}. The
module provides a flow node for the LSM303DLHC magnetometer.

%package -n lib%{name}-flow-module-max31855
Summary: MAX31855 flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-max31855
This package contains the MAX31855 flow module for %{name}. The module
provides a flow node for the MAX31855 temperature reader.

%package -n lib%{name}-flow-module-network
Summary: Network flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-network
This package contains the network flow module for %{name}. The module
provides a flow node that outputs boolean packets after network
connect/disconnect events occur.

%package -n lib%{name}-flow-module-oic
Summary: OIC flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-oic
This package contains the OIC flow module for %{name}. The module
provides server and client flow nodes for Open Interconnect Consortium
"brighlight" class of devices.

%package -n lib%{name}-flow-module-persistence
Summary: Persistence flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-persistence
This package contains the persistence flow module for %{name}. The
module provides flow nodes for storing/retrieving Soletta basic packet
type values on the file system or on EFI variables.

%package -n lib%{name}-flow-module-piezo-speaker
Summary: Piezo-speaker flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-piezo-speaker
This package contains the piezo-speaker flow module for %{name}. The
module provides a flow node for sound output on (PWM) piezo speakers.

%package -n lib%{name}-flow-module-process
Summary: Process flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-process
This package contains the process flow module for %{name}. The module
provides flow nodes for spawning a process and connecting its
stdin/stdout/stderr back into a flow.

%package -n lib%{name}-flow-module-servo-motor
Summary: Servo-motor flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-servo-motor
This package contains the servo-motor flow module for %{name}. The
module provides a flow node to control servo motors.

%package -n lib%{name}-flow-module-test
Summary: Test flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-test
This package contains the test flow module for %{name}. The module
provides flow nodes that aids one to write testing/validation flows
(checking for expected packet results).

%package -n lib%{name}-flow-module-thingspeak
Summary: ThingSpeak flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: libcurl

%description -n lib%{name}-flow-module-thingspeak
This package contains the ThingSpeak flow module for %{name}. The
module provides flow nodes that interface with ThingSpeak -- a service
that allows publishing data via HTTP, to be consumed by IoT devices.
To use these nodes, one must register and obtain an API key. API keys
for channels and talkbacks are different. For the talkback feature,
obtaining a Talkback ID is also required.

%package -n lib%{name}-flow-module-udev
Summary: Udev flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: udev

%description -n lib%{name}-flow-module-udev
This package contains the udev flow module for %{name}. The module
provides a udev flow node that outputs boolean packets after a devices
are attached or dettached on the system.

%package -n lib%{name}-flow-module-unix-socket
Summary: Unix-socket flow module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-module-unix-socket
This package contains the unix-socket flow module for %{name}. The
module provides I/O flow nodes that aid on isolating flows by means of
unix sockets.

%package -n lib%{name}-flow-metatype-module-js
Summary: Javascript flow metatype module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-flow-metatype-module-js
This package contains the javascript flow metatype module for %{name}.
The module a javascript metatype for flows, i. e., the possibility of
declaring new node types with the behaviour implemented in that
language, directly in .fbp files.

%package -n lib%{name}-linux-micro-module-bluetooth
Summary: Bluetooth linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-bluetooth
This package contains the bluetooth linux-micro module for %{name}.
The module controls the bluetooth daemon in the system.

%package -n lib%{name}-linux-micro-module-console
Summary: Console linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-console
This package contains the console linux-micro module for %{name}. The
module spawns agetty (or getty or /bin/sh) on consoles defined by
kernel, respawning as they exit. This service is useful during
development or for devices that should allow maintenance access by a
serial console. The consoles are defined by the kernel as it reads the
kernel command line for "console=XXX" statements, see
https://www.kernel.org/doc/Documentation/serial-console.txt.

%package -n lib%{name}-linux-micro-module-dbus
Summary: D-Bus linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: dbus

%description -n lib%{name}-linux-micro-module-dbus
This package contains the D-Bus linux-micro module for %{name}. The
module controls the D-Bus daemon in the system.

%package -n lib%{name}-linux-micro-module-fstab
Summary: fstab linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-fstab
This package contains the fstab linux-micro module for %{name}. The
module will mount filesystems in /etc/fstab. This is a simple
implementation that will mount entries, however no filesystem check
(fsck) is done. Moreover, the fifth and sixth fields (fs_freq and
fs_passno) are not used. The file /etc/fstab is optional, if it
doesn not exist the service starts but nothing is mounted.

%package -n lib%{name}-linux-micro-module-hostname
Summary: Hostname linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-hostname
This package contains the hostname linux-micro module for %{name}. The
module reads /etc/hostname and sets machine hostname. When the file is
read, leading and trailing spaces are ignored and the resulting string
is sent directly to sethostname(2). The file /etc/hostname must exist.

%package -n lib%{name}-linux-micro-module-locale
Summary: Locale linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-locale
This package contains the locale linux-micro module for %{name}. The
module implements a service to sets locale environment variables. It
will mimic systemd-localed.service and read the locale setting from
/etc/locale.conf or kernel command line, then setting the environment
variables in the current and children processes.

%package -n lib%{name}-linux-micro-module-machine-id
Summary: Machine-Id linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-machine-id
This package contains the machine-id linux-micro module for %{name}.
The module provides a service that guarantees the presence and
validity of a unique machine identifier in the file system. This UUID
is made available for the rest of Soletta by an utility function.

%package -n lib%{name}-linux-micro-module-network-up
Summary: Network-up linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-network-up
This package contains the network-up linux-micro module for %{name}.
The module implements a service that will enumerate all network
interfaces using netlink and then bring up all of them. If the kernel
is configured for IPv6 (CONFIG_IPV6=y) then automatic IP addresses are
assigned based on the MAC address. This service relies on netlink
communication with the kernel.

%package -n lib%{name}-linux-micro-module-rc-d
Summary: rc-d linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-rc-d
This package contains the rc-d linux-micro module for %{name}. The
module provides a init.d/rc.d compatibility service that is able to
run scripts from /etc/init.d or /etc/rc.d with standard parameters
"start", "stop", "restart" and "status". To enable a service all one
needs to do is symlink the service name to rc-d.so. As an example, to
enable /etc/init.d/myservice to be used by linux-micro: ln -s
/usr/lib/soletta/modules/linux-micro/rc-d.so
/usr/lib/soletta/modules/linux-micro/myservice.so. A set of services
are started automatically by Soletta in order to do initialization --
those are listed in
/usr/lib/soletta/modules/linux-micro/initial-services.

%package -n lib%{name}-linux-micro-module-sysctl
Summary: sysctl linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-sysctl
This package contains the sysctl linux-micro module for %{name}. The
module sets kernel parameters from sysctl.conf files. This service
will mimic systemd-sysctl.service and read the settings from
/etc/sysctl.conf or /run/sysctl.d, /etc/sysctl.d,
/usr/local/lib/sysctl.d, /usr/lib/sysctl.d, /lib/sysctl.d. Files are
processed in alphabetical order. See
http://www.freedesktop.org/software/systemd/man/systemd-sysctl.service.html

%package -n lib%{name}-linux-micro-module-watchdog
Summary: Watchdog linux-micro module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-linux-micro-module-watchdog
This package contains the watchdog linux-micro module for %{name}. The
module starts and keeps alive the kernel watchdog. Linux provides a
watchdog API with both software and hardware implementations. The
software implementation may be used to protect against userspace
hangups, while the hardware may protect from kernel hangups as well.
This module will open /dev/watchdog, check the period and start a
timer to keep the watchdog alive, avoiding the system to be rebooted.
If the application hangs for more than such period, the watchdog will
reboot the device. See
https://www.kernel.org/doc/Documentation/watchdog/watchdog-api.txt.

%package -n lib%{name}-pin-mux-module-galileo
Summary: Galileo pin-mux module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-pin-mux-module-galileo
This package contains the galileo pin-mux module for %{name}. The
module provides pin multiplexing rules/mapping for Galileo boards
(revisions D ang G). Without this module, to use Galileo I/O pins with
the desired function, one would have to setup them on their own
beforehand.

%package -n lib%{name}-pin-mux-module-edison
Summary: Edison pin-mux module for %{name}
Group: System Environment/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-pin-mux-module-edison
This package contains the edison pin-mux module for %{name}. The
module provides pin multiplexing rules/mapping for Edison boards
(revision C). Without this module, to use Edison I/O pins with the
desired function, one would have to setup them on their own
beforehand.

%package -n lib%{name}-devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: python3 >= 3.4

%description -n lib%{name}-devel
This package contains the header files, static libraries and
development documentation for %{name}. If you like to develop programs
using %{name}, you will need to install %{name}-devel.

# Docs disabled for now because the man-formatted output is not even
# being created yet

# %package -n lib%{name}-doc
# Summary: Development documentation for %{name}
# Group: Documentation

# %description -n lib%{name}-doc
# This package contains the development documentation for %{name}.

%prep
%setup -n %{name}-%{soletta_release}
%setup -T -D -a 1 -n %{name}-%{soletta_release}
mv duktape-release-%{soletta_duktape_release}/* src/thirdparty/duktape

%build
make %{?_smp_mflags}
# TODO: should we generate man pages from doxygen tags?
# make doc || :

%install
export LIBDIR=%{_libdir}/
cp %{SOURCE2} .config
make %{?_smp_mflags} DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install

%{?%{name}_debug_package}

%files -n lib%{name}
%defattr(-, root, root, -)
%{_libdir}/*.so*
%{_bindir}/sol-fbp-runner
%{_datadir}/soletta/board_detect.json
%{_libdir}/soletta/modules/linux-micro/initial-services

%files -n lib%{name}-devel
%defattr(-, root, root, -)
%{_bindir}/sol-fbp-generator
%{_bindir}/sol-fbp-to-dot
%{_bindir}/sol-flow-node-type-gen.py
%{_bindir}/sol-flow-node-types
%{_bindir}/sol-flow-node-type-validate.py
%{_includedir}/soletta/*
%{_datadir}/gdb/auto-load/*
%{_libdir}/pkgconfig/soletta.pc
%{_datadir}/soletta/flow/schemas/node-type-genspec.schema
%{_datadir}/soletta/flow/descriptions/aio.json
%{_datadir}/soletta/flow/descriptions/app.json
%{_datadir}/soletta/flow/descriptions/boolean.json
%{_datadir}/soletta/flow/descriptions/byte.json
%{_datadir}/soletta/flow/descriptions/color.json
%{_datadir}/soletta/flow/descriptions/console.json
%{_datadir}/soletta/flow/descriptions/constant.json
%{_datadir}/soletta/flow/descriptions/converter.json
%{_datadir}/soletta/flow/descriptions/filter-repeated.json
%{_datadir}/soletta/flow/descriptions/float.json
%{_datadir}/soletta/flow/descriptions/gpio.json
%{_datadir}/soletta/flow/descriptions/int.json
%{_datadir}/soletta/flow/descriptions/led-7seg.json
%{_datadir}/soletta/flow/descriptions/platform.json
%{_datadir}/soletta/flow/descriptions/pwm.json
%{_datadir}/soletta/flow/descriptions/random.json
%{_datadir}/soletta/flow/descriptions/string.json
%{_datadir}/soletta/flow/descriptions/switcher.json
%{_datadir}/soletta/flow/descriptions/temperature.json
%{_datadir}/soletta/flow/descriptions/timer.json
%{_datadir}/soletta/flow/descriptions/timestamp.json
%{_datadir}/soletta/flow/descriptions/trigonometry.json
%{_datadir}/soletta/flow/descriptions/wallclock.json

%files -n lib%{name}-flow-module-accelerometer
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/accelerometer.so
%{_datadir}/soletta/flow/descriptions/accelerometer.json

%files -n lib%{name}-flow-module-am2315
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/am2315.so
%{_datadir}/soletta/flow/descriptions/am2315.json

%files -n lib%{name}-flow-module-calamari
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/calamari.so
%{_datadir}/soletta/flow/descriptions/calamari.json

%files -n lib%{name}-flow-module-compass
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/compass.so
%{_datadir}/soletta/flow/descriptions/compass.json

%files -n lib%{name}-flow-module-evdev
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/evdev.so
%{_datadir}/soletta/flow/descriptions/evdev.json

%files -n lib%{name}-flow-module-file
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/file.so
%{_datadir}/soletta/flow/descriptions/file.json

%files -n lib%{name}-flow-module-flower-power
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/flower-power.so
%{_datadir}/soletta/flow/descriptions/flower-power.json

%files -n lib%{name}-flow-module-grove
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/grove.so
%{_datadir}/soletta/flow/descriptions/grove.json

%files -n lib%{name}-flow-module-gtk
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/gtk.so
%{_datadir}/soletta/flow/descriptions/gtk.json

%files -n lib%{name}-flow-module-gyroscope
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/gyroscope.so
%{_datadir}/soletta/flow/descriptions/gyroscope.json

%files -n lib%{name}-flow-module-iio
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/iio.so
%{_datadir}/soletta/flow/descriptions/iio.json

%files -n lib%{name}-flow-module-keyboard
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/keyboard.so
%{_datadir}/soletta/flow/descriptions/keyboard.json

%files -n lib%{name}-flow-module-led-strip
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/led-strip.so
%{_datadir}/soletta/flow/descriptions/led-strip.json

%files -n lib%{name}-flow-module-location
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/location.so
%{_datadir}/soletta/flow/descriptions/location.json

%files -n lib%{name}-flow-module-magnetometer
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/magnetometer.so
%{_datadir}/soletta/flow/descriptions/magnetometer.json

%files -n lib%{name}-flow-module-max31855
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/max31855.so
%{_datadir}/soletta/flow/descriptions/max31855.json

%files -n lib%{name}-flow-module-network
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/network.so
%{_datadir}/soletta/flow/descriptions/network.json

%files -n lib%{name}-flow-module-oic
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/oic.so
%{_datadir}/soletta/flow/descriptions/oic.json

%files -n lib%{name}-flow-module-persistence
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/persistence.so
%{_datadir}/soletta/flow/descriptions/persistence.json

%files -n lib%{name}-flow-module-piezo-speaker
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/piezo-speaker.so
%{_datadir}/soletta/flow/descriptions/piezo-speaker.json

%files -n lib%{name}-flow-module-process
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/process.so
%{_datadir}/soletta/flow/descriptions/process.json

%files -n lib%{name}-flow-module-servo-motor
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/servo-motor.so
%{_datadir}/soletta/flow/descriptions/servo-motor.json

%files -n lib%{name}-flow-module-test
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/test.so
%{_datadir}/soletta/flow/descriptions/test.json

%files -n lib%{name}-flow-module-thingspeak
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/thingspeak.so
%{_datadir}/soletta/flow/descriptions/thingspeak.json

%files -n lib%{name}-flow-module-udev
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/udev.so
%{_datadir}/soletta/flow/descriptions/udev.json

%files -n lib%{name}-flow-module-unix-socket
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow/unix-socket.so
%{_datadir}/soletta/flow/descriptions/unix-socket.json

%files -n lib%{name}-flow-metatype-module-js
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/flow-metatype/js.so

%files -n lib%{name}-linux-micro-module-bluetooth
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/bluetooth.so

%files -n lib%{name}-linux-micro-module-console
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/console.so

%files -n lib%{name}-linux-micro-module-dbus
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/dbus.so

%files -n lib%{name}-linux-micro-module-fstab
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/fstab.so

%files -n lib%{name}-linux-micro-module-hostname
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/hostname.so

%files -n lib%{name}-linux-micro-module-locale
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/locale.so

%files -n lib%{name}-linux-micro-module-machine-id
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/machine-id.so

%files -n lib%{name}-linux-micro-module-network-up
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/network-up.so

%files -n lib%{name}-linux-micro-module-rc-d
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/rc-d.so

%files -n lib%{name}-linux-micro-module-sysctl
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/sysctl.so

%files -n lib%{name}-linux-micro-module-watchdog
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/linux-micro/watchdog.so

%files -n lib%{name}-pin-mux-module-galileo
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/pin-mux/intel-galileo-rev-d.so
%{_libdir}/soletta/modules/pin-mux/intel-galileo-rev-g.so

%files -n lib%{name}-pin-mux-module-edison
%defattr(-, root, root, -)
%{_libdir}/soletta/modules/pin-mux/intel-edison-rev-c.so

# TODO: should we generate man pages from doxygen tags?
# %files -n lib%{name}-doc
# %defattr(-, root, root, -)
# %doc %{_mandir}/man3/*

%license COPYING

%changelog
* Wed Sep 16 2015 Gustavo Lima Chaves
- make debug package functional

* Tue Sep 15 2015 Gustavo Lima Chaves
- add pre-made config for Fedora 22

* Fri Sep 11 2015 Gustavo Lima Chaves
- first build for Fedora 22
