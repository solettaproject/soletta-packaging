%global soletta_major 0
%global soletta_minor 0
%global soletta_build 1
%global soletta_tag beta7

%global soletta_duktape_tag beta2
%global soletta_tinycbor_tag 0.2

Summary: A framework for making IoT devices
Name: soletta
Version: %{soletta_major}.%{soletta_minor}.%{soletta_build}
Release: 0.1.%{soletta_tag}%{?dist}
License: BSD
URL: http://github.com/solettaproject/soletta
Source0: https://github.com/solettaproject/%{name}/archive/v1_%{soletta_tag}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://github.com/solettaproject/duktape-release/archive/v1_%{soletta_duktape_tag}.tar.gz#/%{name}-duktape-%{version}.tar.gz
Source2: https://github.com/01org/tinycbor/archive/v%{soletta_tinycbor_tag}.tar.gz#/%{name}-tinycbor-%{version}.tar.gz
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: mosquitto-devel
BuildRequires: pcre-devel
BuildRequires: systemd-devel
BuildRequires: python3 >= 3.4
BuildRequires: python3-jsonschema

%description
Soletta project is a framework for making IoT devices. With Soletta
library developers can easily write software for devices that control
actuators/sensors and communicate using standard technologies. It
enables adding smartness even on the smallest edge devices.

%package %{name}-flow-module-accelerometer
Summary: Accelerometer flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-accelerometer
This package contains the accelerometer flow module for %{name}. The
module provides flow nodes for accelerometers such as ADXL345 and
LSM303DLHC.

%package %{name}-flow-module-am2315
Summary: AM2315 flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-am2315
This package contains the AM2315 flow module for %{name}. The module
provides flow nodes that output AM2315 sensor readings (temperature
and humidity).

