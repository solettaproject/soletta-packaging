%global soletta_version 1
%global soletta_current 1
%global soletta_revision 0
%global soletta_age 0

%global soletta_major %(echo $(( %{soletta_current} - %{soletta_age} )))
%global soletta_minor %{soletta_age}
%global soletta_release %{soletta_revision}

%global soletta_duktape_version 1.4.0
%global soletta_mavlink_version 1.0.11
%global soletta_tinycbor_version 0.2
%global soletta_tinydtls_version 0.8.1

Summary: A framework for making IoT devices
Name: soletta
Version: %{soletta_version}
Release: 3%{?dist}
# Apache License (ASL):
#       data/*
#       doc/*
#       src/*
#       tools/*  (exceptions below)
# BSD 2-Clause:
#       src/thirdparty/oic-data-models/*
# MIT:
#       src/thirdparty/duktape/*
#       src/thirdparty/tinycbor/*
#       src/thirdparty/tinydtls/*
#       doc/node-types-html/css/jquery-ui.min.css
#       doc/node-types-html/js/frameworks/* (exceptions below)
# LGPL:
#       src/thirdparty/mavlink/*
# GPL:
#       tools/kconfig/*
#       doc/node-types-html/js/frameworks/isotope.pkgd.min.js
# Python License:
#       src/modules/flow/format/string-format.c
#       src/modules/flow/string/string-replace-ascii.c
#       src/modules/flow/string/string-replace-icu.c
License: ASL 2.0 and BSD and MIT and LGPLv2+ and GPLv2+ and Python
URL: http://github.com/solettaproject/soletta
Source0: https://github.com/solettaproject/%{name}/releases/download/v1/%{name}.tar.gz
Provides: bundled(duktape) = %{soletta_duktape_version}
Provides: bundled(mavlink) = %{soletta_mavlink_version}
Provides: bundled(tinycbor) = %{soletta_tinycbor_version}
Provides: bundled(tinydtls) = %{soletta_tinydtls_version}
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
# We need libmicrohttpd >= 0.9.47, actually, but v1 went out without
# this check. Let's build with it only for future (distro) releases,
# then
%if 0%{?fedora} > 26
BuildRequires: libmicrohttpd-devel
%endif
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

%package flow-module-am2315
Summary: AM2315 flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-am2315
This package contains the AM2315 flow module for %{name}. The module
provides flow nodes that output AM2315 sensor readings (temperature
and humidity).

