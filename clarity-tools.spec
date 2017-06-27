Summary: A collection of extra tools for the Clarity
Name: clarity-extratools
Version: 12
Release: 0
License: GPLv2, GPLv2+, ASL 2.0
Source: %{name}-%{version}.tar.gz
Group: Development/Tools
Packager: Insignary Inc <tech@insignary.com>
BuildRequires: xz-devel, lzo-devel, zlib-devel, make, gcc-c++
Requires: lzo, xz-libs, lz4, zlib

%description
A collection of extra tools for the Clarity, scraped from GPL source code releases and firmware replacement projects, plus projects.

%prep
%setup -q
%build
make
%install
rm -rf $RPM_BUILD_ROOT
install -D -p -m 755 cramfs/disk-utils/clarity-fsck.cramfs $RPM_BUILD_ROOT%{_bindir}/clarity-fsck.cramfs
install -D -p -m 755 squashfs4.3/squashfs-tools/clarity-unsquashfs43 $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs43
install -D -p -m 755 squashfs-atheros/squashfs3.3/squashfs-tools/clarity-unsquashfs-atheros $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-atheros
install -D -p -m 755 squashfs-atheros2/clarity-unsquashfs-atheros2 $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-atheros2
install -D -p -m 755 squashfs-atheros4.0/squashfs-tools/clarity-unsquashfs-atheros40 $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-atheros40
install -D -p -m 755 squashfs-broadcom/clarity-unsquashfs-broadcom $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-broadcom
install -D -p -m 755 squashfs-broadcom40/squashfs_4.0/clarity-unsquashfs-broadcom40 $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-broadcom40
install -D -p -m 755 squashfs-openwrt/clarity-unsquashfs-openwrt $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-openwrt
install -D -p -m 755 squashfs-ddwrt/clarity-unsquashfs-ddwrt $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-ddwrt
install -D -p -m 755 squashfs-ralink/squashfs3.2-r2/squashfs-tools/clarity-unsquashfs-ralink $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-ralink
install -D -p -m 755 squashfs-realtek/squashfs-tools/clarity-unsquashfs-realtek $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-realtek
#install -D -p -m 755 squashfs-realtek2/squashfs-2.1-r2/clarity-unsquashfs-realtek2 $RPM_BUILD_ROOT%{_bindir}/clarity-unsquashfs-realtek2
install -D -p -m 755 unyaffs/clarity-unyaffs $RPM_BUILD_ROOT%{_bindir}/clarity-unyaffs
install -D -p -m 755 romfsck/clarity-romfsck $RPM_BUILD_ROOT%{_bindir}/clarity-romfsck
install -D -p -m 755 code2html-0.9.1/clarity-code2html $RPM_BUILD_ROOT%{_bindir}/clarity-code2html
install -D -p -m 755 clarity-minix/clarity-minix $RPM_BUILD_ROOT%{_bindir}/clarity-minix
install -D -p -m 755 simg2img/clarity-simg2img $RPM_BUILD_ROOT%{_bindir}/clarity-simg2img
install -D -p -m 755 mkboot/mkboot $RPM_BUILD_ROOT%{_bindir}/mkboot
%files
%{_bindir}/clarity-unsquashfs43
%{_bindir}/clarity-unsquashfs-atheros
%{_bindir}/clarity-unsquashfs-atheros2
%{_bindir}/clarity-unsquashfs-atheros40
%{_bindir}/clarity-unsquashfs-broadcom
%{_bindir}/clarity-unsquashfs-broadcom40
%{_bindir}/clarity-unsquashfs-openwrt
%{_bindir}/clarity-unsquashfs-ddwrt
%{_bindir}/clarity-unsquashfs-ralink
%{_bindir}/clarity-unsquashfs-realtek
#%{_bindir}/clarity-unsquashfs-realtek2
%{_bindir}/clarity-fsck.cramfs
%{_bindir}/clarity-unyaffs
%{_bindir}/clarity-romfsck
%{_bindir}/clarity-code2html
%{_bindir}/clarity-minix
%{_bindir}/clarity-simg2img
%{_bindir}/mkboot