%package %{name}-flow-module-calamari
Summary: Calamari flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-calamari
This package contains the calamari flow module for %{name}. The module
provides flow nodes for doing I/O on the Calamari board
(http://elinux.org/Calamari_Lure) components.

%package %{name}-flow-module-compass
Summary: Compass flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-compass
This package contains the compass flow module for %{name}. The module
provides a compass node that takes direction-vectors of given
accelerometer and a magnetometer nodes and outputs heading towards
Magnetic North Pole, in degrees.

%package %{name}-flow-module-evdev
Summary: Evdev flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-evdev
This package contains the evdev flow module for %{name}. The module
provides an evdev node that outputs boolean packets after evdev events
(being listened) occur.

%package %{name}-flow-module-file
Summary: File flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-file
This package contains the file flow module for %{name}. The module
provides a file node meant to read and write data to files
(asynchronously).

%package %{name}-flow-module-flower-power
Summary: Flower-power flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-flower-power
This package contains the flower-power flow module for %{name}. The
module interfaces with Parrot Flower Power
(http://www.parrot.com/usa/products/flower-power/), measuring and
analyzing the four elements crucial the health of plants: sunlight,
temperature, soil moisture and fertilizer. It fetches plant data via
HTTP, using a web service.

%package %{name}-flow-module-grove
Summary: Grove flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-grove
This package contains the grove flow module for %{name}. The module
provides flow nodes for doing I/O and package conversions for the
Grove Starter Kit
(http://www.seeedstudio.com/wiki/Grove_-_Starter_Kit_v3) components.

%package %{name}-flow-module-gtk
Summary: Gtk flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gtk3

%description %{name}-flow-module-gtk
This package contains the Gtk flow module for %{name}. The module
provides flow nodes for doing I/O of various Soletta basic packet
types, for simulation purposes. Both input and output nodes will be
Gtk UI elements.

%package %{name}-flow-module-gyroscope
Summary: Gyroscope flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-gyroscope
This package contains the gyroscope flow module for %{name}. The
module provides a flow node for the L3G4200D gyroscope.

%package %{name}-flow-module-http-client
Summary: HTTP client flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-http-client
This package contains the HTTP-client flow module for %{name}. The
module provides flow nodes that fetch and output the basic packet
types of Soletta, to be combined with the respective server nodes. It
also provides nodes that fetch arbitrary URL contents and output them
as either string or blob packets.

%if 0%{?fedora} >= 23
%package %{name}-flow-module-http-server
Summary: HTTP server flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-http-server
This package contains the HTTP-server flow module for %{name}. The
module provides flow nodes that serve the basic packet
types of Soletta, to be combined with the respective client nodes. It
also provides a node to serve static files.
%endif

%package %{name}-flow-module-iio
Summary: IIO flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-iio
This package contains the iio flow module for %{name}. The module
provides an IIO-based gyroscope input flow node. As any IIO device, it
can use a buffer to get the readings.

%package %{name}-flow-module-json
Summary: JSON flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-json
This package contains the json flow module for %{name}. The module
provides nodes to manipulate JSON packets, like retrieving arbitrary
content of the JSON object and output that in an appropriate port,
count the number of object fields, etc.

%package %{name}-flow-module-keyboard
Summary: Keyboard flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-keyboard
This package contains the keyboard flow module for %{name}. The module
provides flow nodes for keyboard input.

%package %{name}-flow-module-led-strip
Summary: Led-Strip flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-led-strip
This package contains the led-strip flow module for %{name}. The
module provides a flow node for the LPD8806 led strip controller.

%package %{name}-flow-module-location
Summary: Location flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-location
This package contains the location flow module for %{name}. The module
provides flow nodes interfacing with the free FreeGeoip service, to
obtain the location of either a given IP address or the originating
address.

%package %{name}-flow-module-magnetometer
Summary: Magnetometer flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-magnetometer
This package contains the magnetometer flow module for %{name}. The
module provides a flow node for the LSM303DLHC magnetometer.

%package %{name}-flow-module-max31855
Summary: MAX31855 flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-max31855
This package contains the MAX31855 flow module for %{name}. The module
provides a flow node for the MAX31855 temperature reader.

%package %{name}-flow-module-network
Summary: Network flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-network
This package contains the network flow module for %{name}. The module
provides a flow node that outputs boolean packets after network
connect/disconnect events occur.

%package %{name}-flow-module-oic
Summary: OIC flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-oic
This package contains the OIC flow module for %{name}. The module
provides server and client flow nodes for Open Interconnect Consortium
"brightlight" class of devices.

%package %{name}-flow-module-persistence
Summary: Persistence flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-persistence
This package contains the persistence flow module for %{name}. The
module provides flow nodes for storing/retrieving Soletta basic packet
type values on the file system or on EFI variables.

%package %{name}-flow-module-piezo-speaker
Summary: Piezo-speaker flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-piezo-speaker
This package contains the piezo-speaker flow module for %{name}. The
module provides a flow node for sound output on (PWM) piezo speakers.

%package %{name}-flow-module-process
Summary: Process flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-process
This package contains the process flow module for %{name}. The module
provides flow nodes for spawning a process and connecting its
stdin/stdout/stderr back into a flow.

%package %{name}-flow-module-servo-motor
Summary: Servo-motor flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-servo-motor
This package contains the servo-motor flow module for %{name}. The
module provides a flow node to control servo motors.

%package %{name}-flow-module-test
Summary: Test flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-test
This package contains the test flow module for %{name}. The module
provides flow nodes that aids one to write testing/validation flows
(checking for expected packet results).

%package %{name}-flow-module-thingspeak
Summary: ThingSpeak flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-thingspeak
This package contains the ThingSpeak flow module for %{name}. The
module provides flow nodes that interface with ThingSpeak -- a service
that allows publishing data via HTTP, to be consumed by IoT devices.
To use these nodes, one must register and obtain an API key. API keys
for channels and talkbacks are different. For the talkback feature,
obtaining a Talkback ID is also required.

%package %{name}-flow-module-udev
Summary: Udev flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: udev

%description %{name}-flow-module-udev
This package contains the udev flow module for %{name}. The module
provides a udev flow node that outputs boolean packets after a devices
are attached or detached on the system.

%package %{name}-flow-module-unix-socket
Summary: Unix-socket flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-module-unix-socket
This package contains the unix-socket flow module for %{name}. The
module provides I/O flow nodes that aid on isolating flows by means of
unix sockets.

%package %{name}-flow-metatype-module-js
Summary: JavaScript flow metatype module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-flow-metatype-module-js
This package contains the JavaScript flow metatype module for %{name}.
The module a JavaScript metatype for flows, i. e., the possibility of
declaring new node types with the behavior implemented in that
language, directly in .fbp files.

%package %{name}-pin-mux-module-galileo
Summary: Galileo pin-mux module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-pin-mux-module-galileo
This package contains the galileo pin-mux module for %{name}. The
module provides pin multiplexing rules/mapping for Galileo boards
(revisions D ang G). Without this module, to use Galileo I/O pins with
the desired function, one would have to setup them on their own
beforehand.

%package %{name}-pin-mux-module-edison
Summary: Edison pin-mux module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description %{name}-pin-mux-module-edison
This package contains the edison pin-mux module for %{name}. The
module provides pin multiplexing rules/mapping for Edison boards
(revision C). Without this module, to use Edison I/O pins with the
desired function, one would have to setup them on their own
beforehand.

%package %{name}-devel
Summary: Header files, libraries and development documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3 >= 3.4

%description %{name}-devel
This package contains the header files, static libraries and
development documentation for %{name}. If you like to develop programs
using %{name}, you will need to install %{name}-devel.

# Docs disabled for now because the man-formatted output is not even
# being created yet

# %%package %%{name}-doc
# Summary: Development documentation for %%{name}

# %%description %%{name}-doc
# This package contains the development documentation for %%{name}.

%prep
%setup -qn %{name}-1_%{soletta_tag}
%setup -T -D -a 1 -qn %{name}-1_%{soletta_tag}
%setup -T -D -a 2 -qn %{name}-1_%{soletta_tag}
mv duktape-release-1_%{soletta_duktape_tag}/* src/thirdparty/duktape
mv tinycbor-%{soletta_tinycbor_tag}/* src/thirdparty/tinycbor

%build
export LIBDIR=%{_libdir}/
make alldefconfig
sed -i 's/CONFIG_CFLAGS=\"\"/CONFIG_CFLAGS=\"-g\"/g' .config
sed -i 's/_SAMPLES=y/_SAMPLES=n/g' .config
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags}

%install
export LIBDIR=%{_libdir}/
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install

%check
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} check
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} check-fbp
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} check-fbp-bin
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} check-stub

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%{?%{name}_debug_package}

%files
%{_libdir}/libsoletta.so.%{soletta_major}
%{_libdir}/libsoletta.so.%{version}
%{_bindir}/sol-fbp-runner
%dir %{_datadir}/soletta
%{_datadir}/soletta/board_detect.json
%dir %{_libdir}/soletta
%dir %{_libdir}/soletta/modules
%dir %{_libdir}/soletta/modules/flow
%dir %{_libdir}/soletta/modules/flow-metatype
%dir %{_libdir}/soletta/modules/pin-mux
%if 0%{?fedora} < 23
%dir %{_libdir}/soletta/modules/linux-micro
%{_libdir}/soletta/modules/linux-micro/initial-services
%{_libdir}/soletta/modules/linux-micro/bluetooth.so
%{_libdir}/soletta/modules/linux-micro/console.so
%{_libdir}/soletta/modules/linux-micro/dbus.so
%{_libdir}/soletta/modules/linux-micro/fstab.so
%{_libdir}/soletta/modules/linux-micro/hostname.so
%{_libdir}/soletta/modules/linux-micro/locale.so
%{_libdir}/soletta/modules/linux-micro/machine-id.so
%{_libdir}/soletta/modules/linux-micro/network-up.so
%{_libdir}/soletta/modules/linux-micro/rc-d.so
%{_libdir}/soletta/modules/linux-micro/sysctl.so
%{_libdir}/soletta/modules/linux-micro/watchdog.so
%endif

%license COPYING

%files %{name}-devel
%{_libdir}/libsoletta.so
%{_bindir}/sol-fbp-generator
%{_bindir}/sol-fbp-to-dot
%{_bindir}/sol-flow-node-type-gen.py
%{_bindir}/sol-flow-node-type-validate.py
%{_bindir}/sol-flow-node-types
%{_bindir}/sol-oic-gen.py
%dir %{_datadir}/soletta/flow
%dir %{_datadir}/soletta/flow/descriptions
%dir %{_datadir}/soletta/flow/schemas
%dir %{_includedir}/soletta
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

%files %{name}-flow-module-accelerometer
%{_libdir}/soletta/modules/flow/accelerometer.so
%{_datadir}/soletta/flow/descriptions/accelerometer.json

%files %{name}-flow-module-am2315
%{_libdir}/soletta/modules/flow/am2315.so
%{_datadir}/soletta/flow/descriptions/am2315.json

%files %{name}-flow-module-calamari
%{_libdir}/soletta/modules/flow/calamari.so
%{_datadir}/soletta/flow/descriptions/calamari.json

%files %{name}-flow-module-compass
%{_libdir}/soletta/modules/flow/compass.so
%{_datadir}/soletta/flow/descriptions/compass.json

%files %{name}-flow-module-evdev
%{_libdir}/soletta/modules/flow/evdev.so
%{_datadir}/soletta/flow/descriptions/evdev.json

%files %{name}-flow-module-file
%{_libdir}/soletta/modules/flow/file.so
%{_datadir}/soletta/flow/descriptions/file.json

%files %{name}-flow-module-flower-power
%{_libdir}/soletta/modules/flow/flower-power.so
%{_datadir}/soletta/flow/descriptions/flower-power.json

%files %{name}-flow-module-grove
%{_libdir}/soletta/modules/flow/grove.so
%{_datadir}/soletta/flow/descriptions/grove.json

%files %{name}-flow-module-gtk
%{_libdir}/soletta/modules/flow/gtk.so
%{_datadir}/soletta/flow/descriptions/gtk.json

%files %{name}-flow-module-gyroscope
%{_libdir}/soletta/modules/flow/gyroscope.so
%{_datadir}/soletta/flow/descriptions/gyroscope.json

%files %{name}-flow-module-http-client
%{_libdir}/soletta/modules/flow/http-client.so
%{_datadir}/soletta/flow/descriptions/http-client.json

%if 0%{?fedora} >= 23
%files %{name}-flow-module-http-server
%{_libdir}/soletta/modules/flow/http-server.so
%{_datadir}/soletta/flow/descriptions/http-server.json
%endif

%files %{name}-flow-module-iio
%{_libdir}/soletta/modules/flow/iio.so
%{_datadir}/soletta/flow/descriptions/iio.json

%files %{name}-flow-module-json
%{_libdir}/soletta/modules/flow/json.so
%{_datadir}/soletta/flow/descriptions/json.json

%files %{name}-flow-module-keyboard
%{_libdir}/soletta/modules/flow/keyboard.so
%{_datadir}/soletta/flow/descriptions/keyboard.json

%files %{name}-flow-module-led-strip
%{_libdir}/soletta/modules/flow/led-strip.so
%{_datadir}/soletta/flow/descriptions/led-strip.json

%files %{name}-flow-module-location
%{_libdir}/soletta/modules/flow/location.so
%{_datadir}/soletta/flow/descriptions/location.json

%files %{name}-flow-module-magnetometer
%{_libdir}/soletta/modules/flow/magnetometer.so
%{_datadir}/soletta/flow/descriptions/magnetometer.json

%files %{name}-flow-module-max31855
%{_libdir}/soletta/modules/flow/max31855.so
%{_datadir}/soletta/flow/descriptions/max31855.json

%files %{name}-flow-module-network
%{_libdir}/soletta/modules/flow/network.so
%{_datadir}/soletta/flow/descriptions/network.json

%files %{name}-flow-module-oic
%{_libdir}/soletta/modules/flow/oic.so
%{_datadir}/soletta/flow/descriptions/oic.json

%files %{name}-flow-module-persistence
%{_libdir}/soletta/modules/flow/persistence.so
%{_datadir}/soletta/flow/descriptions/persistence.json

%files %{name}-flow-module-piezo-speaker
%{_libdir}/soletta/modules/flow/piezo-speaker.so
%{_datadir}/soletta/flow/descriptions/piezo-speaker.json

%files %{name}-flow-module-process
%{_libdir}/soletta/modules/flow/process.so
%{_datadir}/soletta/flow/descriptions/process.json

%files %{name}-flow-module-servo-motor
%{_libdir}/soletta/modules/flow/servo-motor.so
%{_datadir}/soletta/flow/descriptions/servo-motor.json

%files %{name}-flow-module-test
%{_libdir}/soletta/modules/flow/test.so
%{_datadir}/soletta/flow/descriptions/test.json

%files %{name}-flow-module-thingspeak
%{_libdir}/soletta/modules/flow/thingspeak.so
%{_datadir}/soletta/flow/descriptions/thingspeak.json

%files %{name}-flow-module-udev
%{_libdir}/soletta/modules/flow/udev.so
%{_datadir}/soletta/flow/descriptions/udev.json

%files %{name}-flow-module-unix-socket
%{_libdir}/soletta/modules/flow/unix-socket.so
%{_datadir}/soletta/flow/descriptions/unix-socket.json

%files %{name}-flow-metatype-module-js
%{_libdir}/soletta/modules/flow-metatype/js.so

%files %{name}-pin-mux-module-galileo
%{_libdir}/soletta/modules/pin-mux/intel-galileo-rev-d.so
%{_libdir}/soletta/modules/pin-mux/intel-galileo-rev-g.so

%files %{name}-pin-mux-module-edison
%{_libdir}/soletta/modules/pin-mux/intel-edison-rev-c.so

# TODO: should we generate man pages from doxygen tags?
# %%files %%{name}-doc
# %%doc %%{_mandir}/man3/*

%changelog
* Fri Oct 16 2015 Gustavo Lima Chaves <gustavo.lima.chaves@intel.com> - 0.0.1-beta7
- first build for Fedora 22