%package flow-module-calamari
Summary: Calamari flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-calamari
This package contains the calamari flow module for %{name}. The module
provides flow nodes for doing I/O on the Calamari board
(http://elinux.org/Calamari_Lure) components.

%package flow-module-compass
Summary: Compass flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-compass
This package contains the compass flow module for %{name}. The module
provides a compass node that takes direction-vectors of given
accelerometer and a magnetometer nodes and outputs heading towards
Magnetic North Pole, in degrees.

%package flow-module-evdev
Summary: Evdev flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-evdev
This package contains the evdev flow module for %{name}. The module
provides an evdev node that outputs boolean packets after evdev events
(being listened) occur.

%package flow-module-file
Summary: File flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-file
This package contains the file flow module for %{name}. The module
provides a file node meant to read and write data to files
(asynchronously).

%package flow-module-flower-power
Summary: Flower-power flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-flower-power
This package contains the flower-power flow module for %{name}. The
module interfaces with Parrot Flower Power
(http://www.parrot.com/usa/products/flower-power/), measuring and
analyzing the four elements crucial the health of plants: sunlight,
temperature, soil moisture and fertilizer. It fetches plant data via
HTTP, using a web service.

%package flow-module-form
Summary: Form flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-form
This package contains the form flow module for %{name}. The module
provides nodes producing formatted, string output to feed LCD
displays, getting input from buttons.

%package flow-module-format
Summary: Format flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-format
This package contains the format flow module for %{name}. The module
aggregates those nodes that make use of Python string-formatting code.

%package flow-module-grove
Summary: Grove flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-grove
This package contains the grove flow module for %{name}. The module
provides flow nodes for doing I/O and package conversions for the
Grove Starter Kit
(http://www.seeedstudio.com/wiki/Grove_-_Starter_Kit_v3) components.

%package flow-module-gtk
Summary: Gtk flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gtk3

%description flow-module-gtk
This package contains the Gtk flow module for %{name}. The module
provides flow nodes for doing I/O of various Soletta basic packet
types, for simulation purposes. Both input and output nodes will be
Gtk UI elements.

%package flow-module-http-client
Summary: HTTP client flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-http-client
This package contains the HTTP-client flow module for %{name}. The
module provides flow nodes that fetch and output the basic packet
types of Soletta, to be combined with the respective server nodes. It
also provides nodes that fetch arbitrary URL contents and output them
as either string or blob packets.

%if 0%{?fedora} > 26
%package flow-module-http-server
Summary: HTTP server flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-http-server
This package contains the HTTP-server flow module for %{name}. The
module provides flow nodes that serve the basic packet
types of Soletta, to be combined with the respective client nodes. It
also provides a node to serve static files.
%endif

%package flow-module-iio
Summary: IIO flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-iio
This package contains the iio flow module for %{name}. The module
provides an IIO-based gyroscope input flow node. As any IIO device, it
can use a buffer to get the readings.

%package flow-module-json
Summary: JSON flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-json
This package contains the json flow module for %{name}. The module
provides nodes to manipulate JSON packets, like retrieving arbitrary
content of the JSON object and output that in an appropriate port,
count the number of object fields, etc.

%package flow-module-jhd1313m1
Summary: JHD1313M1 flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-jhd1313m1
This package contains the JHD1313M1 flow module for %{name}. The
module provides nodes giving output to Grove-kit LCD controller
(JHD1313M1 model), for simple string displaying and backlight color
setting.

%package flow-module-keyboard
Summary: Keyboard flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-keyboard
This package contains the keyboard flow module for %{name}. The module
provides flow nodes for keyboard input.

%package flow-module-mqtt
Summary: MQTT flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-mqtt
This package contains the mqtt flow module for %{name}. The module
provides a flow node implementing a MQTT client.

# We depend on http-server for the oauth node
%if 0%{?fedora} > 26
%package flow-module-oauth
Summary: OAuth flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-oauth
This package contains the oauth flow module for %{name}. The module
provides a flow nodes to negotiate an OAuth access token.
%endif

%package flow-module-power-supply
Summary: Power supply flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-power-supply
This package contains the power supply flow module for %{name}. The
module provides flow nodes to list and query information from all
power supplies of the system.

%package flow-module-led-strip
Summary: Led-Strip flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-led-strip
This package contains the led-strip flow module for %{name}. The
module provides a flow node for the LPD8806 led strip controller.

%package flow-module-location
Summary: Location flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-location
This package contains the location flow module for %{name}. The module
provides flow nodes interfacing with the free FreeGeoip service, to
obtain the location of either a given IP address or the originating
address.

%package flow-module-network
Summary: Network flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-network
This package contains the network flow module for %{name}. The module
provides a flow node that outputs boolean packets after network
connect/disconnect events occur.

%package flow-module-oic
Summary: OIC flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-oic
This package contains the OIC flow module for %{name}. The module
provides server and client flow nodes for all Open Interconnect
Consortium classes of devices.

%package flow-module-persistence
Summary: Persistence flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-persistence
This package contains the persistence flow module for %{name}. The
module provides flow nodes for storing/retrieving Soletta basic packet
type values on the file system or on EFI variables.

%package flow-module-piezo-speaker
Summary: Piezo-speaker flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-piezo-speaker
This package contains the piezo-speaker flow module for %{name}. The
module provides a flow node for sound output on (PWM) piezo speakers.

%package flow-module-process
Summary: Process flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-process
This package contains the process flow module for %{name}. The module
provides flow nodes for spawning a process and connecting its
stdin/stdout/stderr back into a flow.

%package flow-module-servo-motor
Summary: Servo-motor flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-servo-motor
This package contains the servo-motor flow module for %{name}. The
module provides a flow node to control servo motors.

%package flow-module-test
Summary: Test flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-test
This package contains the test flow module for %{name}. The module
provides flow nodes that aids one to write testing/validation flows
(checking for expected packet results).

%package flow-module-thingspeak
Summary: ThingSpeak flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-thingspeak
This package contains the ThingSpeak flow module for %{name}. The
module provides flow nodes that interface with ThingSpeak -- a service
that allows publishing data via HTTP, to be consumed by IoT devices.
To use these nodes, one must register and obtain an API key. API keys
for channels and talkbacks are different. For the talkback feature,
obtaining a Talkback ID is also required.

%package flow-module-udev
Summary: Udev flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: udev

%description flow-module-udev
This package contains the udev flow module for %{name}. The module
provides a udev flow node that outputs boolean packets after a devices
are attached or detached on the system.

%package flow-module-unix-socket
Summary: Unix-socket flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-unix-socket
This package contains the unix-socket flow module for %{name}. The
module provides I/O flow nodes that aid on isolating flows by means of
unix sockets.

%package flow-module-update
Summary: Update flow module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-module-update
This package contains the update flow module for %{name}. The module
provides flow nodes that assist on checking availability of, fetching
and installing Soletta-application updates.

%package flow-metatype-module-js
Summary: JavaScript flow metatype module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-metatype-module-js
This package contains the JavaScript flow metatype module for %{name}.
The module a JavaScript metatype for flows, i. e., the possibility of
declaring new node types with the behavior implemented in that
language, directly in .fbp files.

%package flow-metatype-module-http-composed-client
Summary: HTTP-composed-packets flow metatype module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-metatype-module-http-composed-client
This package contains the HTTP-composed-packets flow metatype module
for %{name}. The module allows creating HTTP client node types using
composed packets.

%if 0%{?fedora} > 26
%package flow-metatype-module-http-composed-server
Summary: HTTP-composed-packets flow metatype module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description flow-metatype-module-http-composed-server
This package contains the HTTP-composed-packets flow metatype module
for %{name}. The module allows creating HTTP server node types using
composed packets.
%endif

%package pin-mux-module-galileo
Summary: Galileo pin-mux module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description pin-mux-module-galileo
This package contains the galileo pin-mux module for %{name}. The
module provides pin multiplexing rules/mapping for Galileo boards (all
revisions). Without this module, to use Galileo I/O pins with the
desired function, one would have to setup them on their own
beforehand.

%package pin-mux-module-edison
Summary: Edison pin-mux module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description pin-mux-module-edison
This package contains the edison pin-mux module for %{name}. The
module provides pin multiplexing rules/mapping for Edison boards
(revision C). Without this module, to use Edison I/O pins with the
desired function, one would have to setup them on their own
beforehand.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3 >= 3.4

%description devel
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
%setup -qn %{name}

%build
export LIBDIR=%{_libdir}/
%if 0%{?fedora} <= 26
# we gotta wait for v2 for this line to be unnecessary -- avoid a
# broken http-server for now
sed -i 's/\"atleast-version\": \"0\.9\.43\"/\"atleast-version\": \"0\.9\.47\"/g' ./data/jsons/dependencies.json
%endif

make alldefconfig
sed -i 's/CONFIG_CFLAGS=\"\"/CONFIG_CFLAGS=\"-g\"/g' .config
sed -i 's/_SAMPLES=y/_SAMPLES=n/g' .config
sed -i 's/RPATH=y/RPATH=n/g' .config

%if 0%{?fedora} <= 26
# Don't bother testing http-server (oauth only on samples for now) if
# we won't build it
find ./src/test-fbp/ -type f -print0 | xargs -0 grep -l "http-server" | xargs rm
# javascript.fbp will go away with the line above, so...
sed -i '/tests-fbp-bin += $(top_srcdir)src\/test-fbp\/javascript\.fbp/d' ./tools/build/Makefile.vars
%endif
make V=1 CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags}

%install
export LIBDIR=%{_libdir}/
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} DESTDIR=%{buildroot} INSTALL="install -p" install

%check
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} check
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} check-fbp
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} check-fbp-bin
make CFLAGS="$CFLAGS %optflags" LDFLAGS="$LDFLAGS %__global_ldflags" %{?_smp_mflags} check-stub

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
# Apache License
%{_libdir}/libsoletta.so.%{soletta_major}
%{_libdir}/libsoletta.so.%{soletta_major}.%{soletta_minor}.%{soletta_release}
%{_bindir}/sol-fbp-runner
%dir %{_datadir}/soletta/
%dir %{_datadir}/soletta/boards
%{_datadir}/soletta/boards/50-default.json
%dir %{_datadir}/soletta/flow/aliases
%{_datadir}/soletta/flow/aliases/50-default.json
%dir %{_libdir}/soletta/
%dir %{_libdir}/soletta/modules/
%dir %{_libdir}/soletta/modules/flow/
%dir %{_libdir}/soletta/modules/flow-metatype/
%dir %{_libdir}/soletta/modules/pin-mux/
%dir %{_datadir}/soletta/flow/
%dir %{_datadir}/soletta/flow/descriptions/
%dir %{_datadir}/soletta/flow/schemas/

