Name:           oobattery
Version:        0.2.0
Release:        1%{?dist}
Summary:        Reads ACPI battery charge level, energy consumption rate, and health condition.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobattery
Source0:        oobattery-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobattery is a sovereign, capability-bounded BATTERY MONITOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobattery
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobattery-uninstall

%files
/usr/bin/oobattery
/usr/bin/oobattery-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign pure openOODA implementation