%license COPYING

%files devel
# Apache License
%{_libdir}/libsoletta.so
%{_bindir}/sol-aio
%{_bindir}/sol-fbp-generator
%{_bindir}/sol-fbp-to-dot
%{_bindir}/sol-flow-node-type-aliases-gen.py
%{_bindir}/sol-flow-node-type-gen.py
%{_bindir}/sol-flow-node-type-validate.py
%{_bindir}/sol-gpio
%{_bindir}/sol-oic-gen.py
%{_includedir}/soletta/
%{_datadir}/gdb/auto-load/*
%{_libdir}/pkgconfig/soletta.pc
%dir %{_datadir}/soletta/flow/descriptions
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
%{_datadir}/soletta/flow/descriptions/regexp.json
%{_datadir}/soletta/flow/descriptions/string.json
%{_datadir}/soletta/flow/descriptions/switcher.json
%{_datadir}/soletta/flow/descriptions/temperature.json
%{_datadir}/soletta/flow/descriptions/timer.json
%{_datadir}/soletta/flow/descriptions/timestamp.json
%{_datadir}/soletta/flow/descriptions/trigonometry.json
%{_datadir}/soletta/flow/descriptions/wallclock.json
%dir %{_datadir}/soletta/flow/schemas
%{_datadir}/soletta/flow/schemas/node-type-genspec.schema

%files flow-module-am2315
# Apache License
%{_libdir}/soletta/modules/flow/am2315.so
%{_datadir}/soletta/flow/descriptions/am2315.json

%files flow-module-calamari
# Apache License
%{_libdir}/soletta/modules/flow/calamari.so
%{_datadir}/soletta/flow/descriptions/calamari.json

%files flow-module-compass
# Apache License
%{_libdir}/soletta/modules/flow/compass.so
%{_datadir}/soletta/flow/descriptions/compass.json

%files flow-module-evdev
# Apache License
%{_libdir}/soletta/modules/flow/evdev.so
%{_datadir}/soletta/flow/descriptions/evdev.json

%files flow-module-file
# Apache License
%{_libdir}/soletta/modules/flow/file.so
%{_datadir}/soletta/flow/descriptions/file.json

%files flow-module-flower-power
# Apache License
%{_libdir}/soletta/modules/flow/flower-power.so
%{_datadir}/soletta/flow/descriptions/flower-power.json

%files flow-module-form
# Apache License
%{_libdir}/soletta/modules/flow/form.so
%{_datadir}/soletta/flow/descriptions/form.json

%files flow-module-format
# Apache License
%{_libdir}/soletta/modules/flow/format.so
%{_datadir}/soletta/flow/descriptions/format.json

%files flow-module-grove
# Apache License
%{_libdir}/soletta/modules/flow/grove.so
%{_datadir}/soletta/flow/descriptions/grove.json

%files flow-module-gtk
# Apache License
%{_libdir}/soletta/modules/flow/gtk.so
%{_datadir}/soletta/flow/descriptions/gtk.json

%files flow-module-http-client
# Apache License
%{_libdir}/soletta/modules/flow/http-client.so
%{_datadir}/soletta/flow/descriptions/http-client.json

%if 0%{?fedora} > 26
%files flow-module-http-server
# Apache License
%{_libdir}/soletta/modules/flow/http-server.so
%{_datadir}/soletta/flow/descriptions/http-server.json
%endif

%files flow-module-iio
# Apache License
%{_libdir}/soletta/modules/flow/iio.so
%{_datadir}/soletta/flow/descriptions/iio.json

%files flow-module-json
# Apache License
%{_libdir}/soletta/modules/flow/json.so
%{_datadir}/soletta/flow/descriptions/json.json

%files flow-module-jhd1313m1
# Apache License
%{_libdir}/soletta/modules/flow/jhd1313m1.so
%{_datadir}/soletta/flow/descriptions/jhd1313m1.json

%files flow-module-keyboard
# Apache License
%{_libdir}/soletta/modules/flow/keyboard.so
%{_datadir}/soletta/flow/descriptions/keyboard.json

%files flow-module-mqtt
# Apache License
%{_libdir}/soletta/modules/flow/mqtt.so
%{_datadir}/soletta/flow/descriptions/mqtt.json

%if 0%{?fedora} > 26
%files flow-module-oauth
# Apache License
%{_libdir}/soletta/modules/flow/oauth.so
%{_datadir}/soletta/flow/descriptions/oauth.json
%endif

%files flow-module-power-supply
# Apache License
%{_libdir}/soletta/modules/flow/power-supply.so
%{_datadir}/soletta/flow/descriptions/power-supply.json

%files flow-module-led-strip
# Apache License
%{_libdir}/soletta/modules/flow/led-strip.so
%{_datadir}/soletta/flow/descriptions/led-strip.json

%files flow-module-location
# Apache License
%{_libdir}/soletta/modules/flow/location.so
%{_datadir}/soletta/flow/descriptions/location.json

%files flow-module-network
# Apache License
%{_libdir}/soletta/modules/flow/network.so
%{_datadir}/soletta/flow/descriptions/network.json

%files flow-module-oic
# Apache License
%{_libdir}/soletta/modules/flow/oic.so
%{_datadir}/soletta/flow/descriptions/oic.json

%files flow-module-persistence
# Apache License
%{_libdir}/soletta/modules/flow/persistence.so
%{_datadir}/soletta/flow/descriptions/persistence.json

%files flow-module-piezo-speaker
# Apache License
%{_libdir}/soletta/modules/flow/piezo-speaker.so
%{_datadir}/soletta/flow/descriptions/piezo-speaker.json

%files flow-module-process
# Apache License
%{_libdir}/soletta/modules/flow/process.so
%{_datadir}/soletta/flow/descriptions/process.json

%files flow-module-servo-motor
# Apache License
%{_libdir}/soletta/modules/flow/servo-motor.so
%{_datadir}/soletta/flow/descriptions/servo-motor.json

%files flow-module-test
# Apache License
%{_libdir}/soletta/modules/flow/test.so
%{_datadir}/soletta/flow/descriptions/test.json

%files flow-module-thingspeak
# Apache License
%{_libdir}/soletta/modules/flow/thingspeak.so
%{_datadir}/soletta/flow/descriptions/thingspeak.json

%files flow-module-udev
# Apache License
%{_libdir}/soletta/modules/flow/udev.so
%{_datadir}/soletta/flow/descriptions/udev.json

%files flow-module-unix-socket
# Apache License
%{_libdir}/soletta/modules/flow/unix-socket.so
%{_datadir}/soletta/flow/descriptions/unix-socket.json

%files flow-module-update
# Apache License
%{_libdir}/soletta/modules/flow/update.so
%{_datadir}/soletta/flow/descriptions/update.json

%files flow-metatype-module-js
# Apache License
%{_libdir}/soletta/modules/flow-metatype/js.so

%files flow-metatype-module-http-composed-client
# Apache License
%{_libdir}/soletta/modules/flow-metatype/http-composed-client.so

%if 0%{?fedora} > 26
%files flow-metatype-module-http-composed-server
# Apache License
%{_libdir}/soletta/modules/flow-metatype/http-composed-server.so
%endif

%files pin-mux-module-galileo
# Apache License
%{_libdir}/soletta/modules/pin-mux/intel-galileo-rev-d.so
%{_libdir}/soletta/modules/pin-mux/intel-galileo-rev-g.so

%files pin-mux-module-edison
# Apache License
%{_libdir}/soletta/modules/pin-mux/intel-edison-rev-c.so

# TODO: should we generate man pages from doxygen tags?
# %%files %%{name}-doc
# %%doc %%{_mandir}/man3/*

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1-2
- Rebuild for Python 3.6

* Wed Aug 03 2016 Gustavo Lima Chaves <gustavo.lima.chaves@intel.com> - 1-1
- mavlink support added
- many IIO node types added
- Some fixes on I/O implementations
- Improvement on sockets API
- Light sensor category added to Linux IIO
- Added support to STTS751 temperature sensor
- LWM2M protocol support added
- Increased amount of node types supported by GTK (simulation)
- Reduced memory consumption by CoAP - LWM2M samples are running fine on RIOT
- Single node support - so it’s possible to have a single node without
  an associated flow. Useful when you need to access a component, send
  packets to its input ports manually and be notified when it’s
  sending packets on its output ports.
- Fixes on HTTP implementation regarding IPv6
- RGB and direction-vector persistence nodes created
- Added support for secure OIC connections using pre shared certs
- Added web inspector to sol-fbp-runner
- Added API to server side events on http-server with samples. It was
  supported on http-client as well.
- Provide node types for a lot of OIC resources data models
- Make OIC device IDs and resource structure compatible with IoTivity 1.1 RC3
- Add simple JSON types as HTTP node types
- LWM2M bootstrap interface implemented
- Connections management support (sol-netctl)
- Introduced sol-bluetooth and sol-gatt API
- Support to node type aliases
- A couple tools were created to help debugging I/O (sol-aio and sol-gpio)
- Node types related to robotics were added

* Wed Dec 02 2015 Gustavo Lima Chaves <gustavo.lima.chaves@intel.com> - 0.0.1.beta13-1
- New nodes were added -- http-client/request, http-client/get-json,
  http-client/create-url, oauth/v1, json/create-array-path,
  json/create-object-path, power-supply/get-list,
  power-supply/get-capacity, power-supply/get-info, mqtt/client,
  update/check, update/fetch, update/install.
- HTTP server node was removed from the package on Fedora 23, since it
  demands a much newer version of libmicrohttpd than Fedora provides
  (and will ever provide at least on Fedora 23, since systemd also
  depends on it and newer versions change the soname).
- A new packet types was added -- HTTP response.
- Board pins can now be addressed by a string label, if backed-up by
  their pin-mux modules.
- The form family of nodes got a handful of other nodes included:
  form/int, form/int-custom, form/string.
- OIC client nodes got a new SCAN port, meant to request scanning of
  all servers matching the client interface. A new DEVICE_ID output
  port was also added, that will dispatch the found IDs in that
  scanning request.
- The platform modules got a new mount points manipulation API, as
  well as a uevent listening one (for Linux).
- An API exposing power supply properties was added to Soletta.
- An API dealing with certificates was added to Soletta.
- MQTT in Soletta got TLS connections support.
- JavaScript code on FBP files now recognize all Soletta package
  types.
- A new root module was added to Soletta: update. It controls how
  Soletta apps will be updated.

* Mon Oct 26 2015 Gustavo Lima Chaves <gustavo.lima.chaves@intel.com> - 0.0.1.beta10-1
- Bump Soletta version to 0.0.1.beta10
- Fix RPM spec to sign bundled packages tinycbor and duktape
- Fix RPM package naming
- Add new flow-module: form
- The json module got a ton of new features and nodes
- string/concatenate node now supports mulitple inputs (up to 23)
- and/or logic nodes now accept multiple (up to 32) input connections
- The int module nodes now send new output packets on input changes
- Multicast packets are now sent to all machine interfaces
- The form module got a new node: the boolean form.

* Tue Oct 20 2015 Gustavo Lima Chaves <gustavo.lima.chaves@intel.com> - 0.0.1.beta8-1
- first rpm build
